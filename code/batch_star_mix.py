#!/usr/bin/env python
import os

#ms = list(range(103, 120+1))
ms = (107, 110, 113, 114, 118)

os.chdir(os.path.expandvars('$subsub/sf/'))

for m in ms:
    print(m)
    os.chdir("m{:03d}/output/mix_emcee/run02/".format(m))
    os.system('time $subsub/code/star_mix_beta.py --samples=5000 --incremental_save=100 > run.out')
    os.chdir(os.path.expandvars('$subsub/sf/'))
