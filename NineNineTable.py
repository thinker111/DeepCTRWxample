#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:yxc  time:2022/4/25

for i in range(1,10):
    for j in range(1,i+1):
        print("{}x{}={}\t".format(i,j,i*j),end="")
    print()
print("finished")