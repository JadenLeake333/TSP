#Author: Jaden Leake
#Date: 2/23/2021
#Attempted solution to travelling salesman problem #

import sys
import json
import math
from draw import *
import itertools

def calculate_distance(data):
    dist_dict = {}
    dist_dict['distances'] = []
    for i in range(data['num']):
        #dist_dict['distances'].append({'source':[]})
        for j in range(len(data['edges'])):
            if i == data['edges'][j]['source']: # This assumes that the id is the same as the index which may not always be true
                target = data['edges'][j]['target']
                x,y = data['nodes'][i]['x'],data['nodes'][i]['y']
                x2,y2 = data['nodes'][target]['x'],data['nodes'][target]['y']
                distance = math.dist([x,y],[x2,y2])
                dist_dict['distances'].append({
                                                'source':i,
                                                'target':target,
                                                'distance':distance,
                                                'flag': 1
                                             })
    print(dist_dict)
    return dist_dict

'''
# Here I wanted to attempt solving the problem recursivly 
def solve_problem(start,end,data):
    #Start from x
    #Find the shortest node from x
    #Find the shortest from that node...#
    start_idx = 0
    if start == end+1: #When we are at the limit, we need to find which node it is closest too
        pass
        
    for idx,i in enumerate(data['distances']):
        if i['source'] == start:
            start_idx = idx
            break

    print(start_idx)
    min_dist = data['distances'][start_idx]['distance']
    index = data['distances'][start_idx]
    #print(min_dist)
    #print(index)

    for i in range(start_idx,len(data['distances'])):
        data['distance'][i]['flag'] = 0
        if start != data['distances'][i]['source']:
            break

        if data['distances'][i]['distance'] < min_dist:
            min_dist = data['distances'][i]['distance']
            index = data['distances'][i]

    print(data)
    tsp['solution'].append(index)
    if len(tsp['solution']) >= end:
        return
    else:
        solve_problem(index['target'],end,data)
'''
'''
def solve_problem(data,length):
    permutations = [p for p in itertools.product(range(0,length),repeat=length)]
    distances = {}
    distances['sums'] = []
    used_idx = []
    # Is not accounting for everything that has been counted
    first_sum = 0
    count = 0 #
    for i in range(len(permutations)): # Length of all permutations
        sets = []
        for j in permutations[i]: # All the permutations in the index
            try:
                first_sum += data['distances'][count]['source'][j]['distance']
                sets.append(data['distances'][count]['source'][j])
                count += 1
            except:
                first_sum = 0
                count = 0
                sets = []
                break
        distances['sums'].append({
                                    "set_data":sets,
                                    "sum":first_sum
        })
        first_sum = 0
        count = 0
    least_index = 0
    least_dist = distances['sums'][0]['sum']
    for idx,i in enumerate(distances['sums']):
        if i['sum'] < least_dist and i['sum'] != 0:
            least_dist = i['sum']
            least_index = idx
    print(least_dist)
    print(distances['sums'][least_index])
'''
def nearest_neighbor(data,length,start):
    distances = {}
    distances['path'] = []
    used_idx = []
    first_sum = 2147483647 #Int limit for max value, hard to find first index
    next_point = -1
    # First pass to get the starting point
    if start != 0:
        for i in range(len(data['distances'])):
            if data['distances'][i]['source'] == start and data['distances'][i]['distance'] < first_sum:
                next_point = data['distances'][i]['target']
                first_sum = data['distances'][i]['distance']
    else:
        for i in range(len(data['distances'])):
            if data['distances'][i]['source'] == start and data['distances'][i]['distance'] < first_sum:
                next_point = data['distances'][i]['target']
                first_sum = data['distances'][i]['distance']

    used_idx.append(start)
    print("next",next_point)
    while len(used_idx) < length+1:
        print("next",next_point)
        first_sum = 2147483647
        for i in range(len(data['distances'])):
            if data['distances'][i]['target'] == next_point and data['distances'][i]['distance'] < first_sum and data['distances'][i]['source'] not in used_idx:
                new_point = data['distances'][i]['source']
                first_sum = data['distances'][i]['distance']
                print("new_point",new_point)
        for i in range(len(data['distances'])):
            if data['distances'][i]['source'] == next_point and data['distances'][i]['distance'] < first_sum and data['distances'][i]['target'] not in used_idx:
                new_point = data['distances'][i]['target']
                first_sum = data['distances'][i]['distance']
                print("new_point",new_point)
        prev = next_point
        next_point = new_point
        used_idx.append(prev)
    print(used_idx)
            
                    
if __name__ == "__main__":
    try:
        jsonfile = sys.argv[1]
        start = int(sys.argv[2])
        visualize = sys.argv[3]

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
        nearest_neighbor(distances,data['num'],start)
        #print(tsp)
        if visualize == "True":
            initialize_board(data)
        
        
