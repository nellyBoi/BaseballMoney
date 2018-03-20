#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 19:20:47 2018

@author: johnnelsonkane

This module will have three routines:
    grabTeamData: grab data for a specified team
    calcMetrics: calculate metrics for a given team
    getTeamMetrics: will combine the first two

"""

from pybaseball import schedule_and_record

'''-------------------------------------------------------------------------'''


def grabTeamData(team, year):
    
    teamData = schedule_and_record(year, team)
    
    return teamData


def calcMetrics(teamData, metricsList,metMod):
    
    # temp
    metricsForArray = []
    
    
    for metric in metricsList:
            
        # calculate metric (routine must be executed by variable name)
        fcn = getattr(metMod, metric, None)
        metricForArray = fcn(teamData)
        metricsForArray.append(metricForArray)

    
    return metricsForArray

def getTeamMetrics(team, year, metricsList, metMod):
    
    teamData = grabTeamData(team, year)
    
    metricForArray = calcMetrics(teamData, metricsList, metMod)
    
    return metricForArray


    
