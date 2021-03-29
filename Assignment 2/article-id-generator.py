#!/usr/bin/env python
# coding: utf-8

# In[1]:


import  csv


# In[2]:


with open('articles.tsv', newline='') as f:
    reader = csv.reader(f)
    articles = list(reader)
f.close()
articles= articles[12:]


# In[3]:


#print(len(articles))
#print(articles)


# In[4]:



#print(len(articles))
#print(articles)

count=1
article_list=list()

for x in articles:
    id=str(count)
    id=id.zfill(4)
    count=count+1
    id='A'+id
    entry=[x[0],id]
    article_list.append(entry)
    

#print(article_list) 
    



# In[5]:


file = open('article-ids.csv', 'w+', newline ='') 
with file:     
    write = csv.writer(file) 
    write.writerows(article_list) 
file.close()


# In[ ]:




