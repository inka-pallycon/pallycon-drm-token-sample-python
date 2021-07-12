"""
 for security_policy @ track_type
"""
TRACK_TYPE = ('ALL', 'ALL_VIDEO', 'AUDIO', 'SD',
              'HD', 'UHD1', 'UHD2')

ALL = TRACK_TYPE[0]
ALL_VIDEO = TRACK_TYPE[1]
AUDIO = TRACK_TYPE[2]
SD = TRACK_TYPE[3]
HD = TRACK_TYPE[4]
UHD1 = TRACK_TYPE[5]
UHD2 = TRACK_TYPE[6]

def check(types) -> bool:
    return types in TRACK_TYPE
