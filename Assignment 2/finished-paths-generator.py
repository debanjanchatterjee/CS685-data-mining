#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import networkx as nx


# In[2]:


with open('paths_finished.tsv', newline='') as f:
    reader = csv.reader(f)
    pfread = list(reader)
f.close()

pfread=pfread[16:]


# In[3]:


with open('article-ids.csv', newline='') as f:
    reader = csv.reader(f)
    article = list(reader)
f.close()


# In[4]:


a_map=dict()
for i in article:
    a_map[i[0]]=i[1]
    
#print(a_map)


# In[5]:


with open('edges.csv', newline='') as f:
    reader = csv.reader(f)
    edge_list= list(reader)
f.close()


# In[6]:


s=set()
isolated_nodes=set()
for i in edge_list:
    for j in i:
        s.add(j)

for c in range(1,4605):
    id=str(c)
    id=id.zfill(4)
    id='A'+id
    if id not in s:
        isolated_nodes.add(id)
#print(isolated_nodes)


# In[7]:


G = nx.DiGraph()
G.add_edges_from(edge_list)


# In[8]:


def modify(l):
    if '<' not in l:
        return l
    index=-1
    for i in range(0,len(l)):
        if l[i]=='<':
            index=i
            break
    
    temp1=l[:index-1]
    temp2=l[index+1:]
    l=temp1+temp2
    return modify(l)


result1=list()


for line in pfread:
    line_arr=line[0].split('\t')
    s=line_arr[-2]
    #if '<' in s:
    #    continue
    
    #s=s.strip()
    #x=s.find('\t')
    #s=s[:x]
    s_arr=s.split(';')
    #print(s_arr)
    cat_list=list()
    cat_set=set()
    s_arr=modify(s_arr)
    if len(s_arr)<=1:
        continue
    
    lhp=len(s_arr)-1
    
    sa=list()
    for a in s_arr:
        aid=a_map[a]
        sa.append(aid)
    #print(sa)   
    if sa[0] in isolated_nodes:
        continue
    if sa[-1] in isolated_nodes:
        continue
    shortest_path=nx.shortest_path(G, source=sa[0], target=sa[-1])
    
    lsp=len(shortest_path)-1
    ratio=lhp/lsp
    e=[lhp,lsp,ratio]
    
    result1.append(e)
    
#result1=sorted(result1, key=lambda x:(x[0]))


# In[9]:


file = open('finished-paths-no-back.csv', 'w+', newline ='') 
with file:     
    write = csv.writer(file) 
    write.writerows(result1) 
file.close()


# In[10]:




result2=list()


for line in pfread:
    line_arr=line[0].split('\t')
    s=line_arr[-2]
    #if '<' in s:
    #    continue
    
    #s=s.strip()
    #x=s.find('\t')
    #s=s[:x]
    s_arr=s.split(';')
    #print(s_arr)
    cat_list=list()
    cat_set=set()
    
    if len(s_arr)<=1:
        continue
    
    lhp=len(s_arr)-1
    
    sa=list()
    sa=[a_map[s_arr[0]],a_map[s_arr[-1]]]
    
   
    #print(sa)   
    if sa[0] in isolated_nodes:
        continue
    if sa[-1] in isolated_nodes:
        continue
    shortest_path=nx.shortest_path(G, source=sa[0], target=sa[-1])
    
    lsp=len(shortest_path)-1
    ratio=lhp/lsp
    e=[lhp,lsp,ratio]
    
    result2.append(e)
    
#result2=sorted(result2, key=lambda x:(x[0]))


# In[11]:


file = open('finished-paths-back.csv', 'w+', newline ='') 
with file:     
    write = csv.writer(file) 
    write.writerows(result2) 
file.close()


# In[ ]:




