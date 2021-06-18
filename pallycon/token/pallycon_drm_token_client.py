import json
import base64
import hashlib

from Crypto.Cipher import AES
import pytz
import datetime
from pallycon.exception.pallycon_token_exception import PallyConTokenException


def _pad(words):
    BS = 16
    print('words', words)
    print('text length', len(words))
    print('block size', (BS - len(words) % BS))
    return (words + (BS - len(words) % BS) * chr(BS - len(words) % BS)).encode("utf-8")


class PallyConDrmTokenClient:
    def __init__(self):
        self.__drm_type = "PlayReady"
        self.__AES_IV = "0123456789abcdef"
        self.__site_key = None
        self.__access_key = None
        self.__site_id = None
        self.__user_id = None
        self.__cid = None
        self.__policy = None
        self.__enc_policy = None
        self.__response_format = 'original'
        self.__payload = None

    def site_key(self, site_key):
        self.__site_key = site_key
        return self

    def access_key(self, access_key):
        self.__access_key = access_key
        return self

    def playready(self):
        self.__drm_type = "PlayReady"
        return self

    def widevine(self):
        self.__drm_type = "Widevine"
        return self

    def fairplay(self):
        self.__drm_type = "FairPlay"
        return self

    def site_id(self, site_id):
        self.__site_id = site_id
        return self

    def user_id(self, user_id):
        self.__user_id = user_id
        return self

    def cid(self, cid):
        self.__cid = cid
        return self

    def policy(self, policy):
        self.__policy = policy.to_json_str()
        self.__enc_policy = (self.__make_enc_policy(self.__policy)).decode("utf-8")
        return self

    def response_format(self, response_format):
        from pallycon.config.response_format import check
        if check(response_format):
            self.__response_format = response_format
        else:
            raise PallyConTokenException('1048')
        return self

    def __timestamp(self):
        timezone = pytz.timezone("UTC")
        new_datetime = datetime.datetime.now(timezone).strftime("%Y-%m-%dT%H:%M:%SZ")
        self.__timestamp = new_datetime
        return self

    def __hash(self):
        hash_input = (
                self.__access_key
                + self.__drm_type
                + self.__site_id
                + self.__user_id
                + self.__cid
                + self.__enc_policy
                + self.__timestamp
        )

        print('hash:::::', hash_input)

        hash_string = base64.b64encode(
            hashlib.sha256(bytes(hash_input, "utf-8")).digest()
        )
        print('encode::::::', hash_string)
        self.__hash = hash_string.decode("utf-8")
        return self

    def execute(self):
        try:
            self.__validation()
            self.__timestamp()
            self.__hash()
            payload_str = json.dumps(self.__get_payload())
            self.__payload = payload_str

            return base64.b64encode(payload_str.encode("utf-8")).decode("utf-8")

        except PallyConTokenException:
            raise

    """
    get parameters
    """
    def __get_payload(self):
        input_str = {
            "drm_type": self.__drm_type,
            "site_id": self.__site_id,
            "user_id": self.__user_id,
            "cid": self.__cid,
            "policy": self.__enc_policy,
            "response_format": self.__response_format,
            "timestamp": self.__timestamp,
            "hash": self.__hash,
        }
        return input_str

    def __make_enc_policy(self, msg):
        key = bytes(self.__site_key, "utf-8")
        raw = _pad(msg)
        print('padded text', raw)
        iv = self.__AES_IV.encode("utf-8")
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return base64.b64encode(cipher.encrypt(raw))

    def __validation(self):
        if self.__user_id is None:
            raise PallyConTokenException('1000')

        if self.__cid is None:
            raise PallyConTokenException('1001')

        if self.__site_id is None:
            raise PallyConTokenException('1002')

        if self.__access_key is None:
            raise PallyConTokenException('1003')

        if self.__site_key is None:
            raise PallyConTokenException('1004')

        if self.__policy is None:
            raise PallyConTokenException('1005')

    def get_drm_type(self):
        return self.__drm_type

    def get_site_id(self):
        return self.__site_id

    def get_user_id(self):
        return self.__user_id

    def get_cid(self):
        return self.__cid

    def get_policy(self):
        return self.__policy.to_json_str()

    def get_site_key(self):
        return self.__site_key

    def get_access_key(self):
        return self.__access_key

    def get_time_stamp(self):
        return self.__timestamp

    def get_hash(self):
        return self.__hash

    def get_response_format(self):
        return self.__response_format

    def to_json_str(self):
        return self.__payload



if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        from pathlib import Path
        set_path = Path(path.abspath(__file__)).parents[0]
        if set_path not in sys.path:
            sys.path.append(path.dirname(set_path))
