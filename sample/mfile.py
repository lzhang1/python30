#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import shutil

sourcedir="/home/rayzhang/python30/sample"
destdir="/tmp/sample"

if os.path.isdir(destdir):
    pass
else:
    os.mkdir(destdir)

for file in os.listdir(sourcedir):
    if os.path.splitext(file)[1] == '.txt':
        print (file)
        shutil.copy(file, os.path.join(destdir,file))

