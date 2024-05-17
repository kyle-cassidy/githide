import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def list():
    """
    Lists all hidden files.
    """
    logging.info('Listing files in .gitignore.local')
    with open('.gitignore.local', 'r') as f:
        lines = f.readlines()
    logging.info('Files listed from .gitignore.local')
    return [line.strip() for line in lines]
