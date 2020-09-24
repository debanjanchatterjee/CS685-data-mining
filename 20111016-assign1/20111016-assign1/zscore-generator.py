#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import statistics
import csv


# In[2]:


#reading lookups


f1=open('lookup_overall.json')
lookup_ovr=json.load(f1)
f1.close()
#print(lookup_ovr)


# In[4]:


#reading lookups


f1=open('lookup_month.json')
lookup_month=json.load(f1)
f1.close()
#print(lookup_month)


# In[6]:


#reading lookups


f1=open('lookup_week.json')
lookup_week=json.load(f1)
f1.close()
#print(lookup_week)


# In[8]:


#reading stats jsons


f1=open('neighbor-overall.json')
nos=json.load(f1)
f1.close()
#print(nos['665'])
#print(nos)


# In[22]:


#reading stats jsons


f1=open('neighbor-month.json')
nms=json.load(f1)
f1.close()
#print(nms)
#print(nms['665'])


# In[23]:


#reading stats jsons


f1=open('neighbor-week.json')
nws=json.load(f1)
f1.close()


# In[24]:


#reading stats jsons


f1=open('state-overall.json')
sos=json.load(f1)
f1.close()
#print(sos)


# In[25]:


#reading stats jsons


f1=open('state-month.json')
sms=json.load(f1)
f1.close()


# In[26]:


#reading stats jsons


f1=open('state-week.json')
sws=json.load(f1)
f1.close()


# In[12]:


# solving overall

overall_list=list()
zos=dict()

for d in lookup_ovr.keys():
    for t in lookup_ovr[d].keys():
        x=int(lookup_ovr[str(d)][t])
        navg=nos[str(d)][t][0]
        nstd=nos[str(d)][t][1]
        if nstd==0:
            nzx=0
        else:
            nzx=(x-navg)/nstd
        savg=sos[str(d)][t][0]
        sstd=sos[str(d)][t][1]
        if sstd==0:
            szx=0
        else:
            szx=(x-savg)/sstd
        overall_list.append([d,t,round(nzx,2),round(szx,2)])
        zos[d]=dict()
        zos[d][t]=[round(nzx,2),round(szx,2)]

        
#print(len(overall_list))        
#print(zos)
overall_list_sorted=sorted(overall_list, key=lambda x:x[0])
overall_list_sorted.insert(0,['districtid','timeid','neighborhoodzscore','statezscore']) 
#print(overall_list_sorted)





# In[13]:


#saving the coded graph
with open('zscore-overall.json', 'w') as fp1:
    json.dump(zos, fp1)
fp1.close()


# In[14]:


#creating cases-overall.csv 

file = open('zscore-overall.csv', 'w+', newline ='') 
with file:     
    write = csv.writer(file) 
    write.writerows(overall_list_sorted) 
file.close()


# In[17]:


monthly_list=list()
zms=dict()

for d in lookup_month.keys():
    for t in lookup_month[d].keys():
        x=int(lookup_month[str(d)][t])
        navg=nms[str(d)][t][0]
        nstd=nms[str(d)][t][1]
        if nstd==0:
            nzx=0
        else:
            nzx=(x-navg)/nstd
        savg=sms[str(d)][t][0]
        sstd=sms[str(d)][t][1]
        if sstd==0:
            szx=0
        else:
            szx=(x-savg)/sstd
        monthly_list.append([d,t,round(nzx,2),round(szx,2)])
        if d not in zms.keys():
            zms[d]=dict()
        zms[d][t]=[round(nzx,2),round(szx,2)]

        
#print(len(monthly_list))        
#print(zms)
#overall_list_sorted=sorted(overall_list, key=lambda x:x[0])
monthly_list_sorted=sorted(monthly_list, key=lambda x:(x[0],int(x[1])))
monthly_list_sorted.insert(0,['districtid','timeid','neighborhoodzscore','statezscore']) 
#print(monthly_list_sorted)



# In[18]:


#saving the coded graph
with open('zscore-month.json', 'w') as fp1:
    json.dump(zms, fp1)
fp1.close()


# In[19]:


#creating cases-overall.csv 

file = open('zscore-month.csv', 'w+', newline ='') 
with file:     
    write = csv.writer(file) 
    write.writerows(monthly_list_sorted) 
file.close()


# In[27]:


#week

weekly_list=list()
zws=dict()

for d in lookup_week.keys():
    for t in lookup_week[d].keys():
        x=int(lookup_week[str(d)][t])
        navg=nws[str(d)][t][0]
        nstd=nws[str(d)][t][1]
        if nstd==0:
            nzx=0
        else:
            nzx=(x-navg)/nstd
        savg=sws[str(d)][t][0]
        sstd=sws[str(d)][t][1]
        if sstd==0:
            szx=0
        else:
            szx=(x-savg)/sstd
        weekly_list.append([d,t,round(nzx,2),round(szx,2)])
        if d not in zws.keys():
            zws[d]=dict()
        zws[d][t]=[round(nzx,2),round(szx,2)]

        
#print(len(weekly_list))        
#print(zws)
#overall_list_sorted=sorted(overall_list, key=lambda x:x[0])
weekly_list_sorted=sorted(weekly_list, key=lambda x:(x[0],int(x[1])))
weekly_list_sorted.insert(0,['districtid','timeid','neighborhoodzscore','statezscore']) 
#print(weekly_list_sorted)


# In[28]:


#saving the coded graph
with open('zscore-week.json', 'w') as fp1:
    json.dump(zws, fp1)
fp1.close()


# In[29]:


#creating cases-overall.csv 

file = open('zscore-week.csv', 'w+', newline ='') 
with file:     
    write = csv.writer(file) 
    write.writerows(weekly_list_sorted) 
file.close()


# In[ ]:




