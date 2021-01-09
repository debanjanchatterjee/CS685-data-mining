#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import statistics
import csv


# In[4]:


#reading code_graph
f2=open('coded-edge-graph.json')
cg=json.load(f2)
f2.close()
#print(cg)


# In[8]:


#reading lookups


f1=open('lookup_overall.json')
lookup_ovr=json.load(f1)
f1.close()
#print(lookup_ovr)


# In[9]:


#reading lookups


f1=open('lookup_month.json')
lookup_month=json.load(f1)
f1.close()
#print(lookup_month)


# In[11]:


#reading lookups


f1=open('lookup_week.json')
lookup_week=json.load(f1)
f1.close()
#print(lookup_week)


# In[12]:


#now I have all the data structures needed to solve the problem
#solving for overall


overall_list=list()
nos=dict()
for d in lookup_ovr.keys():
    for t in lookup_ovr[d].keys():
        n_cases=list()
        for n in cg[d]:
            n_cases.append(int(lookup_ovr[str(n)][t]))
        mean=statistics.mean(n_cases)
        if(len(n_cases)<2):
            std=0
        else:
            std=statistics.stdev(n_cases)
        overall_list.append([d,t,round(mean,2),round(std,2)])
        nos[d]=dict()
        nos[d][t]=[round(mean,2),round(std,2)]

#print(len(overall_list))
#print(overall_list)
overall_list_sorted=sorted(overall_list, key=lambda x:x[0])
overall_list_sorted.insert(0,['districtid','timeid','neighbormean','neighborstddev']) 
#print(overall_list_sorted)


# In[13]:


#saving the coded graph
with open('neighbor-overall.json', 'w') as fp1:
    json.dump(nos, fp1)
fp1.close()


# In[14]:


#creating cases-overall.csv 

file = open('neighbor-overall.csv', 'w+', newline ='') 
with file:     
    write = csv.writer(file) 
    write.writerows(overall_list_sorted) 
file.close()


# In[16]:



#solving for month


monthly_list=list()
nms=dict()
for d in lookup_month.keys():
    for t in lookup_month[d].keys():
        n_cases=list()
        for n in cg[d]:
            n_cases.append(int(lookup_month[str(n)][t]))
        mean=statistics.mean(n_cases)
        if(len(n_cases)<2):
            std=0
        else:
            std=statistics.stdev(n_cases)
        monthly_list.append([d,t,round(mean,2),round(std,2)])
        if d not in nms.keys():
            nms[d]=dict()
        nms[d][t]=[round(mean,2),round(std,2)]

#print(len(monthly_list))
#print(monthly_list)
#print(nms)
#monthly_list_sorted=sorted(monthly_list, key=lambda x:x[0])
monthly_list_sorted=sorted(monthly_list, key=lambda x:(x[0],int(x[1])))
monthly_list_sorted.insert(0,['districtid','timeid','neighbormean','neighborstddev']) 
#print(monthly_list_sorted)


# In[17]:


#saving the coded graph
with open('neighbor-month.json', 'w') as fp1:
    json.dump(nms, fp1)
fp1.close()


# In[18]:


#creating neighbors-month.csv 

file = open('neighbor-month.csv', 'w+', newline ='') 
with file:     
    write = csv.writer(file) 
    write.writerows(monthly_list_sorted) 
file.close()


# In[21]:


#solving for week


weekly_list=list()
nws=dict()
for d in lookup_week.keys():
    for t in lookup_week[d].keys():
        n_cases=list()
        for n in cg[d]:
            n_cases.append(int(lookup_week[str(n)][t]))
        mean=statistics.mean(n_cases)
        if(len(n_cases)<2):
            std=0
        else:
            std=statistics.stdev(n_cases)
        weekly_list.append([d,t,round(mean,2),round(std,2)])
        if d not in nws.keys():
            nws[d]=dict()
        nws[d][t]=[round(mean,2),round(std,2)]

#print(len(weekly_list))
#print(monthly_list)
#print(nws)

#weekly_list_sorted=sorted(weekly_list, key=lambda x:x[0])
weekly_list_sorted=sorted(weekly_list, key=lambda x:(x[0],int(x[1])))
weekly_list_sorted.insert(0,['districtid','timeid','neighbormean','neighborstddev']) 
#print(weekly_list_sorted)


# In[22]:


#saving the coded graph
with open('neighbor-week.json', 'w') as fp1:
    json.dump(nws, fp1)
fp1.close()


# In[23]:


#creating neighbors-month.csv 

file = open('neighbor-week.csv', 'w+', newline ='') 
with file:     
    write = csv.writer(file) 
    write.writerows(weekly_list_sorted) 
file.close()


# In[ ]:




