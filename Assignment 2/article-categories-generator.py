#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv


# In[2]:


with open('categories.tsv', newline='') as f:
    reader = csv.reader(f)
    categories = list(reader)
f.close()

categories=categories[13:]
#print(categories)


# In[3]:


with open('article-ids.csv', newline='') as f:
    reader = csv.reader(f)
    article_list = list(reader)
f.close()


# In[4]:


with open('category-ids.csv', newline='') as f:
    reader = csv.reader(f)
    category_list = list(reader)
f.close()


# In[5]:



cat_mod=list()

for x in categories:
    e=list()
    t=x[0]
    i=t.find('subject')
    s=t[i:]
    s0=t[:i].strip()
    e.append(s0)
    e.append(s)
    cat_mod.append(e)
 

#print(len(cat_mod))
#print(cat_mod)


# In[6]:




result=list()
m=dict()

for i in category_list:
    m[i[0]]=i[1]
for a in article_list:
    entry=list()
    a_name=a[0]
    entry.append(a[1])
    
    for x in cat_mod:
        #print(x[0])
        #print(a_name)
        
        if x[0]==a_name:
           entry.append(m[x[1]])
    if len(entry)==1:
        entry.append('C0001')
    result.append(entry)
      


#print(result[4545])


# In[7]:


file = open('article-categories.csv', 'w+', newline ='') 
with file:     
    write = csv.writer(file) 
    write.writerows(result) 
file.close()


# In[ ]:




