#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import statistics
import csv


# In[2]:


#reading zscores

f1=open('zscore-overall.json')
zos=json.load(f1)
f1.close()
#print(zos)


# In[3]:


#reading zscores

f1=open('zscore-month.json')
zms=json.load(f1)
f1.close()


# In[4]:


#reading zscores

f1=open('zscore-week.json')
zws=json.load(f1)
f1.close()


# In[6]:


# solving overall

overall_list=list()




for d in zos.keys():
    for t in zos[d]:
        if zos[d][t][0]>1:
            nspot='hot'
        elif zos[d][t][0]<-1:
            nspot='cold'
        else:
            nspot='na'
        if nspot!='na':
            overall_list.append([t,'neighborhood',nspot,d])
            
        if zos[d][t][1]>1:
            sspot='hot'
        elif zos[d][t][1]<-1:
            sspot='cold'
        else:
            sspot='na'
        if sspot!='na':
            overall_list.append([t,'state',sspot,d])

            

        
#print(len(overall_list))        
#print(zos)
#overall_list_sorted=sorted(overall_list, key=lambda x:x[0])
overall_list_sorted=sorted(overall_list, key=lambda x:(int(x[0]),int(x[3])))
overall_list_sorted.insert(0,['timeid','method','spot','districtid']) 
#print(overall_list_sorted)



# In[7]:


#creating cases-overall.csv 

file = open('method-spot-overall.csv', 'w+', newline ='') 
with file:     
    write = csv.writer(file) 
    write.writerows(overall_list_sorted) 
file.close()


# In[8]:


# solving monthly

monthly_list=list()




for d in zms.keys():
    for t in zms[d]:
        if zms[d][t][0]>1:
            nspot='hot'
        elif zms[d][t][0]<-1:
            nspot='cold'
        else:
            nspot='na'
        if nspot!='na':
            monthly_list.append([t,'neighborhood',nspot,d])
            
        if zms[d][t][1]>1:
            sspot='hot'
        elif zms[d][t][1]<-1:
            sspot='cold'
        else:
            sspot='na'
        if sspot!='na':
            monthly_list.append([t,'state',sspot,d])

            

        
#print(len(overall_list))        
#print(zos)
#overall_list_sorted=sorted(overall_list, key=lambda x:x[0])
monthly_list_sorted=sorted(monthly_list, key=lambda x:(int(x[0]),int(x[3])))
monthly_list_sorted.insert(0,['timeid','method','spot','districtid']) 
#print(monthly_list_sorted)


# In[9]:


#creating cases-overall.csv 

file = open('method-spot-month.csv', 'w+', newline ='') 
with file:     
    write = csv.writer(file) 
    write.writerows(monthly_list_sorted) 
file.close()


# In[10]:


# solving weekly

weekly_list=list()




for d in zws.keys():
    for t in zws[d]:
        if zws[d][t][0]>1:
            nspot='hot'
        elif zws[d][t][0]<-1:
            nspot='cold'
        else:
            nspot='na'
        if nspot!='na':
            weekly_list.append([t,'neighborhood',nspot,d])
            
        if zws[d][t][1]>1:
            sspot='hot'
        elif zws[d][t][1]<-1:
            sspot='cold'
        else:
            sspot='na'
        if sspot!='na':
            weekly_list.append([t,'state',sspot,d])

            

        
#print(len(overall_list))        
#print(zos)
#overall_list_sorted=sorted(overall_list, key=lambda x:x[0])
weekly_list_sorted=sorted(weekly_list, key=lambda x:(int(x[0]),int(x[3])))
weekly_list_sorted.insert(0,['timeid','method','spot','districtid']) 
#print(weekly_list_sorted)


# In[11]:


#creating cases-overall.csv 

file = open('method-spot-week.csv', 'w+', newline ='') 
with file:     
    write = csv.writer(file) 
    write.writerows(weekly_list_sorted) 
file.close()


# In[ ]:




