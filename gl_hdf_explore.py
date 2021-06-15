# -*- coding: utf-8 -*-
# Script to explore available metadata
# Copyright (c) [2021] Godwin Liu

from argparse import ArgumentParser
from os.path import join, exists
import h5py
import sys


if __name__ == '__main__':

    # Subject ids
    sids = ['50002', '50004', '50007', '50009', '50020',
            '50021', '50022', '50025', '50026', '50027']
    # Sequences available for each subject id are listed in scripts/subjects_and_sequences.txt

    parser = ArgumentParser(description='Explore available metadata content')
    parser.add_argument('--path', type=str, default='registrations_f.hdf5',
                        help='dataset path in hdf5 format')
    parser.add_argument('--seq', type=str, default='jiggle_on_toes',
                        help='sequence name')                         
    parser.add_argument('--sid', type=str, default='50004', choices=sids,
                        help='subject id')
    args = parser.parse_args()

    sidseq = args.sid + '_' + args.seq
    print('Looking in: \'' + args.path + '\'')
    print('\n\t..' + sidseq)
    
    with h5py.File(args.path, 'r') as f:

        print('\nKeys in HDF5 datafile:\n')
        print(f.keys())

        i = 0
        for k in f.keys():
            dset = f[k]
            print('\nKey:\t' + str(k))
            print('\tDataset:\tShape: ' + str(dset.shape) + '\tType: ' + str(dset.dtype))
            i += 1

        print('\nTotal Data Sets in File: ' + str(i))


