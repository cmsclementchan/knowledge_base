
import boto3
# pip install boto3 

# Initialize interfaces
s3Client = boto3.client('s3')
s3Resource = boto3.resource('s3')


# Create a byte string to send to bucket
putMessage = b'Hi! Hello World'

def put_object(buket_name,key):
    # put_object
    response = s3Client.put_object(
        Body = putMessage,
        Bucket = buket_name,
        Key = key
    )
    print(response)
    return


def upload_file(filename,des_folder,des_filename):
    # upload_file
    boto3Upload = filename
    s3Resource.meta.client.upload_file(boto3Upload, des_folder, des_filename)
    return

