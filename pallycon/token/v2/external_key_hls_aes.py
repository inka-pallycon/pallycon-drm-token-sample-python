from pallycon.exception.pallycon_token_exception import PallyConTokenException
from pallycon.config import track_type as hls_aes_track_type
from pallycon.config.track_type import check


class ExternalKeyHlsAes:
    def __init__(self, track_type: hls_aes_track_type = '', key_id: str = '', key: str = ''):

        if isinstance(track_type, str) and check(track_type):
            self.__track_type = track_type
        else:
            raise PallyConTokenException('1043')

        if isinstance(key_id, str) and _check_hex16(key_id):
            self.__key_id = key_id
        else:
            raise PallyConTokenException('1044')

        if isinstance(key, str) and _check_hex16(key):
            self.__key = key
        else:
            raise PallyConTokenException('1045')

    @property
    def track_type(self) -> hls_aes_track_type:
        return self.__track_type

    @property
    def key_id(self) -> str:
        return self.__key_id

    @property
    def key(self) -> str:
        return self.__key

    def dict(self):
        hls_aes = {
            'track_type': self.__track_type,
            'key_id': self.__key_id,
            'key': self.__key
        }
        return hls_aes


def _check_hex16(words) -> bool:
    import re
    test = re.compile('^[0-9a-f]{32}$')
    pattern = test.match(words)
    if pattern is None:
        pattern = False
    else:
        pattern = True
    return pattern
