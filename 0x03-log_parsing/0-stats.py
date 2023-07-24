#!/usr/bin/python3
"""log parsing module."""
import sys

tfs = 0
while True:
    nl = 0
    fsize = 0
    ld = {}
    try:
        while nl < 10:
            line = sys.stdin.readline()
            nl += 1
            if 'GET /projects' in line:
                fsize += int(line.split()[-1])
                stat = line.split()[-2]
                try:
                    stat = int(stat)
                    if stat in ld.keys():
                        ld[stat] += 1
                    else:
                        ld[stat] = 1
                except ValueError:
                    pass
        tfs += fsize
        print(f'File size: {tfs}')
        for a in sorted(ld):
            print(f'{a}: {ld[a]}')
    except KeyboardInterrupt:
        break
