from pallycon.exception.pallycon_token_exception import PallyConTokenException


class SecurityPolicyWidevine:
    def __init__(self):
        self.__widevine_security_level = None
        self.__widevine_required_hdcp_version = None
        self.__widevine_required_cgms_flags = None
        self.__widevine_disable_analog_output = None
        self.__widevine_hdcp_srm_rule = None
        self.__widevine_override_device_revocation = None
        self.__widevine_enable_license_cipher = None

""" setter """

    def security_level(self, security_level: int):
        from pallycon.config.widevine.security_level import check
        if check(security_level):
            self.__widevine_security_level = security_level
        else:
            raise PallyConTokenException('1022')
        return self

    def required_hdcp_version(self, required_hdcp_version: str):
        from pallycon.config.widevine.required_hdcp_version import check
        if check(required_hdcp_version):
            self.__widevine_required_hdcp_version = required_hdcp_version
        else:
            raise PallyConTokenException('1023')
        return self

    def required_cgms_flags(self, required_cgms_flags: str):
        from pallycon.config.widevine.required_cgms_flags import check
        if check(required_cgms_flags):
            self.__widevine_required_cgms_flags = required_cgms_flags
        else:
            raise PallyConTokenException('1024')
        return self

    def disable_analog_output(self, disable_analog_output: bool):
        if isinstance(disable_analog_output, bool):
            self.__widevine_disable_analog_output = disable_analog_output
        else:
            raise PallyConTokenException('1025')
        return self

    def hdcp_srm_rule(self, hdcp_srm_rule: str):
        from pallycon.config.widevine.hdcp_srm_rule import check
        if check(hdcp_srm_rule):
            self.__widevine_hdcp_srm_rule = hdcp_srm_rule
        else:
            raise PallyConTokenException('1026')
        return self

    def override_device_revocation(self, override_device_revocation: bool):
        if isinstance(override_device_revocation, bool):
            self.__widevine_override_device_revocation = override_device_revocation
        else:
            raise PallyConTokenException('1051')
        return self

    def enable_license_cipher(self, enable_license_cipher: bool):
        if isinstance(enable_license_cipher, bool):
            self.__widevine_enable_license_cipher = enable_license_cipher
        else:
            raise PallyConTokenException('1054')
        return self

    """ getter """

    def get_security_level(self) -> int:
        return self.__widevine_security_level

    def get_required_hdcp_version(self) -> str:
        return self.__widevine_required_hdcp_version

    def get_required_cgms_flags(self) -> str:
        return self.__widevine_required_cgms_flags

    def get_disable_analog_output(self) -> bool:
        return self.__widevine_disable_analog_output

    def get_hdcp_srm_rule(self) -> str:
        return self.__widevine_hdcp_srm_rule

    def get_enable_license_cipher(self) -> bool:
        return self.__widevine_enable_license_cipher

    def dict(self):
        widevine = {}

        if self.__widevine_security_level is not None:
            widevine['security_level'] = self.__widevine_security_level
        if self.__widevine_required_hdcp_version is not None:
            widevine['required_hdcp_version'] = self.__widevine_required_hdcp_version
        if self.__widevine_required_cgms_flags is not None:
            widevine['required_cgms_flags'] = self.__widevine_required_cgms_flags
        if self.__widevine_disable_analog_output is not None:
            widevine['disable_analog_output'] = self.__widevine_disable_analog_output
        if self.__widevine_hdcp_srm_rule is not None:
            widevine['hdcp_srm_rule'] = self.__widevine_hdcp_srm_rule
        if self.__widevine_enable_license_cipher is not None:
            widevine['enable_license_cipher'] = self.__widevine_enable_license_cipher

        return widevine
