def remove(file):
    """
    Removes a file from the hidden list.
    """
    with open('.gitignore.local', 'r') as f:
        lines = f.readlines()
    with open('.gitignore.local', 'w') as f:
        for line in lines:
            if line.strip() != file:
                f.write(line)
