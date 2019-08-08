from .photo_size import PhotoSize


class Video:

    def __init__(self, **kwargs):
        self.file_id = kwargs.get('file_id')
        self.width = kwargs.get('width')
        self.height = kwargs.get('height')
        self.duration = kwargs.get('duration')
        self.thumb = PhotoSize(**kwargs['thumb']) if 'thumb' in kwargs else None
        self.mime_type = kwargs.get('mime_type')
        self.file_size = kwargs.get('file_size')
