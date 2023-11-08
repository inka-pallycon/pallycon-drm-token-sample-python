import logging
import json
from pallycon.token.pallycon_drm_token_client import PallyConDrmTokenClient as Token
from pallycon.token.pallycon_drm_token_policy import PallyConDrmTokenPolicy as Policy
from pallycon.token.pallycon_drm_token_policy import PlaybackPolicy
from pallycon.token.pallycon_drm_token_policy import SecurityPolicy
from pallycon.token.pallycon_drm_token_policy import ExternalKey
from pallycon.exception.pallycon_token_exception import PallyConTokenException

"""
### set log ###
"""
logger = logging.getLogger('TEST_LOG')
logger.setLevel(logging.DEBUG)

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)

logger.addHandler(consoleHandler)

formatter = logging.Formatter('%(asctime)s  %(name)s  %(levelname)s: %(message)s')
consoleHandler.setFormatter(formatter)

"""
### set variables ###
"""
playback = PlaybackPolicy()
security = SecurityPolicy()
external = ExternalKey()
policy = Policy()

"""
makes make token you want
after set up all variables and policy through set_policy() etc,
you can now call this function set_drm_token()

if there are some mistakes when created, 
you can get the error codes and the messages we offer through 'PallyConTokenException'
"""


def set_drm_token():
    from pallycon.config import response_format

    set_policy()
    token = Token() \
        .widevine() \
        .site_id("<Site ID>") \
        .site_key("<Site Key>") \
        .access_key("<Access Key>") \
        .user_id("tester-user") \
        .cid("<Content ID>") \
        .policy(policy) \
        .response_format(response_format.ORIGINAL)

    logger.info(":::::: TOKEN ::::::\n" + token.execute())
    logger.debug(':::::: BEFORE ENCRYPT TOKEN ::::::' + token.to_json_str())


def set_policy():
    """
    set up policies
    if you want to set up
        @playback_policy: use the function set_playback_policy()
        @security_policy: use the function set_security_policy()
        @external_key:    use the function set_external_key()
    """
    set_playback_policy()
    set_security_policy()
    set_external_key()

    policy \
        .playback(playback) \
        .security(security) \
        .external(external)

    logger.debug('policy set:\t' + policy.to_json_str())


def set_playback_policy():
    from pallycon.config import allowed_track_types

    playback \
        .allowed_track_types(allowed_track_types.SD_HD) \
        .persistent(False)

    logger.debug('playback set:\t' + json.dumps(playback.dict()))


def set_security_policy():
    """
    ### set Widevine | Playready | Fairplay | Ncg
        `Version 1 and 2` have only one difference in how to set.
        choose version you prefer.
    """

    # version 1.
    from pallycon.config import track_type
    from pallycon.token.v2.security_policy_widevine import SecurityPolicyWidevine as Widevine
    from pallycon.token.v2.security_policy_playready import SecurityPolicyPlayready as Playready
    from pallycon.token.v2.security_policy_fairplay import SecurityPolicyFairplay as Fairplay
    from pallycon.token.v2.security_policy_ncg import SecurityPolicyNcg as Ncg

    security.track_type(track_type.ALL) \
        .widevine(Widevine()
                  .security_level(1)
                  .required_hdcp_version('HDCP_NONE')
                  .required_cgms_flags('CGMS_NONE')
                  .override_device_revocation(False)) \
        .playready(Playready()
                   .security_level(150)
                   .digital_video_protection_level(100)
                   .analog_video_protection_level(100)
                   .digital_audio_protection_level(100)
                   ) \
        .fairplay(Fairplay()
                  .hdcp_enforcement(-1)
                  .allow_airplay(True)
                  .allow_av_adapter(True)) \
        .ncg(Ncg()
             .allow_mobile_abnormal_device(True)
             .allow_external_display(True)
             .control_hdcp(0))

    # version 2.
    """
    from pallycon.config.playready import security_level as p_security_level, digital_video_protection, \
        analog_video_protection, digital_audio_protection
    from pallycon.config.widevine import security_level, required_hdcp_version, required_cgms_flags
    from pallycon.config import fairplay_hdcp_enforcement, ncg_control_hdcp

    security.track_type(track_type.ALL) \
        .widevine(Widevine()
                  .security_level(security_level.SW_SECURE_CRYPTO)
                  .required_hdcp_version(required_hdcp_version.HDCP_NONE)
                  .required_cgms_flags(required_cgms_flags.CGMS_NONE)
                  .override_device_revocation(False)
                  .enable_license_cipher(False) \
        .playready(Playready()
                   .security_level(p_security_level.LEVEL_150)
                   .digital_video_protection_level(digital_video_protection.LEVEL_100)
                   .analog_video_protection_level(analog_video_protection.LEVEL_100)
                   .digital_audio_protection_level(digital_audio_protection.LEVEL_100)) \
        .fairplay(Fairplay()
                  .hdcp_enforcement(fairplay_hdcp_enforcement.HDCP_NONE)
                  .allow_airplay(True)
                  .allow_av_adapter(True)) \
        .ncg(Ncg()
             .allow_mobile_abnormal_device(False)
             .allow_external_display(True)
             .control_hdcp(ncg_control_hdcp.HDCP_NONE))
     """

    logger.debug('security set:\t' + json.dumps(security.dict()))


def set_external_key():
    """
    ### set mpeg_cenc | hls_aes | ncg
    """
    from pallycon.token.v2.external_key_mpeg_cenc import ExternalKeyMpegCenc as MpegCenc
    from pallycon.token.v2.external_key_hls_aes import ExternalKeyHlsAes as HlsAes
    from pallycon.token.v2.external_key_ncg import ExternalKeyNcg as Ncg
    from pallycon.config import track_type

    hls_aes_list = [
        HlsAes(track_type.SD,
               '<key_id>',
               '<key>',
               "<iv>"),
        HlsAes(track_type.HD,
               '<key_id>',
               '<key>',
               "<iv>"),
        HlsAes(track_type.UHD1,
               '<key_id>',
               '<key>',
               "<iv>"),
        HlsAes(track_type.UHD2,
               '<key_id>',
               '<key>',
               "<iv>"),
    ]

    external \
        .mpeg_cenc(MpegCenc(track_type.HD,
                            '<key_id>',
                            '<key>',
                            '<iv>')) \
        .mpeg_cenc(MpegCenc(track_type.UHD1,
                            '<key_id>',
                            '<key>',
                            '<iv>')) \
        .mpeg_cenc(MpegCenc(track_type.UHD2,
                            '<key_id>',
                            '<key>',
                            '<iv>')) \
        .hls_aes(hls_aes_list) \
        .ncg(Ncg(track_type.ALL_VIDEO,
                 '<cek>'))

    logger.debug('external set\t' + json.dumps(external.dict()))


try:
    set_drm_token()
except PallyConTokenException as p:
    print(p)
