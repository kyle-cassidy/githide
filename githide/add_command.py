def add(file):
    """
    Adds a file to the hidden list.
    """
    with open('.gitignore.local', 'a') as f:
        f.write(f'{file}\n')
