import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def init():
    """
    Initializes the tool by creating `.gitignore.local` and configures git to use it.
    """
    # Log the creation of .gitignore.local file
    logging.info('Creating .gitignore.local file')
    with open('.gitignore.local', 'w') as f:
        f.write('# Local gitignore file\n')

    # Log the configuration of git to use .gitignore.local
    logging.info('Configuring git to use .gitignore.local')
    os.system('git config core.excludesfile .gitignore.local')

    # Log the addition of .gitignore.local to .git/info/exclude
    logging.info('Adding .gitignore.local to .git/info/exclude')
    with open('.git/info/exclude', 'a') as f:
        f.write('.gitignore.local\n')

    # Output the current git config for core.excludesfile
    logging.info('Outputting current git config for core.excludesfile')
    os.system('git config --local --get core.excludesfile')
    logging.info('Initialization complete')
    
    
