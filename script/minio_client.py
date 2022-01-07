from minio import Minio
import os

DEFAULT_UPDATED_SAVED_WEIGHTS = './distilbert_saved_weights_new.pt'
DEFAULT_BUCKET_NAME = 'jx-test'

# DEFAULT_BUCKET_NAME = 'jx-test'
TEST_FILE = './test.pt'
class MinioClient:
    def __init__(self):
        MINIO_ACCESS_KEY = os.environ.get("MINIO_ACCESS_KEY")
        MINIO_SECRET_KEY = os.environ.get("MINIO_SECRET_KEY")
        self.client = Minio("minio.covid-polygraph.ml", access_key=MINIO_ACCESS_KEY, secret_key=MINIO_SECRET_KEY)

    def fetch_update(self, bucket_name, object_name):
        self.client.fget_object(bucket_name, object_name, DEFAULT_UPDATED_SAVED_WEIGHTS)
        return DEFAULT_UPDATED_SAVED_WEIGHTS
    
    # # testing only
    # def upload(self, object_name):
    #     self.client.fput_object(DEFAULT_BUCKET_NAME, object_name, TEST_FILE)
    #     return object_name
client = MinioClient()