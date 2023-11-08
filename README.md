# Drm-token-Sample-PYTHON





<br>

## Prerequisites

### Language

This works on `PYTHON` version : 

- 3.7.10 and greater

<br>

### IDE

- PyCharm
- Anaconda 4.8.2

<br>

### Libraries

For Anaconda users, create a virtual environment using `environment.yml` file and command.  

`environment.yml` file :     
```text
name: drm_token {{or, set environment name}}
channels:
  - defaults
dependencies:
  - ca-certificates=2021.5.25
  - certifi=2021.5.30
  - openssl=1.1.1k
  - pip=21.1.2
  - pycrypto=2.6.1
  - python=3.7.10
  - pytz=2021.1
  - setuptools=52.0.0
  - sqlite=3.35.4
  - vc=14.2
  - vs2015_runtime=14.27.29016
  - wheel=0.36.2
  - wincertstore=0.2
prefix: {{set anaconda env directory}}
``` 

command : 
```shell script
conda env create -f environment.yml
```
<br>

For other environments users, install packages using `requirements.txt`.   
```text
certifi==2021.5.30
pycrypto==2.6.1
pytz==2021.1
wincertstore==0.2
```

<br><br>

## Directories

| dir         |            | description                         |
| ----------- | ---------- | ----------------------------------- |
| pallycon    |            |                                     |
|             | /config    | configuration module for policy     |
|             | /exception | exception package                   |
|             | /sample    | make token sample @`client_test.py` |
|             | /token     | source directory                    |

<br>


