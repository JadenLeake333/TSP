#Author: Jaden Leake
#Date: 2/23/2021
#Attempted solution to travelling salesman problem #

import sys
import json
import math
from draw import *

def calculate_distance(data):
    dist_dict = {}
    dist_dict['distances'] = []
    for i in range(data['num']-1):
        for j in range(len(data['edges'])):
            if i == data['edges'][j]['source']: # This assumes that the id is the same as the index which may not always be true
                target = data['edges'][j]['target']
                x,y = data['nodes'][i]['x'],data['nodes'][i]['y']
                x2,y2 = data['nodes'][target]['x'],data['nodes'][target]['y']
                distance = math.dist([x,y],[x2,y2])
                dist_dict['distances'].append({
                                                'source':i,
                                                'target':target,
                                                'distance':distance
                                             })
    return dist_dict

def solve_problem(start,end,data):
    #Start from 1
    #Find the shortest node from 1
    #Find the shortest from that node...#
    start_idx = 0
    for idx,i in enumerate(data['distances']):
        if i['source'] == start:
            start_idx = idx
            break

    min_dist = data['distances'][start_idx]['distance']
    index = data['distances'][start_idx]
    #print(min_dist)
    #print(index)
    new_target = 0
    for i in range(start_idx,len(data['distances'])):
        #if i > data['distances'][i]['source']:
        #    break

        if data['distances'][i]['distance'] < min_dist:
            min_dist = data['distances'][i]['distance']
            index = data['distances'][i]

    tsp['solution'].append(index)

if __name__ == "__main__":
    global tsp
    tsp = {}
    tsp['solution'] = []
    try:
        jsonfile = sys.argv[1]
        visualize = sys.argv[2]
    except:
        jsonfile = None
        print("Enter a .json file and bool value")
        quit(0)
    
    if jsonfile != None:
        try:
            with open (jsonfile) as file:
                data = json.load(file)
        except:
            print("Please enter a valid .json filename or make sure you have input a valid json")
            quit()
        distances = calculate_distance(data)
        solve_problem(5,data['num']-2,distances)
        print(tsp)
        if visualize == "True":
            initialize_board(data)
        
        
