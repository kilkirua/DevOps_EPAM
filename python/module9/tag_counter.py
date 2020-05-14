import requests
from collections import Counter
from bs4 import BeautifulSoup
import json
import datetime
import boto3
from botocore.exceptions import ClientError
import logging
import argparse


class TagCounter():
    """The class TagCounter() counts tags on an HTML page. Accepts a link to a web page.
    It is possible to use as a module.
    TagCounter() has the ability to log in a local directory, as well as upload the log to s3 bucket.
    """
    def __init__(self, url):
        """

        :param url: Page for tag count
        """
        self.request = requests.get(url,
                               headers={'Accept-Language': 'En-us'})
        self.soup = BeautifulSoup(self.request.text, 'lxml')

    def count(self):
        """

        :return: Dictionary with the total number of tags and the number of each tag
        """
        tags = [tag.name for tag in self.soup.body.find_all()]
        c = Counter(tags)
        result = {
            sum(c.values()): json.dumps(c)
        }
        return result

    def log(self, log_name):
        """

        :param log_name: Name of log file
        """
        self.log_name = log_name

        date = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')

        with open(self.log_name, 'a') as w_file:
            log_string = f"{date} {self.request.url} {self.count()}\n"
            w_file.write(log_string)

    @staticmethod
    def upload_file(file_name, bucket, object_name=None):
        """Upload a file to an S3 bucket

            :param file_name: File to upload
            :param bucket: Bucket to upload to
            :param object_name: S3 object name. If not specified then file_name is used
            :return: True if file was uploaded, else False
        """

        # If S3 object_name was not specified, use file_name
        if object_name is None:
            object_name = file_name

        # Upload the file
        s3_client = boto3.client('s3')
        try:
            response = s3_client.upload_file(file_name, bucket, object_name)
            print(f"{file_name} uploaded successfully in {bucket}")
        except ClientError as e:
            logging.error(e)
            return False
        return True

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=TagCounter.__doc__)
    parser.add_argument('url', type=str, help=TagCounter.count.__doc__)
    parser.add_argument('-w', type=str, help=TagCounter.log.__doc__, nargs='?', const=f'{parser.prog}.log', metavar='FILENAME')
    parser.add_argument('-s3', type=str, nargs='+', help=TagCounter.upload_file.__doc__,
                        metavar=('FILE_TO_UPLOAD BUCKET_TO_UPLOAD', 'S3_OBJECT_NAME'))

    args = parser.parse_args()

    counter = TagCounter(args.url)
    print(counter.count())

    if args.w and args.s3:
        if args.s3 and len(args.s3) < 2:
            counter.log(args.w)
            parser.print_help()
            exit()
        else:
            try:
                args.s3[2]
            except IndexError:
                args.s3.append(args.s3[0])
            counter.log(args.w)
            counter.upload_file(args.s3[0], args.s3[1], args.s3[2])
    elif args.w:
        counter.log(args.w)
    elif args.s3:
        try:
            args.s3[2]
        except IndexError:
            args.s3.append(args.s3[0])
        counter.upload_file(args.s3[0], args.s3[1], args.s3[2])





# test = TagCounter("https://google.com/")
# print(test.count())
# print(test.log("counter_html.log"))
# test.upload_file('counter_html.log', "kilkiruato")
