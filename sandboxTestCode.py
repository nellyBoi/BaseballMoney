#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 18:28:48 2018

@author: johnnelsonkane

This script is just a sandbox for testing code

"""

from pybaseball import team_pitching

# getting all team listing names
dataFull = team_pitching(start_season=2010,\
                         end_season=2016,ind=0,league='all')

import baseballMetricsMod_v1