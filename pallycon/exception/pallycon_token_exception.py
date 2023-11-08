import json

"""
Error Code List
"""
error_list = [
    ('1000', 'Token err : The userId is Required'),
    ('1001', 'Token err : The cId is Required'),
    ('1002', 'Token err : The siteId is Required'),
    ('1003', 'Token err : The accessKey is Required'),
    ('1004', 'Token err : The siteKey is Required'),
    ('1005', 'Token err : The policy is Required'),

    ('1006', 'Policy Err : The playback_policy should be an instance of PlaybackPolicy'),
    ('1007', 'Policy Err : The security_policy should be an instance of SecurityPolicy or List[SecurityPolicy]'),
    ('1008', 'Policy Err : The external_key should be an instance of ExternalKey'),

    ('1009', 'PlaybackPolicy : The persistent should be Boolean'),
    ('1010', 'PlaybackPolicy : The license_duration should be Integer'),
    ('1011', 'PlaybackPolicy : The expireDate time format should be \'YYYY-MM-DD\'T\'HH:mm:ss\'Z\''),
    ('1012', 'PlaybackPolicy : The allowed_track_types value should be in allowed_track_types module'),

    ('1013', 'SecurityPolicy : The track_type should be in type of TRACK_TYPE '
             'in [pallycon.config.track_type] module'),
    ('1014', 'SecurityPolicy : The widevine should be an instance of SecurityPolicyWidevine'),
    ('1015', 'SecurityPolicy : The playready should be an instance of SecurityPolicyPlayready'),
    ('1016', 'SecurityPolicy : The fairplay should be an instance of SecurityPolicyFairplay'),
    ('1017', 'SecurityPolicy : The ncg should be an instance of SecurityPolicyNcg'),

    ('1018', 'ExternalKey: The ExternalKey Should be filled if called'),
    ('1019', 'ExternalKey: The MpegCenc should be an instance of MpegCenc or List[MpegCenc]'),
    ('1020', 'ExternalKey: The HlsAes should be an instance of HlsAes or List[HlsAes]'),
    ('1021', 'ExternalKey: The Ncg should be an instance of Ncg'),

    ('1022', 'SecurityPolicyWidevine: The security_level should be in type of SECURITY_LEVEL '
             'in [pallycon.config.widevine.security_level] module'),
    ('1023', 'SecurityPolicyWidevine: The required_hdcp_version should be in type of REQUIRED_HDCP_VERSION '
             'in [pallycon.config.widevine.required_hdcp_version] module'),
    ('1024', 'SecurityPolicyWidevine: The required_cgms_flags should be in type of REQUIRED_CGMS_FLAGS '
             'in [pallycon.config.widevine.security_level] module'),
    ('1025', 'SecurityPolicyWidevine: The disable_analog_output should be Boolean'),
    ('1026', 'SecurityPolicyWidevine: The hdcp_srm_rule should be in type of HDCP_SRM_RULE '
             'in [pallycon.config.widevine.hdcp_srm_rule] module'),

    ('1027', 'SecurityPolicyPlayready: The security_level should be in type of SECURITY_LEVEL '
             'in [pallycon.config.playready.security_level] module'),
    ('1028', 'SecurityPolicyPlayready: The digital_video_protection_level should be '
             'in type of DIGITAL_VIDEO_PROTECTION_LEVEL '
             'in [pallycon.config.playready.digital_video_protection] module'),
    ('1029', 'SecurityPolicyPlayready: The analog_video_protection_level should be '
             'in type of ANALOG_VIDEO_PROTECTION_LEVEL '
             'in [pallycon.config.playready.analog_video_protection] module'),
    ('1030', 'SecurityPolicyPlayready: The digital_audio_protection_level should be '
             'in type of DIGITAL_AUDIO_PROTECTION '
             'in [pallycon.config.playready.digital_audio_protection] module'),
    ('1032', 'SecurityPolicyPlayready: The require_hdcp_type_1 should be Boolean'),
    ('1033', 'SecurityPolicyFairplay: The hdcp_enforcement should be in type of FAIRPLAY_HDCP_ENFORCEMENT '
             'in [pallycon.config.fairplay_hdcp_enforcement] module'),
    ('1034', 'SecurityPolicyFairplay: The allow_airplay should be Boolean'),
    ('1035', 'SecurityPolicyFairplay: The allow_av_adapter should be Boolean'),
    ('1036', 'SecurityPolicyNcg: The allow_mobile_abnormal_device should be Boolean'),
    ('1037', 'SecurityPolicyNcg: The allow_external_display should be Boolean'),
    ('1038', 'SecurityPolicyNcg: The control_hdcp should be in type of CONTROL_HDCP '
             'in [pallycon.config.ncg_control_hdcp] module'),
    ('1039', 'ExternalKeyMpegCenc: The track_type should be in type of TRACK_TYPE '
             'in [pallycon.config.track_type] module'),
    ('1040', 'ExternalKeyMpegCenc : The key_id should be 16byte hex String'),
    ('1041', 'ExternalKeyMpegCenc : The key should be 16byte hex String'),
    ('1042', 'ExternalKeyMpegCenc : The iv should be 16byte hex String'),
    ('1043', 'ExternalKeyHlsAes: The track_type should be in type of TRACK_TYPE '
             'in [pallycon.config.track_type] module'),
    ('1044', 'ExternalKeyHlsAes : The key should be 16byte hex String'),
    ('1045', 'ExternalKeyHlsAes : The iv should be 16byte hex String'),
    ('1046', 'ExternalKeyNcg : The track_type should be in type of TRACK_TYPE '
             'in [pallycon.config.track_type] module'),
    ('1047', 'ExternalKeyNcg : The Cek should be 32byte hex String'),
    ('1048', 'Token err : The response_format should be in type of RESPONSE_FORMAT '
             'in [pallycon.config.response_format] module'),
    ('1049', 'PlaybackPolicy : The rental_duration should be Integer'),
    ('1050', 'PlaybackPolicy : The playback_duration should be Integer'),
    ('1051', 'SecurityPolicyWidevine: The override_device_revocation should be Boolean'),
    ('1052', 'ExternalKeyHlsAes : The key_id should be 16byte hex String'),
    ('1053', 'PlaybackPolicy : The max_stream_per_user should be Integer'),
    ('1054', 'SecurityPolicyWidevine : The enable_license_cipher should be Boolean'),

]
error_dict = dict(error_list)

class PallyConTokenException(Exception):

    def __init__(self, code='0000'):
        self.__code = code
        if code is not '0000':
            self.__message = error_dict[code]
        else:
            self.__message = 'success'

    def __str__(self):
        json_str = {
            'error_code': self.__code,
            'error_message': self.__message
        }
        return 'YOU\'VE GOT THE ERROR ||||| ' + json.dumps(json_str)
