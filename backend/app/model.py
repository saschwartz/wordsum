import os
import gensim
import logging

logger = logging.getLogger('models')

model = None
if os.environ.get('ENVIRONMENT', 'production') == 'test': 
    model_path = '/usr/src/wordsum/dev/models/GoogleNews-vectors-negative300.bin.gz'
    logger.info('In test environment, loading model from: {}'.format(model_path))
    model = gensim.models.KeyedVectors.load_word2vec_format(
        '/usr/src/wordsum/dev/models/GoogleNews-vectors-negative300.bin.gz',
        binary=True
    )
    logger.info('Done loading model!')