#!/usr/bin/python

import shutil
import json
import os

def addrepo(dist, debs):
    cmd = "reprepro -Vb repo --ignore=wrongdistribution includedeb "
    debs = ['deb/' + x for x in debs]
    cmd += dist + " " + " ".join(debs)

    os.system(cmd)

for entry in ['db', 'dists', 'pool']:
    try:
        shutil.rmtree('./repo/' + entry)
    except OSError:
        pass

with open('pkgs.json') as fp:
    debs = json.load(fp)

addrepo('cloudprint-jessie', debs['latest_stable'])
addrepo('cloudprint-stretch', debs['latest_pkgs'])

