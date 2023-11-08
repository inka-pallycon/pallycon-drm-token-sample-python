from pallycon.exception.pallycon_token_exception import PallyConTokenException
import re


class PlaybackPolicy:
    def __init__(self):
        self.__policy_persistent = None
        self.__policy_license_duration = None
        self.__policy_expire_date = None
        self.__policy_allowed_track_types = None
        self.__policy_rental_duration = None
        self.__policy_playback_duration = None
        self.__policy_max_stream_per_user = None

def persistent(self, persistent: bool):
        if isinstance(persistent, bool):
            self.__policy_persistent = persistent
        else:
            raise PallyConTokenException('1009')
        return self

    def license_duration(self, license_duration: int):
        if isinstance(license_duration, int) and not isinstance(license_duration, bool):
            self.__policy_license_duration = license_duration
        else:
            raise PallyConTokenException('1010')
        return self

    def expire_date(self, expire_date: str):
        if isinstance(expire_date, str) and _check_dates(expire_date):
            self.__policy_expire_date = expire_date
        else:
            raise PallyConTokenException('1011')
        return self

    def allowed_track_types(self, allowed_track_types: str):
        from pallycon.config.allowed_track_types import check
        if isinstance(allowed_track_types, str) and check(allowed_track_types):
            self.__policy_allowed_track_types = allowed_track_types
        else:
            raise PallyConTokenException('1012')
        return self

    def rental_duration(self, rental_duration: int):
        if isinstance(rental_duration, int) and not isinstance(rental_duration, bool):
            self.__policy_rental_duration = rental_duration
        else:
            raise PallyConTokenException('1049')
        return self

    def playback_duration(self, playback_duration: int):
        if isinstance(playback_duration, int) and not isinstance(playback_duration, bool):
            self.__policy_playback_duration = playback_duration
        else:
            raise PallyConTokenException('1050')
        return self

    def max_stream_per_user(self, max_stream_per_user: int):
        if isinstance(max_stream_per_user, int) and not isinstance(max_stream_per_user, bool):
            self.__policy_max_stream_per_user = max_stream_per_user
        else:
            raise PallyConTokenException('1053')
        return self

    """ getter of persistent, license_duration, expire_date and allowed_track_types """
    def get_persistent(self) -> bool:
        return self.__policy_persistent

    def get_license_duration(self) -> int:
        return self.__policy_license_duration

    def get_expire_date(self) -> str:
        return self.__policy_expire_date

    def get_allowed_track_types(self) -> str:
        return self.__policy_allowed_track_types

    def get_rental_duration(self) -> int:
        return self.__policy_rental_duration

    def get_playback_duration(self) -> int:
        return self.__policy_playback_duration

    def get_max_stream_per_user(self) -> int:
        return self.__policy_max_stream_per_user

    def dict(self):
        playback_policy = {}

        if self.__policy_persistent is not None:
            playback_policy['persistent'] = self.__policy_persistent
        if self.__policy_license_duration is not None:
            playback_policy['license_duration'] = self.__policy_license_duration
        if self.__policy_expire_date is not None:
            playback_policy['expire_date'] = self.__policy_expire_date
        if self.__policy_allowed_track_types is not None:
            playback_policy['allowed_track_types'] = self.__policy_allowed_track_types
        if self.__policy_rental_duration is not None:
            playback_policy['rental_duration'] = self.__policy_rental_duration
        if self.__policy_playback_duration is not None:
            playback_policy['playback_duration'] = self.__policy_playback_duration
        if self.__policy_max_stream_per_user is not None:
            playback_policy['max_stream_per_user'] = self.__policy_max_stream_per_user

        return playback_policy


def _check_dates(expire_date: str) -> bool:
    pattern = re.match(
        "^[0-9]{4}-[0,1][0-9]-[0-5][0-9]T([0-2][0-9]:[0-5][0-9]:[0-5][0-9])Z$",
        expire_date)
    return pattern
