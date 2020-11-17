class WrongFileTypeException(Exception):
    def __init__(self, message):
        self.message = message


class InvalidFileDataException(ValueError):
    def __init__(self, message):
        self.message = message


class FileNotFoundException(FileNotFoundError):
    def __init__(self, message):
        self.message = message
