import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def init():
    """
    Initializes the tool by creating `.gitignore.local` and configures git to use it.
    """
    logging.info('Creating .gitignore.local file')
    with open('.gitignore.local', 'w') as f:
        f.write('# Local gitignore file\n')
    logging.info('Configuring git to use .gitignore.local')
    os.system('git config core.excludesfile .gitignore.local')
    logging.info('Adding .gitignore.local to .git/info/exclude')
        f.write('# Local gitignore file\n')
    os.system('git config core.excludesfile .gitignore.local')
    with open('.git/info/exclude', 'a') as f:
        f.write('.gitignore.local\n')
