#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv


# In[2]:


read=list()

f = open("shortest-path-distance-matrix.txt", "r")
for x in f:
  read.append(x.strip())

read=read[17:]


# In[3]:


#print(read[0])
#print(len(read))
#print(len(read[2]))


# In[4]:




m=dict()


count=1
for x in range(1,4605):
    id=str(count)
    id=id.zfill(4)
    
    id='A'+id
    m[count]=id
    count=count+1
    
#print(m)
    
    


# In[5]:



x=1
#print(len(read[0]))
result=list()
for l in read:
    
    y=1
   
    for i in l:
        
        if i=='1':
            entry=list()
            entry.append(m[x])
            entry.append(m[y])
            result.append(entry)
        else:
            y=y+1
            continue
        y=y+1
            
    
        
    x=x+1
    


result=sorted(result, key=lambda x:(x[0],x[1]))
#print('done')           
            


# In[6]:


file = open('edges.csv', 'w+', newline ='') 
with file:     
    write = csv.writer(file) 
    write.writerows(result) 
file.close()


# In[ ]:





# In[ ]:




