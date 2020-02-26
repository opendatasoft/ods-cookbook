class Storage(object):
    # returns a string with the content of the file or None if it does not exist.
    def get(self, path):
        pass

    # returns true if the file exists
    def exists(self, path):
        pass

    # saves a file-like object at the given location
    def save(self, path, file):
        pass

    # returns a list of directories from the root
    def get_dirs(self):
        pass

    # returns the files from a given directory
    def get_files(self, path):
        pass

    # creates a new directory
    def mkdir(self, path):
        pass

    # moves
    def move(self, source, dest):
        pass

    # join
    def join(self, *paths):
        pass
