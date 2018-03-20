#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 20:47:13 2018

@author: johnnelsonkane

baseballMetricsMod_v1.py

This script will contain the metrics developed to analyze baseball teams. This
first version will contain metrics that are called once per single team.

+++ METRICS +++

awayWinsMinusHomeLosses: The away wins minus the home losses in the provided 
    season. 
    
winMargin: For all of the winning games the average of Runs (R) - 
    Runs Against(RA). Note that loss margins are not included in this metric.
    

NOTE:  - metrics still need to be validated
    
"""
from numpy import mean

def awayWinsMinusHomeLosses(teamData):
    
    # file header names
    inDataColNames = list(teamData.columns.values)
    
    # raise error if necessary header names are not in input DataFrame
    if not (('Home_Away' in inDataColNames) and ('W/L' in inDataColNames)):
        print(('Missing necessary header in awayWinsMinsHomeLosses metric'))
        return
    
    # grab indices of headers 
    Home_Away_idx = inDataColNames.index('Home_Away')
    W_L_idx = inDataColNames.index('W/L')
    
    # Home and away indices
    HomeAway_vec = teamData.iloc[:,Home_Away_idx]
    awayIdx = HomeAway_vec == '@'
    homeIdx = HomeAway_vec == 'Home' 
    
    # Wins and losses indices
    WinsLosses_vec = teamData.iloc[:,W_L_idx]
    winIdx = WinsLosses_vec == 'W'
    lossIdx = WinsLosses_vec == 'L'
    
    # Calculating away wins minus home losses
    metricVal = (sum(awayIdx & winIdx) - sum(homeIdx & lossIdx))
    
    return metricVal

def winMargin(teamData):
    
    # file header names
    inDataColNames = list(teamData.columns.values)
    
    # raise error if necessary header names are not in input DataFrame
    if not ((('W/L' in inDataColNames) and ('R' in inDataColNames)) and \
            ('RA' in inDataColNames)):
        print(('Missing necessary header in awayWinsMinsHomeLosses metric'))
        return
    
    W_L_idx = inDataColNames.index('W/L')
    R_idx = inDataColNames.index('R')
    RA_idx = inDataColNames.index('RA')
    
    WL_vec = teamData.iloc[:,W_L_idx]
    R_vec = teamData.iloc[:,R_idx]
    RA_vec = teamData.iloc[:,RA_idx]
    
    # game win boolean
    win_bool = WL_vec == 'W'
    
    # R_vec, RA_vec that is only non-zero for game wins (losses play no effect)
    R_vec_winBool = R_vec.iloc[[i for i, x in enumerate(win_bool) if x]]
    RA_vec_winBool = RA_vec.iloc[[i for i, x in enumerate(win_bool) if x]]
    
    metricVal = mean(R_vec_winBool - RA_vec_winBool)
            
    return metricVal