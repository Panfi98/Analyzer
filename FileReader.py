class FileReader:
    """This class reads strings from a file and stores
    them into lists."""
    def __init__(self, filename, filepath = str()):
        self.filename = filename
        self.filepath = filepath
        self.data = []

    def fileReader(self):
        file = open(filepath+filename)

