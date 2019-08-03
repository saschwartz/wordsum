import os, sys
import gensim
from io import BytesIO
from google.cloud import storage
import logging

logging.basicConfig(level='INFO')
logger = logging.getLogger('models')

logger.info('Beginning model load')
model = None

local_model_path = os.environ.get('LOCAL_MODEL_PATH', None)
if local_model_path:
    logger.info('Loading model locally from LOCAL_MODEL_PATH: {}'.format(local_model_path))
    model = gensim.models.KeyedVectors.load_word2vec_format(
        local_model_path,
        binary=True,
        limit=100000
    )

gcs_model_bucket = os.environ.get('GCS_MODEL_BUCKET', None)
gcs_model_path = os.environ.get('GCS_MODEL_PATH', None)
if gcs_model_bucket and gcs_model_path:
    logger.info('Loading model file from GCS.')
    logger.info('GCS_MODEL_BUCKET: {}'.format(gcs_model_bucket))
    logger.info('GCS_MODEL_PATH: {}'.format(gcs_model_path))
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(gcs_model_bucket)
    blob = bucket.blob(gcs_model_path)
    data = blob.download_as_string()
    output = BytesIO()
    output.write(data)
    logger.info('Loading GCS model file into gensim.')
    model = gensim.models.KeyedVectors.load_word2vec_format(
        output,
        binary=True,
        limit=100000
    )

if not model:
    logger.exception('Could not load model! Exiting.')
    sys.exit(1)

logger.info('Done loading model!')