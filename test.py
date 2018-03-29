# -*- coding :utf-8 -*-
#/ur/bin/python
# _uthor=liuong time=2018/3/29

a = '0x9'
if len(a) == 3:
    a = '0x0' + a[2]
print(a)