import sys
import random
import json
import math
from draw import *

def calculate_distance(**kwargs):
    dist_list = []
    for i in range(kwargs['num']-1):
        for j in range(len(kwargs['edges'])):
            if i == kwargs['edges'][j]['source']: # This assumes that the id is the same as the index which may not always be true
                target = kwargs['edges'][j]['target']
                x,y = kwargs['nodes'][i]['x'],kwargs['nodes'][i]['y']
                x2,y2 = kwargs['nodes'][target]['x'],kwargs['nodes'][target]['y']
                distance = math.dist([x,y],[x2,y2])
                dist_list.append((i,target,distance))
    return dist_list

if __name__ == "__main__":
    try:
        jsonfile = sys.argv[1]
    except:
        jsonfile = None
        print("Enter a .json filename")
        quit(0)
    
    if jsonfile != None:
        try:
            with open (jsonfile) as file:
                data = json.load(file)
        except:
            print("Please enter a valid .json filename or make sure you have input a valid json")
            quit()
        distances = calculate_distance(**data)
        initialize_board(**data)
        
        
