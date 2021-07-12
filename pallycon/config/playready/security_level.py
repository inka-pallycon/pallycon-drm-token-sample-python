# for @security_policy @playready @security_level
SECURITY_LEVEL = (150, 2000, 3000)

LEVEL_150 = SECURITY_LEVEL[0]  # 'LEVEL_150',
LEVEL_2000 = SECURITY_LEVEL[1]  # 'LEVEL_2000'
LEVEL_3000 = SECURITY_LEVEL[2]  # 'LEVEL_3000'

def check(playready_security_level) -> bool:
    return playready_security_level in SECURITY_LEVEL
