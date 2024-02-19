import logging.config
import os


LOGLEVEL = os.environ.get('LOGLEVEL', 'DEBUG').upper()

logging_config = {
    'version' : 1,
    'disable_existng_loggers' : False,
    'formatters':{
        'simple':{
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        }
    },
    'handlers':{
        'stdout':{
            'class': 'logging.StreamHandler',
            'level': LOGLEVEL,
            'formatter': 'simple',
            'stream': 'ext://sys.stdout',
        }
    },
    'loggers':{
        'root' :{'level': LOGLEVEL,'handlers': ['stdout']}
    },
}

logging.config.dictConfig(config=logging_config)