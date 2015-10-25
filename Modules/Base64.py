#!/usr/bin/env python3
# -*- coding utf-8 -*-

__Author__ ='eamon'

'base64'

import base64

r=base64.b64encode(b'sff.this is a test string...')

print(r)

r=base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')

print(r)

r=base64.urlsafe_b64decode('abcd--__')

print(r)


def safe_base64_decode(s):
	last_empty= (-len(s))%4
	if last_empty != 0:
			s+=b'='*last_empty
	return base64.b64decode(s)

assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('Pass')

print('s'*4)

