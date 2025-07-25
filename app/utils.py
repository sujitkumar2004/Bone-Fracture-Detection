# import string
# import random
# from urllib.parse import urlparse

# def generate_short_code(length=6):
#     return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# def is_valid_url(url):
#     parsed = urlparse(url)
#     return all([parsed.scheme, parsed.netloc])
# app/utils.py

import string
import random
import re

def generate_short_code(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))

def is_valid_url(url):
    pattern = re.compile(
        r'^(http|https)://'
        r'([\w.-]+)+(:\d+)?(/([\w/_.]*)?)?$'
    )
    return re.match(pattern, url) is not None
