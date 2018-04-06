#!/usr/bin/env python
import os
import yaml
import numpy as np
import h5py

#ms = list(range(98, 115)) + list(range(116, 125+1))
ms = [114]

os.chdir(os.path.expandvars('$subsub/sf/'))

for m in ms:

    dat_name = os.path.expandvars('$subsub/data/reduced/subsub_IGRINS_m{:03d}.hdf5'.format(m))
    path_out = 'm{:03d}/'.format(m)
    sf_out = 'm{:03d}/config.yaml'.format(m)

    f = open("m115/config.yaml")
    config = yaml.load(f)
    f.close()

    f=h5py.File(dat_name, "r")
    wls = f['wls'][:]
    f.close()

    config['data']['files'] = ['$subsub/data/reduced/subsub_IGRINS_m{:03d}.hdf5'.format(m)]
    config['grid']['hdf5_path'] = '$subsub/sf/m{:03d}/libraries/PHOENIX_IGRINS_m{:03d}.hdf5'.format(m, m)
    lb, ub = int(np.floor(wls[0])), int(np.ceil(wls[-1]))

    config['grid']['wl_range'] = [lb-1, ub+1]
    config['PCA']['path'] = '$subsub/sf/m{:03d}/PHOENIX_IGRINS_H_PCA_Teff3000-5300.hdf5'.format(m)
    config['data']['instruments'] =['IGRINS_H']
    config['Theta_priors']= '$subsub/sf/m{:03d}/user_prior.py'.format(m)

    os.makedirs(path_out, exist_ok=True)
    with open(sf_out, mode='w') as outfile:
        outfile.write(yaml.dump(config))
        print('wrote to {}'.format(path_out))

#for m in ms:
#    os.chdir("m{:03d}".format(m))
#    os.system('mkdir libraries &')
#    os.system('$Starfish/scripts/grid.py --create > grid.out &')
#    os.chdir("..")