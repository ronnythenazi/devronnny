from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):
    bucket_name = 'ronnythenazi'
    location = 'media'
<<<<<<< HEAD
    default_acl = 'public-read'
=======
>>>>>>> 058c8427d62ca51e53049814e011646951b0babb
    file_overwrite = False