## Guide
Go to [PallyCon Docs for Policy Json Specification](https://pallycon.com/docs/en/multidrm/license/license-token/#license-policy-json)
and figure out which specification to use.

### How to get token

0. make **quick** token : go to `pallycon/sample/amke_token.py` and run this module

1. Before get token, you need to set up `policy`.

   ```python
   from pallycon_drm_token_policy import PallyConDrmTokenPolicy as Policy
   
   policy = Policy()
   
   def set_policy():
       set_playback_policy()
       set_security_policy()
       set_external_key()
       
       policy \
           .playback(playback) \
           .security(security) \
           .external(external)
   ```

2. As you can see above, you need to decide whether to set `playback`, `security`, or `external`.

   If you want to set up all policies, 

   ```python
   from pallycon_drm_token_policy import PlaybackPolicy
   from pallycon_drm_token_policy import SecurityPolicy
   from pallycon_drm_token_policy import ExternalKey
   
   playback = PlaybackPolicy()
   security = SecurityPolicy()
   external = ExternalKey()
   
   
   def set_playback_policy():
       playback \
           .allowed_track_types(allowed_track_types.SD_ONLY) \
           .persistent(False)
           
   def set_security_policy():
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
   
   def set_external_key():
       """
       ### set mpeg_cecn | hls_aes | ncg
       """
       hls_aes_list = [
           HlsAes(track_type.SD,
                  '<key_id>',
                  '<key>'),
           HlsAes(track_type.HD,
                  '<key_id>',
                  '<key>'),
           HlsAes(track_type.UHD1,
                  '<key_id>',
                  '<key>'),
           HlsAes(track_type.UHD2,
                  '<key_id>',
                  '<key>')
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
   ```

3. Import `PallyConDrmTokenClient` from `pallycon_drm_token_client.py`

   ```python
   from pallycon_drm_token_client import PallyConDrmTokenClient as Token 
   from pallycon.config import response_format
   
   def set_drm_token():
       set_policy()
       token = Token()\
           .widevine()\
           .site_id("<Site ID>")\
           .site_key("<Site Key>")\
           .access_key("<Access Key>")\
           .user_id("tester-user")\
           .cid("<Content ID>")\
           .policy(policy)\
           .response_format(response_format.ORIGINAL)
       
       token.execute()
   ```

4. Make encrypted token !

   ```python
   try:
       set_drm_token()
   except PallyConTokenException as p:
       print(p)
   ```

   `PallyConTokenException` will arise if there are minor mistakes when created. The `result` will return JSON with an `error_code` and `error_message`. Follow the comment and fix the bugs. 

   For example, 
   
   ```json
   {
       "error_code": "1048",
       "error_message": "Token err : The response_format should be in type of RESPONSE_FORMAT in [pallycon.config.response_format] module"
   }
   ```
   
   If you want to see All the error codes and error messages you would get, see the `error_list` in `pallycon\excepion\pallycon_tokne_exception.py` module. 
   








We hope this instruction would be helpful to generate DRM License Token to request PallyCon Multi-DRM Cloud Server and get the License issued from.










### Error Messages

| Error Code | Error Messages                                               |
| ---------- | ------------------------------------------------------------ |
| 1000       | Token err : The userId is Required                           |
| 1001       | Token err : The cId is Required                              |
| 1002       | Token err : The siteId is Required                           |
| 1003       | Token err : The accessKey is Required                        |
| 1004       | Token err : The siteKey is Required                          |
| 1005       | Token err : The policy is Required                           |
| 1006       | Policy Err : The playback_policy should be an instance of PlaybackPolicy |
| 1007       | Policy Err : The security_policy should be an instance of SecurityPolicy or List[SecurityPolicy] |
| 1008       | Policy Err : The external_key should be an instance of ExternalKey |
| 1009       | PlaybackPolicy : The persistent should be Boolean            |
| 1010       | PlaybackPolicy : The license_duration should be Integer      |
| 1011       | PlaybackPolicy : The expireDate time format should be \'YYYY-MM-DD\'T\'HH:mm:ss\'Z\' |
| 1012       | PlaybackPolicy : The allowed_track_types value should be in allowed_track_types module |
| 1013       | SecurityPolicy: The track_type should be in type of  TRACK_TYPE<br />in `pallycon.config.track_type` module |
| 1014       | SecurityPolicy: The widevine should be an instance of SecurityPolicyWidevine |
| 1015       | SecurityPolicy: The playready should be an instance of SecurityPolicyPlayready |
| 1016       | SecurityPolicy: The fairplay should be an instance of SecurityPolicyFairplay |
| 1017       | SecurityPolicy: The ncg should be an instance of SecurityPolicyNcg |
| 1018       | ExternalKey: The ExternalKey Should be filled if called      |
| 1019       | ExternalKey: The MpegCenc should be an instance of MpegCenc or List[MpegCenc] |
| 1020       | ExternalKey: The HlsAes should be an instance of HlsAes or List[HlsAes] |
| 1021       | ExternalKey: The Ncg should be an instance of Ncg            |
| 1022       | SecurityPolicyWidevine: The security_level should be in type of  SECURITY_LEVEL<br />in `pallycon.config.widevine.security_level` module |
| 1023       | SecurityPolicyWidevine: The required_hdcp_version should be in type of  REQUIRED_HDCP_VERSION<br />in `pallycon.config.widevine.required_hdcp_version` module |
| 1024       | SecurityPolicyWidevine: The required_cgms_flagsshould be in type of  REQUIRED_CGMS_FLAGS<br />in `pallycon.config.widevine.required_cgms_flags` module |
| 1025       | SecurityPolicyWidevine: The disable_analog_output should be Boolean |
| 1026       | SecurityPolicyWidevine: The hdcp_srm_rule should be in type of  HDCP_SRM_RULE<br />in `pallycon.config.widevine.hdcp_srm_rule` module |
| 1027       | SecurityPolicyPlayready: The security_level should be in type of  SECURITY_LEVEL<br />in `pallycon.config.playready.security_level` module |
| 1028       | SecurityPolicyPlayready: The digital_video_protection_level should be in type of  DIGITAL_VIDEO_PROTECTION_LEVEL<br />in `pallycon.config.playready.digital_video_protection` module |
| 1029       | SecurityPolicyPlayready: The analog_video_protection_level should be in type of  ANALOG_VIDEO_PROTECTION_LEVEL<br />in `pallycon.config.playready.analog_video_protection` module |
| 1030       | SecurityPolicyPlayready: The digital_audio_protection_level should be in type of  DIGITAL_AUDIO_PROTECTION<br />in `pallycon.config.playready.digital_audio_protection` module |
| 1032       | SecurityPolicyPlayready: The require_hdcp_type_1 should be Boolean |
| 1033       | SecurityPolicyFairplay: The hdcp_enforcement should be in type of FAIRPLAY_HDCP_ENFORCEMENT<br />in `pallycon.config.fairplay_hdcp_enforcement` module |
| 1034       | SecurityPolicyFairplay: The allow_airplay should be Boolean  |
| 1035       | SecurityPolicyFairplay: The allow_av_adapter should be Boolean |
| 1036       | SecurityPolicyNcg: The allow_mobile_abnormal_device should be Boolean |
| 1037       | SecurityPolicyNcg: The allow_external_display should be Boolean |
| 1038       | SecurityPolicyNcg: The control_hdcp should be in type of CONTROL_HDCP<br />in `pallycon.config.ncg_control_hdcp` module |
| 1039       | ExternalKeyMpegCenc: The track_type should be in type of  TRACK_TYPE<br />in `pallycon.config.track_type` module |
| 1040       | ExternalKeyMpegCenc : The key_id should be 16byte hex String |
| 1041       | ExternalKeyMpegCenc : The key should be 16byte hex String    |
| 1042       | ExternalKeyMpegCenc : The iv should be 16byte hex String     |
| 1043       | ExternalKeyHlsAes: The track_type should be in type of  TRACK_TYPE<br />in `pallycon.config.track_type` module |
| 1044       | ExternalKeyHlsAes : The key should be 16byte hex String      |
| 1045       | ExternalKeyHlsAes : The iv should be 16byte hex String       |
| 1046       | ExternalKeyNcg : The track_type should be in type of  TRACK_TYPE<br />in `pallycon.config.track_type` module |
| 1047       | ExternalKeyNcg : The Cek should be 32byte hex String         |
| 1048       | Token err : The response_format should be in type of RESPONSE_FORMAT<br />in `pallycon.config.response_format` module |
| 1049       | PlaybackPolicy : The rental_duration should be Integer |
| 1050       | PlaybackPolicy : The playback_duration should be Integer |
| 1051       | SecurityPolicyWidevine: The override_device_revocation should be Boolean |
| 1052       | ExternalKeyHlsAes : The key_id should be 16byte hex String |
| 1053       | PlaybackPolicy : The max_stream_per_user should be Integer |
| 1054       | SecurityPolicyWidevine : The enable_license_cipher should be Boolean |








