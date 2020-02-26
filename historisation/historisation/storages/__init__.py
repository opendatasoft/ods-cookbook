from .local import LocalStorage
from .ftp import FTPStorage

storages = {
    'local': LocalStorage,
    'ftp': FTPStorage
}