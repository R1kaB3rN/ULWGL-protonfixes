""" Gobliiins 5
Setup doesn't work and language is default to french
"""
#pylint: disable=C0103

from protonfixes import util
import os
import sys
import subprocess
import glob

def main():
    if (sys.argv[2].find("winsetup")!=-1): os.chdir(sys.argv[2][-29:-13])
    install_dir = glob.escape(util.get_game_install_path())
    with open(os.path.join(install_dir,'Gobliiins5-Part4/acsetup.cfg'), 'r') as f:
        if 'Linear' not in f.read():
            for i in range(1,5):
                subprocess.call(["sed -i 's/filter=stdscale/filter=Linear/' {}{}{}{}".format(install_dir,'/Gobliiins5-Part',i,'/acsetup.cfg')], shell=True)
                subprocess.call(["sed -i 's/translation.*/translation=English/' {}{}{}{}".format(install_dir,'/Gobliiins5-Part',i,'/acsetup.cfg')], shell=True)
