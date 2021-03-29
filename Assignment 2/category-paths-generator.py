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


# In[ ]:





# In[3]:


with open('article-ids.csv', newline='') as f:
    reader = csv.reader(f)
    article = list(reader)
f.close()




# In[4]:


with open('article-categories.csv', newline='') as f:
    reader = csv.reader(f)
    ac = list(reader)
f.close()


# In[5]:


a_map=dict()
for i in article:
    a_map[i[0]]=i[1]
    
#print(a_map)


# In[6]:


c_map=dict()

for i in ac:
    c_map[i[0]]=i[1:]

#print(c_map)


# In[7]:


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


hp=dict()
ht=dict()
sp=dict()
st=dict()

for n in range(1,147):
    id=str(n)
    id=id.zfill(4)
    id='C'+id
    hp[id]=0
    ht[id]=0
    sp[id]=0
    st[id]=0




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
    for art in s_arr:
        aid=a_map[art]
        cl=c_map[aid]
        for c in cl:
            cat_list.append(c)
            cat_set.add(c)
    
    for i in cat_list:
        hp[i]=hp[i]+1
    for i in cat_set:
        ht[i]=ht[i]+1
        
    
#print(len(hp))
#print(len(ht))
#print(hp)
#print(ht)


# In[8]:


with open('edges.csv', newline='') as f:
    reader = csv.reader(f)
    edge_list= list(reader)
f.close()


# In[9]:


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

    


# In[10]:


G = nx.DiGraph()
G.add_edges_from(edge_list)


# In[11]:


#p = nx.shortest_path(G, source='A0010', target='A0099')
#print(p)


# In[12]:





for line in pfread:
    line_arr=line[0].split('\t')
    s=line_arr[-2]
    #if '<' in s:
    #    continue
    
    #s=s.strip()
    #x=s.find('\t')
    #s=s[:x]
    s_arr=s.split(';')
    s_arr=modify(s_arr)
    if len(s_arr)<=1:
        continue
    #print(s_arr)
    cat_list=list()
    cat_set=set()
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
    
    #print(shortest_path)
    for aid in shortest_path:
        cl=c_map[aid]
        for c in cl:
            cat_list.append(c)
            cat_set.add(c)
    
    for i in cat_list:
        sp[i]=sp[i]+1
    for i in cat_set:
        st[i]=st[i]+1
        
#print(len(sp))
#print(len(st))
#print(sp)
#print(st)
        


# In[13]:



result=list()


for k in hp:
    e=[k,ht[k],hp[k],st[k],sp[k]]
    result.append(e)
    


# In[14]:


file = open('category-paths.csv', 'w+', newline ='') 
with file:     
    write = csv.writer(file) 
    write.writerows(result) 
file.close()


# In[ ]:




