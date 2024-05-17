def list():
    """
    Lists all hidden files.
    """
    with open('.gitignore.local', 'r') as f:
        lines = f.readlines()
    for line in lines:
        print(line.strip())
