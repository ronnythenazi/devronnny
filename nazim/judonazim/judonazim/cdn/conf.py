import os
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_S3_ENDPOINT_URL = "https://fra1.digitaloceanspaces.com"
AWS_S3_OBJECT_PARAMETERS = {
  "CacheControl": "max-age=86400",
}
AWS_LOCATION = f"https://{AWS_STORAGE_BUCKET_NAME}.fra1.digitaloceanspaces.com"

#DEFAULT_FILE_STORAGE = "judonazim.cdn.backends.MediaRootS3Boto3Storage"
DEFAULT_FILE_STORAGE = "judonazim.cdn.backends.MediaRootS3Boto3Storage"

#STATICFILES_STORAGE = "judonazim.cdn.backends.StaticRootS3Boto3Storage"



#new

AWS_DEFAULT_ACL = 'public-read'


# Use AWS_S3_ENDPOINT_URL here if you haven't enabled the CDN and got a custom domain.
#STATIC_URL = '{}/{}/'.format(AWS_S3_ENDPOINT_URL, 'static')
#STATIC_ROOT = 'static/'
