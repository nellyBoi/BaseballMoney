#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 18:18:44 2018

@author: johnnelsonkane

createMetricsArray_wrapper.py

This script will be the outer-most wrapper for testing the module 
'metricsModule' and the metrics within it. It can later be replaced by an 
actual routine, or a higher-level GUI that will simply display the data/metrics 
we wish to see.

IN: 
    - year/season
    - teamList : list of teams, this should remain a constant parameter, 
      given that we will always want info on every team.
    - metrics for array: name of metrics that we wish to have. The metrics must
      exist in the module 'metricsModule.py'. If a metric is called that is not
      in the metrics module than code will raise an error.
      
OUT:
    - metricsArray: A panda.DataSeries array, where rows represent teams. First
      column will have team name, all proceeding columns will be metrics, 
      labeled by the metric name


NOTES: Can use the pickle library to save the final data frame, if needed, 
    for load into the model.
    
+++ TEAMS +++
ARI: Arizona Diamondbacks
ATL: Atlanta Braves
BAL: Baltimore Orioles
BOS: Boston Red Sox 
CHC: hicago Cubs
CHW or CWS: Chicago White Sox 
CIN: Cincinnati Reds
CLE: Cleveland Indians 
COL: Colorado Rockies 
DET: Detroit Tigers 
FLA: Florida Marlins
HOU: Houston Astros
KAN: Kansas City Royals
LAA: Los Angeles Angels of Anaheim
LAD: Los Angeles Dodgers 
MIL: Milwaukee Brewers 
MIN: Minnesota Twins 
NYM: New York Mets 
NYY: New York Yankees 
OAK: Oakland Athletics 
PHI: Philadelphia Phillies 
PIT: Pittsburgh Pirates 
SD: San Diego Padres 
SF: San Francisco Giants 
SEA: Seattle Mariners 
STL: St. Louis Cardinals 
TB: Tampa Bay Rays 
TEX: Texas Rangers 
TOR: Toronto Blue Jays 
WAS: Washington Nationals

"""

from pandas import DataFrame as df
from teamMetrics import getTeamMetrics
import inspect
# name of baseball metrics module
metricsModule = 'baseballMetricsMod_v1'

year = 2015
metrics = ['awayWinsMinusHomeLosses','winMargin']

# original
'''teamList = ['ARI','ATL','BAL','BOS','CHC','CHW','CIN','CLE','COL','DET','FLA',\
'HOU','KAN','LAA','LAD','MIL','MIN','NYM','NYY','OAK','PHI','PIT','SD','SF',\
'SEA','STL','TB','TEX','TOR','WAS']'''

# bad abbreviations removed (FLA, KAN, WAS)
teamList = ['ARI','ATL','BAL','BOS','CHC','CHW','CIN','CLE','COL','DET',\
'HOU','LAA','LAD','MIL','MIN','NYM','NYY','OAK','PHI','PIT','SD','SF',\
'SEA','STL','TB','TEX','TOR']


'''+++++++++++ End of definitions, beginning of code +++++++++++++++++++++++'''
metMod = __import__(metricsModule)



allModRoutines = inspect.getmembers(metMod, inspect.isfunction)
    
for metric in metrics:
        
    # check if metric is in list of metrics, if so calculate metric, if not, 
    # remove metric from list before building DataFrame
    routineAvail = metric in dict(allModRoutines)
    
    if routineAvail == 1:
        print('routine is available')
    else:
        print('The metric ' + metric + ' is not available in the module')
        
        # remove metric from list for DataFrame
        metricIdx = metrics.index(metric)
        metrics.pop(metricIdx)
        
        continue

# building data frame
colNames = metrics.copy()
colNames.reverse()
colNames.append('Team Abv.')
colNames.reverse()
metricsArray = df(columns = colNames)

# appending column names with team names
metricsArray.iloc[:,0] = teamList

# loop through team symbols to get metricsArray
for team in teamList:
    
    teamIdx = teamList.index(team)
    
    metricForArray = getTeamMetrics(team, year, metrics, metMod)
    
    metricsArray.iloc[teamIdx,1:] = metricForArray
    