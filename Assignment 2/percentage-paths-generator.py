#!/usr/bin/env python
# coding: utf-8

# In[8]:


import csv


# In[9]:


with open('finished-paths-no-back.csv', newline='') as f:
    reader = csv.reader(f)
    fpnb = list(reader)
f.close()


# In[10]:


with open('finished-paths-back.csv', newline='') as f:
    reader = csv.reader(f)
    fpb = list(reader)
f.close()


# In[11]:




result1=list()
for i in range(1,13):
    result1.append(0)
    
    
total1=0

for i in fpnb:
    diff=int(i[0])-int(i[1])
    if diff>10:
        result1[11]=result1[11]+1
    else:
        result1[diff]=result1[diff]+1
    total1=total1+1
    
#print(total1)    
for i in range(0,12):
    result1[i]=(result1[i]*100)/total1
    
    
result1=[result1]
#print(result1)


# In[12]:


file = open('percentage-paths-no-back.csv', 'w+', newline ='') 
with file:     
    write = csv.writer(file) 
    write.writerows(result1) 
file.close()


# In[13]:


result2=list()
for i in range(1,13):
    result2.append(0)
    
    
total2=0    

for i in fpb:
    diff=int(i[0])-int(i[1])
    if diff>10:
        result2[11]=result2[11]+1
    else:
        result2[diff]=result2[diff]+1
    total2=total2+1
    
#print(total2)    
for i in range(0,12):
    result2[i]=(result2[i]*100)/total2

result2=[result2]
#print(result2)


# In[7]:


file = open('percentage-paths-back.csv', 'w+', newline ='') 
with file:     
    write = csv.writer(file) 
    write.writerows(result2) 
file.close()


# In[ ]:




