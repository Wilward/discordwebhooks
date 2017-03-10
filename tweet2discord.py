#!/usr/bin/env python

'''Post tweets to discord webhooks'''

__author__ = 'tero@hanninen.eu'

import configparser
import getopt
import os
import sys
import twitter


USAGE = '''Usage: tweet2discord

  This script fetches Twitter tweets and posts them to a Discord Webhook

  Options:
       The config options are stored in tweet2discord.conf file
'''

if __name__ == "__main__":
