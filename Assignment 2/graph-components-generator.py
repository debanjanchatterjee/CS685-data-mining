#!/usr/bin/env python
# coding: utf-8

# In[6]:


import csv
import networkx as nx


# In[7]:


with open('edges.csv', newline='') as f:
    reader = csv.reader(f)
    edge_list= list(reader)
f.close()


# In[8]:


#print(edge_list)


# In[9]:


edges=set()

for i in edge_list:
    for j in i:
        edges.add(j)

isolated_nodes=4604-len(edges)
#print(isolated_nodes)
i_nodes=list()
for i in range(0,isolated_nodes):
    i_nodes.append(i)
    
#print(len(edge_list))


# In[10]:


G = nx.Graph()
G.add_nodes_from(i_nodes)
G.add_edges_from(edge_list)


# In[11]:


#print(G)
#print(G.number_of_nodes())
#print(G.number_of_edges())


# In[12]:


numbercc=nx.algorithms.components.number_connected_components(G)
#print(numbercc)


# In[13]:


result=list()


S = [G.subgraph(c).copy() for c in nx.connected_components(G)]
#print(len(S))


# In[14]:



for sg in S:
    a=sg.number_of_nodes()
    b=sg.number_of_edges()
    c=nx.algorithms.distance_measures.diameter(sg)
    e=[a,b,c]
    result.append(e)
    
result=sorted(result, key=lambda x:(x[0],x[1]))
#print('done')


# In[ ]:


#print(result)
#print('done')


# In[15]:


file = open('graph-components.csv', 'w+', newline ='') 
with file:     
    write = csv.writer(file) 
    write.writerows(result) 
file.close()


# In[ ]:




