#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import statistics
import csv


# In[2]:


#reading code_map
f2=open('code_map.json')
code_map=json.load(f2)
f2.close()


# In[3]:


#reading data-all.json



f2=open('data-all.json')
dataset=json.load(f2)
f2.close()
#print(dataset['2020-06-02']['AP']['districts']['Anantapur']['delta']['confirmed'])
#print(dataset['2020-03-15'])


# In[4]:


#handling Unknowns

unknown_map=dict()
unknown_map['Unknown_TG']=code_map['Telangana_TG']
unknown_map['Unknown_MN']=code_map['Manipur_MN']
unknown_map['Unknown_GA']=code_map['Goa_GA']
unknown_map['Unknown_AS']=code_map['Assam_AS']
unknown_map['Unknown_SK']=code_map['Sikkim_SK']
#print(code_map['Assam_AS'])


# In[5]:


#creating states and district list from data-all.json

days2020=[range(30,32),range(1,30),range(15,32),range(1,31),range(1,32),range(1,31),range(1,32),range(1,32),range(1,6),range(1,32),range(1,31),range(1,32)]
year='2020'
dist_covid=set()
state_covid=dict()

day=30
for month in range(3, 10):
    for day in days2020[month-1]:
        if(month<10):
            smonth='0'+str(month)
        else:
            smonth=str(month)
        if(day<10):
            sday='0'+str(day)
        else:
            sday=str(day)
        x=year+'-'+smonth+'-'+sday
        for states in dataset[x].keys():
            state_covid[states]=set()
            d=dataset[x][states]
            if 'districts' in d.keys():
                for keys in d['districts'].keys():
                    dist_covid.add(keys)
                    state_covid[states].add(keys)
        
#print(state_covid.keys())
#l=0
#for i in state_covid:
#   l=l+len(state_covid[i])

#print(l)
    
    


# In[7]:


#getting the cases



#print(state_covid)

state_map=dict()
for s in state_covid.keys():
    state_map[s]=list()
    for d in state_covid[s]:
        name=d+'_'+s
        if name in code_map.keys():
            state_map[s].append(code_map[name])
        elif name in unknown_map.keys():
            state_map[s].append(unknown_map[name])
            


#print(state_map)
            




# In[8]:


#reading lookups


f1=open('lookup_overall.json')
lookup_ovr=json.load(f1)
f1.close()
#print(lookup_ovr)



# In[10]:


#reading lookups


f1=open('lookup_month.json')
lookup_month=json.load(f1)
f1.close()
#print(lookup_month)


# In[12]:


#reading lookups


f1=open('lookup_week.json')
lookup_week=json.load(f1)
f1.close()
#print(lookup_week)


# In[13]:


# reverse code_map


cm_rev=dict()
for x in code_map.keys():
    cm_rev[code_map[x]]=x
    
#print(cm_rev)


# In[15]:


#now I have all the data structures needed to solve the problem
#solving for overall


overall_list=list()
sos=dict()


for d in lookup_ovr.keys():
    for t in lookup_ovr[d].keys():
        n_cases=list()
        name=cm_rev[int(d)]
        scode=name[-2:]
        
        for dist in state_map[scode]:
            if dist!=d:
                n_cases.append(int(lookup_ovr[str(dist)][t]))
        if(len(n_cases)<1):
            mean=int(lookup_ovr[str(d)][t])
        else:
            mean=statistics.mean(n_cases)
        if(len(n_cases)<2):
            std=0
        else:
            std=statistics.stdev(n_cases)
        overall_list.append([d,t,round(mean,2),round(std,2)])
        sos[d]=dict()
        sos[d][t]=[round(mean,2),round(std,2)]





#print(len(overall_list))
#print(overall_list)
#print(sos)
overall_list_sorted=sorted(overall_list, key=lambda x:x[0])
overall_list_sorted.insert(0,['districtid','timeid','statemean','statestddev']) 
#print(overall_list_sorted)


# In[16]:


#saving the coded graph
with open('state-overall.json', 'w') as fp1:
    json.dump(sos, fp1)
fp1.close()


# In[17]:


#creating cases-overall.csv 

file = open('state-overall.csv', 'w+', newline ='') 
with file:     
    write = csv.writer(file) 
    write.writerows(overall_list_sorted) 
file.close()


# In[18]:


#now I have all the data structures needed to solve the problem
#solving for month


monthly_list=list()
sms=dict()


for d in lookup_month.keys():
    for t in lookup_month[d].keys():
        n_cases=list()
        name=cm_rev[int(d)]
        scode=name[-2:]
        
        for dist in state_map[scode]:
            if dist!=d:
                n_cases.append(int(lookup_month[str(dist)][t]))
        if(len(n_cases)<1):
            mean=int(lookup_month[str(d)][t])
        else:
            mean=statistics.mean(n_cases)
        if(len(n_cases)<2):
            std=0
        else:
            std=statistics.stdev(n_cases)
        monthly_list.append([d,t,round(mean,2),round(std,2)])
        if d not in sms.keys():
            sms[d]=dict()
        sms[d][t]=[round(mean,2),round(std,2)]





#print(len(monthly_list))
#print(overall_list)
#print(sms)
#overall_list_sorted=sorted(overall_list, key=lambda x:x[0])
monthly_list_sorted=sorted(monthly_list, key=lambda x:(x[0],int(x[1])))
monthly_list_sorted.insert(0,['districtid','timeid','statemean','statestddev']) 
#print(monthly_list_sorted)


# In[19]:


#saving the coded graph
with open('state-month.json', 'w') as fp1:
    json.dump(sms, fp1)
fp1.close()


# In[20]:


#creating cases-overall.csv 

file = open('state-month.csv', 'w+', newline ='') 
with file:     
    write = csv.writer(file) 
    write.writerows(monthly_list_sorted) 
file.close()


# In[21]:


#now I have all the data structures needed to solve the problem
#solving for week


weekly_list=list()
sws=dict()


for d in lookup_week.keys():
    for t in lookup_week[d].keys():
        n_cases=list()
        name=cm_rev[int(d)]
        scode=name[-2:]
        
        for dist in state_map[scode]:
            if dist!=d:
                n_cases.append(int(lookup_week[str(dist)][t]))
        if(len(n_cases)<1):
            mean=int(lookup_week[str(d)][t])
        else:
            mean=statistics.mean(n_cases)
        if(len(n_cases)<2):
            std=0
        else:
            std=statistics.stdev(n_cases)
        weekly_list.append([d,t,round(mean,2),round(std,2)])
        if d not in sws.keys():
            sws[d]=dict()
        sws[d][t]=[round(mean,2),round(std,2)]





#print(len(weekly_list))
#print(overall_list)
#print(sws)
#overall_list_sorted=sorted(overall_list, key=lambda x:x[0])

weekly_list_sorted=sorted(weekly_list, key=lambda x:(x[0],int(x[1])))
weekly_list_sorted.insert(0,['districtid','timeid','statemean','statestddev']) 
#print(weekly_list_sorted)


# In[22]:


#saving the coded graph
with open('state-week.json', 'w') as fp1:
    json.dump(sws, fp1)
fp1.close()


# In[23]:


#creating cases-overall.csv 

file = open('state-week.csv', 'w+', newline ='') 
with file:     
    write = csv.writer(file) 
    write.writerows(weekly_list_sorted) 
file.close()


# In[ ]:




