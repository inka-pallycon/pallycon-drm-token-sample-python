from pallycon.exception.pallycon_token_exception import PallyConTokenException
from pallycon.token.v2.security_policy_widevine import SecurityPolicyWidevine
from pallycon.token.v2.security_policy_playready import SecurityPolicyPlayready
from pallycon.token.v2.security_policy_fairplay import SecurityPolicyFairplay
from pallycon.token.v2.security_policy_ncg import SecurityPolicyNcg



class SecurityPolicy:
    def __init__(self):
        self.__security_track_type = 'ALL'
        self.__security_widevine = None
        self.__security_playready = None
        self.__security_fairplay = None
        self.__security_ncg = None

    """ setter """
    def track_type(self, track_type: str):
        from pallycon.config.track_type import check
        if isinstance(track_type, str) and check(track_type):
            self.__security_track_type = track_type
        else:
            raise PallyConTokenException('1013')
        return self

    def widevine(self, widevine: SecurityPolicyWidevine):
        if isinstance(widevine, SecurityPolicyWidevine):
            self.__security_widevine = widevine.dict()
        else:
            raise PallyConTokenException('1014')
        return self

    def playready(self, playready: SecurityPolicyPlayready):
        if isinstance(playready, SecurityPolicyPlayready):
            self.__security_playready = playready.dict()
        else:
            raise PallyConTokenException('1015')
        return self

    def fairplay(self, fairplay: SecurityPolicyFairplay):
        if isinstance(fairplay, SecurityPolicyFairplay):
            self.__security_fairplay = fairplay.dict()
        else:
            raise PallyConTokenException('1016')
        return self

    def ncg(self, ncg: SecurityPolicyNcg):
        if isinstance(ncg, SecurityPolicyNcg):
            self.__security_ncg = ncg.dict()
        else:
            raise PallyConTokenException('1017')
        return self

    """ getter """
    def get_widevine(self) -> dict:
        return self.__security_widevine

    def get_playready(self) -> dict:
        return self.__security_playready

    def get_fairplay(self) -> dict:
        return self.__security_fairplay

    def get_ncg(self) -> dict:
        return self.__security_ncg

    def dict(self) -> dict:
        security_policy = {
            'track_type': self.__security_track_type
        }
        if self.__security_widevine is not None:
            security_policy['widevine'] = self.__security_widevine
        if self.__security_playready is not None:
            security_policy['playready'] = self.__security_playready
        if self.__security_fairplay is not None:
            security_policy['fairplay'] = self.__security_fairplay
        if self.__security_ncg is not None:
            security_policy['ncg'] = self.__security_ncg

        return security_policy



