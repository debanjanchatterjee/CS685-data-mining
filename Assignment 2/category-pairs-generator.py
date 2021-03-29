#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv
import networkx as nx


# In[2]:


with open('paths_unfinished.tsv', newline='') as f:
    reader = csv.reader(f)
    pfread = list(reader)
f.close()

pfread=pfread[17:]


# In[3]:


#print(pfread[0])


# In[4]:


#parr=pfread[0][0].split('\t')
#print(parr)
#bc=parr[-3]
#barr=bc.split(';')
#bs=barr[0]
#print(bs)


# In[5]:


with open('article-ids.csv', newline='') as f:
    reader = csv.reader(f)
    article = list(reader)
f.close()


# In[6]:


with open('category-ids.csv', newline='') as f:
    reader = csv.reader(f)
    category = list(reader)
f.close()


# In[7]:


with open('article-categories.csv', newline='') as f:
    reader = csv.reader(f)
    ac = list(reader)
f.close()


# In[8]:


a_map=dict()
for i in article:
    a_map[i[0]]=i[1]
    
#print(a_map)


# In[9]:


c_map=dict()

for i in ac:
    c_map[i[0]]=i[1:]

#print(c_map)


# In[10]:



cat_map=dict()
cat_map_rev=dict()
for i in category:
    cat_map[i[1]]=i[0]
    cat_map_rev[i[0]]=i[1]
#print(cat_map)
#print(cat_map_rev)


# In[11]:



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
    
    


# In[12]:


category_ids=list()

fp=dict()
fup=dict()

for i in cat_map:
    category_ids.append(i)

    
for i in category_ids:
    if i not in fp:
        fp[i]=dict()
    if i not in fup:
        fup[i]=dict()
    for j in category_ids:
        if j not in fp[i]:
            fp[i][j]=0
        if j not in fup[i]:
            fup[i][j]=0
#print(fp)
#print(fup)
    


# In[13]:


artc=dict()


artc['Long_peper']='Long_pepper'
artc['Test']='Directdebit'
artc['Adolph_Hitler']='Adolf_Hitler'
artc['Netbook']='Directdebit'
artc['Podcast']='Podcasting'
artc['Christmas']='Directdebit'
artc['Sportacus']='Directdebit'
artc['Charlottes_web']='Charlotte%27s_Web'
artc['C++']='Directdebit'
artc['Macedonia']='Directdebit'
artc['Usa']='Directdebit'
artc['_Zebra']='Directdebit'
artc['Rss']='RSS_%28file_format%29'
artc['Black_ops_2']='Directdebit'
artc['Western_Australia']='Directdebit'
artc['The_Rock']='Directdebit'
artc['Great']='Directdebit'
artc['Georgia']='Georgia_%28country%29'
artc['English']='English_language'
artc['Fats']='Directdebit'
artc['Mustard']='Directdebit'
artc['Bogota']='Bogot%C3%A1'
artc['The']='Directdebit'
artc['Rat']='Directdebit'
artc['Kashmir']='Directdebit'




# In[14]:


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





for line in pfread:
    line_arr=line[0].split('\t')
    source=line_arr[-3]
    destination=line_arr[-2]
    src_arr=source.split(';')
    source=src_arr[0]
    
    if source not in a_map:
        source=artc[source]
        
    if destination not in a_map:
        destination=artc[destination]
        
    aid_src=a_map[source]
    aid_dst=a_map[destination]
    
    
    cl_src=c_map[aid_src]
    cl_dst=c_map[aid_dst]
    
    
    cat_list_src=set(findSC(cl_src))
    cat_list_dst=set(findSC(cl_dst))
    
    cat_list_src=list(cat_list_src)
    cat_list_dst=list(cat_list_dst)
    
    
    
    for x in cat_list_src:
        for y in cat_list_dst:
            
            if x not in fup:
                fup[x]=dict()
            
            if y not in fup[x]:
                fup[x][y]=0
                
            fup[x][y]=fup[x][y]+1
            
        
        
#print(fup)


# In[15]:


with open('paths_finished.tsv', newline='') as f:
    reader = csv.reader(f)
    pfread = list(reader)
f.close()

pfread=pfread[16:]


# In[16]:




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
    
    s_arr=modify(s_arr)
    if len(s_arr)<=1:
        continue
     
    
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
    
    
    
    for x in cat_list_src:
        for y in cat_list_dst:
            
            if x not in fp:
                fp[x]=dict()
            
            if y not in fp[x]:
                fp[x][y]=0
                
            fp[x][y]=fp[x][y]+1
            
        
        
#print(fp)
        
    


# In[17]:






#for x in fp:
#    if x not in fup[x]:
#        fup[x]=dict()
#       
#    for y in fp[x]:
#        if y not in fup[x]:
#            fup[x][y]=0


#print(fp)


# In[ ]:





# In[18]:




result=list()





for x in fp:
    for y in fp[x]:
        
        total=fup[x][y]+fp[x][y]
        if total==0:
            continue
        pfp=fp[x][y]/total*100
        pfup=fup[x][y]/total*100
        
        e=[x,y,pfp,pfup]
        
        result.append(e)
        

result=sorted(result, key=lambda x:(x[0],x[1]))    
        


# In[19]:


file = open('category-pairs.csv.', 'w+', newline ='') 
with file:     
    write = csv.writer(file) 
    write.writerows(result) 
file.close()


# In[ ]:





# In[ ]:




