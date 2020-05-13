from sys import argv
import boto3

# s3_from = list(argv[1])  # list of s3 buckets
# s3_to = argv[2]  # copy files from list to this bucket

def copy_files(s3_from, s3_to):
    s3 = boto3.resource('s3')

    if s3.Bucket(s3_to) not in s3.buckets.all():
        s3.create_bucket(Bucket=s3_to)
        s3.Bucket(s3_to).wait_until_exists()
        print(f"Created {s3.Bucket(s3_to).name} bucket")

    for bucket in s3_from:
        for file in s3.Bucket(bucket).objects.all():
            file_from = {'Bucket': file.bucket_name,
                         'Key': file.key,
                         }
            s3.Bucket(s3_to).copy(file_from, file.key)
            print(f"Copied {file.key}")


#copy_files(['kilkiruafrom2', 'kilkiruafrom1'], "kilkiruato")
