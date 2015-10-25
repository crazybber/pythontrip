#!/usr/bin/env python3
# -*- coding utf-8 -*-

__Author__ ='eamon'

'struct'

# n=10240099
# b1 = n & 0xff000000 >> 24
# b2 = n & 0xff0000 >> 16
# b3 = n & 0xff00 >> 8
# b4 = n & 0xff

# b5= bytes([b1,b2,b3,b4])

# print(b5)

import struct

r=struct.pack('>I',10240099)
print(r)

# r=struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')

# print(r)