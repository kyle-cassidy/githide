import os

def init():
    """
    Initializes the tool by creating `.gitignore.local` and configures git to use it.
    """
    with open('.gitignore.local', 'w') as f:
        f.write('# Local gitignore file\n')
    os.system('git config core.excludesfile .gitignore.local')
    with open('.git/info/exclude', 'a') as f:
        f.write('.gitignore.local\n')
