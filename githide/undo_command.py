def undo():
    """
    Undoes the last hide operation.
    """
    with open('.gitignore.local', 'r') as f:
        lines = f.readlines()
    if lines:
        with open('.gitignore.local', 'w') as f:
            f.writelines(lines[:-1])
