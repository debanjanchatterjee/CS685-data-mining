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


# In[3]:



#print(len(categories))
#print(categories)

cat_mod=list()

for x in categories:
    t=x[0]
    i=t.find('subject')
    s=t[i:]
    cat_mod.append(s)
 

#print(len(cat_mod))
#print(cat_mod)
    
    
#x=categories[0].find('subject')
#print(categores[0][x:])


# In[4]:





m=dict()



for x in cat_mod:
    
    s_arr=x.split('.')
    l=len(s_arr)
    #print(l)
    
    for i in range(1,l+1):
        if i not in m:
            m[i]=list()
            m[i].append(s_arr[0:i])
        else:
            m[i].append(s_arr[0:i])
    
       
            
#    if l not in m:
#        m[l]=list()
#        m[l].append(s_arr[l-1])
#    else:
#        m[l].append(s_arr[l-1])
        
#print(len(m))
#print(m.keys())
#print(m)


for keys in m:
    
    #ts=set(m[keys])
    #tl=list(ts)
    tl=m[keys]
    #tl=sorted(tl, key=lambda x:x[keys-1])
    tl.sort()
    m[keys]=tl


 

 

#print(len(m_full))
#print(m_full)
#print(len(m))
#print(m)
    


# In[5]:



def convertLS(l):
    s=""
    for i in l:
       s=s+i+'.' 
    return s[:-1]


m_new=dict()



for keys in m:
    l=m[keys]
    if keys not in m_new:
        m_new[keys]=list()
    for x in l:
        new_s=convertLS(x)
        if new_s not in m_new[keys]:
            m_new[keys].append(new_s)
    

#print(len(m_new))
#print(m_new)
    


# In[6]:


count=1
category_list=list()

for k in m_new:
    l=m_new[k]
    for i in l:
        id=str(count)
        id=id.zfill(4)
        count=count+1
        id='C'+id
        entry=[i,id]
        category_list.append(entry)
        

category_list=sorted(category_list, key=lambda x:x[0])
    


# In[7]:


file = open('category-ids.csv', 'w+', newline ='') 
with file:     
    write = csv.writer(file) 
    write.writerows(category_list) 
file.close()


# In[ ]:





# In[ ]:




