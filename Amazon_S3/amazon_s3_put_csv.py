import boto3

s3 = boto3.client(
    's3',
    aws_access_key_id='AKIAWN5WN37JHC2EBHYG',
    aws_secret_access_key='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'
)

with open('upload_file.txt', 'rb') as f:
    s3.put_object(Bucket='rainbow-engine-test', Key='upload_file.txt', Body=f)