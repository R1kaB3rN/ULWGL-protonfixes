"""Game fix for Assassin's Creed Odyssey"""
# pylint: disable=C0103

from protonfixes import util

def main():
    # Disable UPlay overlay and change CloseBehavior
    util.disable_uplay_overlay()
