class File:

    def __init__(self, **kwargs):
        self.file_id = kwargs.get('file_id')
        self.file_size = kwargs.get('file_size')
        self.file_path = kwargs.get('file_path')
