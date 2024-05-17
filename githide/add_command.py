import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def add(file):
    """
    Adds a file to the hidden list.
    """
    logging.info(f'Adding {file} to .gitignore.local')
    with open('.gitignore.local', 'a') as f:
        f.write(f'{file}\n')
    logging.info(f'{file} added to .gitignore.local')
