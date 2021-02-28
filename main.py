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
    test_form = {}
    test_form['distances'] = []
    for i in range(data['num']):
        test_form['distances'].append({'source':[]})
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
    with open ('data.json', 'w') as data:
        json.dump(dist_dict,data,indent=4)
    return dist_dict

def solve_problem(data,length,start):
    permutations = [p for p in itertools.permutations(range(0,length+1))]
    #print(permutations)
    distances = {}
    distances['sums'] = []
    first_sum = 0

    for i in range(len(permutations)):
        first_sum = 0
        if permutations[i][0] != start:
            continue
        else:
            for j in range(len(permutations[i])-1):
                for k in range(len(data['distances'])):
                    if permutations[i][j] == data['distances'][k]['source'] and permutations[i][j+1] == data['distances'][k]['target'] or permutations[i][j] == data['distances'][k]['target'] and permutations[i][j+1] == data['distances'][k]['source']:
                        first_sum += data['distances'][k]['distance']
            distances['sums'].append({
                                    'order':list(permutations[i]),
                                    'sum': first_sum
            })

    least_sum = distances['sums'][0]['sum']
    order = 0
    for i in distances['sums']:
        if i['sum'] <  least_sum:
            least_sum = i['sum']
            order = i['order']

    print("The shortest path is %d units, order:"%least_sum,order)
    return order

def nearest_neighbor(data,length,start):
    distances = {}
    distances['path'] = []
    distances['path'].append({'source':[]})
    used_idx = []
    sums = 0
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
    sums += first_sum
    used_idx.append(start)
    while len(used_idx) < length+1:
        first_sum = 2147483647
        for i in range(len(data['distances'])): #Check what targets the next point
            if data['distances'][i]['target'] == next_point and data['distances'][i]['distance'] < first_sum and data['distances'][i]['source'] not in used_idx:
                new_point = data['distances'][i]['source']
                first_sum = data['distances'][i]['distance']
                sums += first_sum
        for i in range(len(data['distances'])): #Check the next point as source
            if data['distances'][i]['source'] == next_point and data['distances'][i]['distance'] < first_sum and data['distances'][i]['target'] not in used_idx:
                new_point = data['distances'][i]['target']
                first_sum = data['distances'][i]['distance']
                sums += first_sum
        prev = next_point
        next_point = new_point
        used_idx.append(prev)
    print("Nearest neighbor starting from %d:\nDistance is: %d"%(start,sums), used_idx)
    return used_idx

'''           
def brute_force(data,length,start):
    limit = math.factorial(length-1)
    distances = {}
    distances['path'] = []
    used_idx = []
    first_sum = 2147483647 #Int limit for max value, hard to find first index
    next_point = -1
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

    while used_idx <= limit:
        for i in range(length+1):
'''       

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
        shortest_path = solve_problem(distances,data['num'],start)
        if visualize == "True":
            initialize_board(data,shortest_path)
        
        
