#!/usr/bin/env python
# coding: utf-8

# In[5]:


import json
import csv


# In[6]:


#reading code_map
f2=open('code_map.json')
code_map=json.load(f2)
f2.close()
#print(code_map)


# In[8]:


#reading code_graph
f2=open('coded-edge-graph.json')
cg=json.load(f2)
f2.close()
#print(cg)


# In[9]:


#Question 3

edge_list=set()
#print(adj_list)

for district in cg.keys():
    for neighbors in cg[district]:
        edge=[int(district),int(neighbors)]
        
        edge.sort()
        
        edge_list.add(tuple(edge))
            
#print(edge_list)
#print(len(edge_list))


# In[10]:


#Question 3 storing into csv file

file = open('edge-graph.csv', 'w+', newline ='') 
with file:     
    write = csv.writer(file) 
    write.writerows(edge_list) 
file.close()


# In[ ]:




