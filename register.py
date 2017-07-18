# -*- coding: utf-8 -*-
# @Author: gess
# @Date:   2017-07-18 15:37:50
# @Last Modified by:   gess
# @Last Modified time: 2017-07-18 16:05:50

import pandoc
import os

# pandoc.core.PANDOC_PATH = '/path/to/pandoc'

doc = pandoc.Document()
doc.markdown = open('README.md').read()
f = open('README.rst','w')
f.write(doc.rst)
f.close()
# os.system("setup.py register")
# os.remove('README.txt')