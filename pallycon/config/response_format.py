RESPONSE_FORMAT = ('original', 'custom')

ORIGINAL = RESPONSE_FORMAT[0]
CUSTOM = RESPONSE_FORMAT[1]

def check(response_format):
    return response_format in RESPONSE_FORMAT

