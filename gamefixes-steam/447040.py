"""Game fix for Watch_Dogs 2"""
# pylint: disable=C0103

from protonfixes import util

def main():
    # Disable UPlay overlay and change CloseBehavior
    util.disable_uplay_overlay()
    # Disable Easy Anti-Cheat and online play; replace launcher with game's EXE in Proton arguments
    util.append_argument("-eac_launcher -nosplash")
