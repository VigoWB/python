def loadFile(path):
    with open(path, 'r') as pointer:
        return pointer.read()


def loadLines(path):
    with open(path, 'r') as pointer:
        return pointer.readlines()