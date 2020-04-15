from sys import argv
char = int(argv[1])
if -15 < char <= 12 or 14 < char < 17 or 19 <= char:
    print("True")
else:
    print("False")
