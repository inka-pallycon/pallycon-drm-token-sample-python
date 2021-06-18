from pallycon.exception.pallycon_token_exception import PallyConTokenException
from pallycon.config import track_type as mpeg_track_type
from pallycon.config.track_type import check


class ExternalKeyMpegCenc:
    def __init__(self, track_type: mpeg_track_type = '', key_id: str = '', key: str = '', iv: str = None):

        if isinstance(track_type, str) and check(track_type):
            self.__track_type = track_type
        else:
            raise PallyConTokenException('1039')

        if isinstance(key_id, str) and _check_hex16(key_id):
            self.__key_id = key_id
        else:
            raise PallyConTokenException('1040')

        if isinstance(key, str) and _check_hex16(key):
            self.__key = key
        else:
            raise PallyConTokenException('1041')

        if isinstance(iv, str) and _check_hex16(iv):
            self.__iv = iv
        elif iv is None:
            self.__iv = None
        else:
            raise PallyConTokenException('1042')

    @property
    def track_type(self) -> mpeg_track_type:
        return self.__track_type

    @property
    def key_id(self) -> str:
        return self.__key_id

    @property
    def key(self) -> str:
        return self.__key

    @property
    def iv(self) -> str:
        return self.__iv

    def dict(self):
        mpeg_cenc = {
            'track_type': self.__track_type,
            'key_id': self.__key_id,
            'key': self.__key
        }
        if hasattr(self, '_ExternalKeyMpegCenc__iv'):
            mpeg_cenc['iv'] = self.__iv
        return mpeg_cenc


def _check_hex16(words) -> bool:
    import re
    test = re.compile('^[0-9a-f]{32}$')
    pattern = test.match(words)
    if pattern is None:
        pattern = False
    else:
        pattern = True
    return pattern


