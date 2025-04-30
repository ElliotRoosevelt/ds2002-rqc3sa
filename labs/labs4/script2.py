#!/bin/bashC
set -e
import boto3
s3=boto3.client(‘s3’)

# vars needed
bucket_name = ‘bucket’
object_name = ‘object’
expires_in = 3000

#fetch
def download_file(url, object_name):
urllib.request.urlretrieve(url, local_filename)

#upload
def upload_file(file_name. bucket_name. object_name):
response= s3_client.upload_file(file_name. bucket_name. Object_name)
print(response)
Return True
upload_file(“file.png”. “ds2002-rqc3sa”. “newname.png”)


#output presigned
def generate_presigned_url(bucket_name, object_name, expires_in):
    response = s3.generate_presigned_url(
        'get_object',
        Params={'Bucket':bucket, 'Key':object},
        ExpiresIn=expires_in
    )
    return response

url = ‘https://img.freepik.com/free-psd/macaroon-isolated-transparent-background_191095-35017.jpg?semt=ais_hybrid&w=740'  
local_filename = 'newname.png'
download_file(url, local_filename)
upload_file(local_filename, 'bucket', 'newname.png')
presigned_url = generate_presigned_url('bucket', 'newname.png', expires_in)


