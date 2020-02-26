import argparse
import sys
import json
import logging

from historisation import Historifier
from historisation.storages import LocalStorage, FTPStorage, storages

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('config', type=str)
    parser.add_argument('--keep-tmp', action='store_false')

    args = parser.parse_args(sys.argv[1:])
    #logger.debug(args)

    config = None

    with open(args.config, 'r') as config_file:
        config = json.load(config_file)

    storage = storages[config['storage']['type']](**config['storage']['params'])
    historifier = Historifier(storage=storage, **config['historifier'])

    tmp_f, fetch_time = getattr(historifier, config['action']['type'])(**config['action']['params'])
    historifier.save(tmp_f, fetch_time)
