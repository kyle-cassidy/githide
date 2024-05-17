import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def remove(file):
    """
    Removes a file from the hidden list.
    """
    logging.info(f'Removing {file} from .gitignore.local')
    with open('.gitignore.local', 'r') as f:
        lines = f.readlines()
    with open('.gitignore.local', 'w') as f:
        for line in lines:
            if line.strip() != file:
                f.write(line)
    logging.info(f'{file} removed from .gitignore.local')
