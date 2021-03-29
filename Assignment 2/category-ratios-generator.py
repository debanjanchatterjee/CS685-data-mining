#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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


with open('category-ids.csv', newline='') as f:
    reader = csv.reader(f)
    category = list(reader)
f.close()


# In[5]:


with open('article-categories.csv', newline='') as f:
    reader = csv.reader(f)
    ac = list(reader)
f.close()


# In[6]:


a_map=dict()
for i in article:
    a_map[i[0]]=i[1]
    
#print(a_map)


# In[7]:


c_map=dict()

for i in ac:
    c_map[i[0]]=i[1:]

#print(c_map)


# In[8]:



cat_map=dict()
cat_map_rev=dict()
for i in category:
    cat_map[i[1]]=i[0]
    cat_map_rev[i[0]]=i[1]
#print(cat_map)
#print(cat_map_rev)


# In[9]:


with open('edges.csv', newline='') as f:
    reader = csv.reader(f)
    edge_list= list(reader)
f.close()


# In[10]:


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


# In[11]:


G = nx.DiGraph()
G.add_edges_from(edge_list)


# In[ ]:





# In[12]:


def subCategories(c):
    c_name=cat_map[c]
    c_arr=c_name.split('.')
    str=''
    r_list=list()
    for s in c_arr:
        str=str+s
        str_id=cat_map_rev[str]
        r_list.append(str_id)
        str=str+'.'
    return r_list
        

def findSC(l):
    lnew=list()
    for i in l:
        lnew=lnew+subCategories(i)
    return lnew
    


# In[13]:


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




hp_map=dict()
sp_map=dict()

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
    #print(s_arr)
    source=s_arr[0]
    destination=s_arr[-1]
    
    #if source not in a_map:
    #    source=artc[source]
        
    #if destination not in a_map:
    #    destination=artc[destination]
        
    aid_src=a_map[source]
    aid_dst=a_map[destination]
    
    
    cl_src=c_map[aid_src]
    cl_dst=c_map[aid_dst]
    
    
    
    cat_list_src=set(findSC(cl_src))
    cat_list_dst=set(findSC(cl_dst))
    
    cat_list_src=list(cat_list_src)
    cat_list_dst=list(cat_list_dst)
    
    
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
    
    for x in cat_list_src:
        if x not in hp_map:
            hp_map[x]=dict()
            
        if x not in sp_map:
            sp_map[x]=dict()
            
            
        for y in cat_list_dst:
            if y not in hp_map[x]:
                hp_map[x][y]=0
            if y not in sp_map[x]:
                sp_map[x][y]=0
                
                
            hp_map[x][y]=hp_map[x][y]+lhp
            sp_map[x][y]=sp_map[x][y]+lsp
    
    


# In[14]:


result=list()



for x in hp_map:
    for y in hp_map[x]:
        r=hp_map[x][y]/sp_map[x][y]
        e=[x,y,r]
        result.append(e)




result=sorted(result, key=lambda x:(x[0],x[1]))
#print(result)


# In[15]:


file = open('category-ratios.csv', 'w+', newline ='') 
with file:     
    write = csv.writer(file) 
    write.writerows(result) 
file.close()


# In[ ]:




