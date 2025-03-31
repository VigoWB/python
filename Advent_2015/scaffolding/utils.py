def loadFile(path):
    with open(path, 'rb') as pointer:
        return pointer.read()


def loadLines(path):
    with open(path, 'rb') as pointer:
        return pointer.readlines()