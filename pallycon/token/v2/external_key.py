from typing import List, Union

from pallycon.exception.pallycon_token_exception import PallyConTokenException
from pallycon.token.v2.external_key_hls_aes import ExternalKeyHlsAes
from pallycon.token.v2.external_key_mpeg_cenc import ExternalKeyMpegCenc
from pallycon.token.v2.external_key_ncg import ExternalKeyNcg


class ExternalKey:
    def __init__(self):
        self.__external_mpeg_list = []
        self.__external_hls_list = []
        self.__external_ncg = None

    """
    constructs a mpegCenc list 
    in two ways
        - at once using a list of mpegCenc
        - adding a mpegCenc to existing mpegCenc list step-by-step.
    this mpeg_cenc list or object will be converted to dictionary type. 
    """

    def mpeg_cenc(self, mpeg_cenc: Union[List[ExternalKeyMpegCenc], ExternalKeyMpegCenc]):
        if isinstance(mpeg_cenc, list):
            mpeg_cenc_list = [item.dict() for item in mpeg_cenc]
            self.__external_mpeg_list = mpeg_cenc_list
        elif isinstance(mpeg_cenc, ExternalKeyMpegCenc):
            self.__external_mpeg_list.append(mpeg_cenc.dict())
        else:
            raise PallyConTokenException('1019')
        return self

    """
    constructs a HlsAes list 
    in two ways
        - at once using a list of HlsAes
        - adding a HlsAes to existing HlsAes list step-by-step.
    this hls_aes list or object will be converted to dictionary type. 
    """

    def hls_aes(self, hls_aes: Union[List[ExternalKeyHlsAes], ExternalKeyHlsAes]):
        if isinstance(hls_aes, list):
            hls_aes_list = [item.dict() for item in hls_aes]
            self.__external_hls_list = hls_aes_list
        elif isinstance(hls_aes, ExternalKeyHlsAes):
            self.__external_hls_list.append(hls_aes.dict())
        else:
            raise PallyConTokenException('1020')
        return self

    def ncg(self, ncg: ExternalKeyNcg):
        if isinstance(ncg, ExternalKeyNcg):
            self.__external_ncg = ncg.dict()
        else:
            raise PallyConTokenException('1021')
        return self

    def get_mpeg_cenc(self) -> List[dict]:
        return self.__external_mpeg_list

    def get_hls_aes(self) -> List[dict]:
        return self.__external_hls_list

    def get_ncg(self) -> dict:
        return self.__external_ncg

    def check(self):
        result = True
        mpeg_list_len = len(self.__external_mpeg_list)
        hls_list_len = len(self.__external_hls_list)
        if (mpeg_list_len + hls_list_len) is 0 \
                and self.__external_ncg is None:
            result = False
            # raise PallyConTokenException('1018')
        return result

    def dict(self) -> dict:
        external_key = {}
        if len(self.__external_mpeg_list) > 0:
            external_key['mpeg_cenc'] = self.__external_mpeg_list
        if len(self.__external_hls_list) > 0:
            external_key['hls_aes'] = self.__external_hls_list
        if self.__external_ncg is not None:
            external_key['ncg'] = self.__external_ncg

        return external_key

