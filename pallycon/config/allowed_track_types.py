ALLOWED_TRACK_TYPES = ('ALL', 'SD_ONLY', 'SD_HD', 'SD_UHD1', 'SD_UHD2')

#: Type of the allowed_track_types
ALL = ALLOWED_TRACK_TYPES[0]
SD_ONLY = ALLOWED_TRACK_TYPES[1]
SD_HD = ALLOWED_TRACK_TYPES[2]
SD_UHD1 = ALLOWED_TRACK_TYPES[3]
SD_UHD2 = ALLOWED_TRACK_TYPES[4]


def check(allowed_track_types):
    return allowed_track_types in ALLOWED_TRACK_TYPES
