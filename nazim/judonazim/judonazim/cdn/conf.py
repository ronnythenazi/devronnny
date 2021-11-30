import os

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")


AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_S3_ENDPOINT_URL = "https://fra1.digitaloceanspaces.com/media/"

#gunicorn --worker-tmp-dir /dev/shm judonazim.wsgi
#gunicorn --worker-tmp-dir /dev/shm judonazim.wsgi


AWS_S3_OBJECT_PARAMETERS = {
  "CacheControl": "max-age=86400",
}
AWS_LOCATION =  "https://ronnythenazi.fra1.digitaloceanspaces.com" #f"https://{AWS_STORAGE_BUCKET_NAME}.fra1.digitaloceanspaces.com"



DEFAULT_FILE_STORAGE = "judonazim.cdn.backends.MediaRootS3Boto3Storage"

AWSS3ADDRESSING_STYLE = 'virtual'

AWS_DEFAULT_ACL = 'public-read'

#this link may solve my problem

#https://coolestguidesontheplanet.com/no-video-with-supported-format-and-mime-type-found/
