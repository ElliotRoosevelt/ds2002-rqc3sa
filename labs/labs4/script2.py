#!/bin/bashC
set -e
import boto3
s3=boto3.client(‘s3’)

# vars needed
bucket_name = str
object_name = str
expires_in = int

#fetch
def download_file(url, object_name):
urllib.request.urlretrieve(url, local_filename)
print(response)

#upload
def upload_file(file_name. bucket_name. object_name):
response= s3_client.upload_file(file_name. bucket_name. Object_name)
print(response)
Return True
upload_file(“file.png”. “ds2002-rqc3sa”. “newname.png”)


#output presigned
response = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket_name, 'Key': object_name},
    ExpiresIn=expires_in
)
