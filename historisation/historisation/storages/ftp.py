from ftplib import FTP, error_perm, all_errors, error_temp
import io
import logging

from ..storage import Storage

logger = logging.getLogger(__name__)


class FTPStorage(Storage):
    def __init__(self, root_dir='/historisation', host='localhost', username=None, password=None):
        super(Storage, self).__init__()
        self.root_dir = root_dir
        self.host = host
        self.username = username
        self.password = password
        self._ftp = None

    def get(self, path):
        ftp = self._get_ftp()
        stream = io.StringIO()

        def write(line):
            stream.write(line.decode('utf8'))

        try:
            ftp.retrlines('RETR %s' % path, write)
            stream.seek(0)
            return stream.read()
        except error_perm:
            return None

    def exists(self, path):
        ftp = self._get_ftp()
        try:
            ftp.nlst(path)
            return True
        except error_temp:
            return False

    def save(self, path, lines):
        ftp = self._get_ftp()
        if type(lines) is str:
            lines = io.StringIO(lines.decode('utf8'))
        ftp.storlines('APPE %s' % path, lines)

    def mkdir(self, path):
        ftp = self._get_ftp()
        try:
            ftp.mkd(path)
        except error_perm:
            pass

    def get_dirs(self):
        ftp = self._get_ftp()
        return ftp.nlst()

    def get_files(self, path):
        ftp = self._get_ftp()
        return [file_path.split('/')[-1] for file_path in ftp.nlst(path)]

    def join(self, *paths):
        return '/'.join(paths)

    def move(self, source, dest):
        ftp = self._get_ftp()
        ftp.rename(source, dest)

    def _get_ftp(self):
        if not self._ftp:
            return self._get_new_ftp()

        try:
            self._ftp.cwd(self.root_dir)
            return self._ftp
        except all_errors:
            return self._get_new_ftp()

    def _get_new_ftp(self):
        self._ftp = FTP(self.host)
        self._ftp.login(self.username, self.password)
        try:
            self._ftp.mkd(self.root_dir)
        except error_perm:
            pass

        self._ftp.cwd(self.root_dir)
        return self._ftp

    def cd_root(self, ftp):
        ftp.cwd(self.root_dir)
        return ftp
