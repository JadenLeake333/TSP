import random
import sys
import json
width = int(sys.argv[1])
height = int(sys.argv[2])
num = int(sys.argv[3])
filename = sys.argv[4]
nodes_dict = {
              'num':num,
              'width':width,
              'height':height  
}
nodes_dict['nodes'] = []
nodes_dict['edges'] = []
for i in range(num+1):
    rwidth = random.randrange(0,width)
    rheight = random.randrange(0,height)
    nodes_dict['nodes'].append({
                                'x':rwidth,
                                'y':rheight,
                                'id':i,
                                'label':i,
                                'flag':1
    })

for i in range(num+1):
    for j in range(i+1,num+1):
        nodes_dict['edges'].append({
                                    'source':i,
                                    'target':j
        })
with open(filename,'w') as file:
    json.dump(nodes_dict,file,indent=4)