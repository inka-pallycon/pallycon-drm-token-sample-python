from pallycon.exception.pallycon_token_exception import PallyConTokenException

class SecurityPolicyFairplay:
    def __init__(self):
        self.__fairplay_hdcp_enforcement = None
        self.__fairplay_allow_airplay = None
        self.__fairplay_allow_av_adapter = None


    """ setter """
    def hdcp_enforcement(self, hdcp_enforcement: int):
        from pallycon.config.fairplay_hdcp_enforcement import check
        if check(hdcp_enforcement):
            self.__fairplay_hdcp_enforcement = hdcp_enforcement
        else:
            raise PallyConTokenException('1033')
        return self

    def allow_airplay(self, allow_airplay: bool):
        if isinstance(allow_airplay, bool):
            self.__fairplay_allow_airplay = allow_airplay
        else:
            raise PallyConTokenException('1034')
        return self

    def allow_av_adapter(self, allow_av_adapter: bool):
        if isinstance(allow_av_adapter, bool):
            self.__fairplay_allow_av_adapter = allow_av_adapter
        else:
            raise PallyConTokenException('1035')
        return self

    """ getter """
    def get_hdcp_enforcement(self) -> int:
        return self.__fairplay_hdcp_enforcement

    def get_allow_airplay(self) -> bool:
        return self.__fairplay_allow_airplay

    def get_allow_av_adapter(self) -> bool:
        return self.__fairplay_allow_av_adapter

    def dict(self):
        fairplay = {}

        if self.__fairplay_hdcp_enforcement is not None:
            fairplay['hdcp_enforcement'] = self.__fairplay_hdcp_enforcement
        if self.__fairplay_allow_airplay is not None:
            fairplay['allow_airplay'] = self.__fairplay_allow_airplay
        if self.__fairplay_allow_av_adapter is not None:
            fairplay['allow_av_adapter'] = self.__fairplay_allow_av_adapter

        return fairplay
