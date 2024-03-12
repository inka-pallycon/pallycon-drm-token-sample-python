RESPONSE_FORMAT = ('original', 'custom', 'json')

ORIGINAL = RESPONSE_FORMAT[0]
CUSTOM = RESPONSE_FORMAT[1]
JSON = RESPONSE_FORMAT[2]

def check(response_format):
    return response_format in RESPONSE_FORMAT

