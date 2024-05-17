import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def undo():
    """
    Undoes the last hide operation.
    """
    logging.info('Undoing the last hide operation')
    with open('.gitignore.local', 'r') as f:
        lines = f.readlines()
    if lines:
        with open('.gitignore.local', 'w') as f:
            f.writelines(lines[:-1])
    logging.info('Last hide operation undone')
