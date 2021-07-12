import json
from typing import Union, List
from ..exception.pallycon_token_exception import PallyConTokenException

from pallycon.token.v2.playback_policy import PlaybackPolicy
from pallycon.token.v2.security_policy import SecurityPolicy
from pallycon.token.v2.external_key import ExternalKey


class PallyConDrmTokenPolicy:
    def __init__(self):
        self.__policy_version = 2
        self.__policy_playback = None
        self.__policy_security = []
        self.__policy_external = None

    """ setter """
    def playback(self, playback: PlaybackPolicy):
        if isinstance(playback, PlaybackPolicy):
            self.__policy_playback = playback.dict()
        else:
            raise PallyConTokenException('1006')
        return self


    """
    constructs a SecurityPolicy list 
    in two ways
        - at once using a list of SecurityPolicy
        - adding a SecurityPolicy to existing HlsAes list step-by-step.
    this security_policy list or object will be converted to dictionary type. 
    """
    def security(self, security: Union[List[SecurityPolicy], SecurityPolicy]):
        if isinstance(security, list):
            security_list = [item.dict() for item in security]
            self.__policy_security = security_list
        elif isinstance(security, SecurityPolicy):
            self.__policy_security.append(security.dict())
        else:
            raise PallyConTokenException('1007')
        return self

    def external(self, external: ExternalKey):
        if isinstance(external, ExternalKey) and external.check():
            self.__policy_external = external.dict()
        elif isinstance(external, ExternalKey) and not external.check():
            raise PallyConTokenException('1018')  # if the external_key is empty even if it called
        else:
            raise PallyConTokenException('1008')
        return self


    """ getter """
    def get_playback(self) -> dict:
        return self.__policy_playback

    def get_security(self) -> List[dict]:
        return self.__policy_security

    def get_external(self) -> dict:
        return self.__policy_external

    def dict(self):
        policy = {
            'policy_version': self.__policy_version
        }
        if self.__policy_playback is not None:
            policy['playback_policy'] = self.__policy_playback
        if len(self.__policy_security) > 0:
            policy['security_policy'] = self.__policy_security
        if self.__policy_external is not None:
            policy['external_policy'] = self.__policy_external

        return policy

    def to_json_str(self):
        return json.dumps(self.dict())



