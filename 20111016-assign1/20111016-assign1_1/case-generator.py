#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import csv


# In[2]:


#reading data-all.json



f2=open('data-all.json')
dataset=json.load(f2)
f2.close()
#print(dataset['2020-06-02']['AP']['districts']['Anantapur']['delta']['confirmed'])
#print(dataset['2020-03-15'])


# In[5]:


#reading code_map
f2=open('code_map.json')
code_map=json.load(f2)
f2.close()
#print(code_map)


# In[6]:


#handling Unknowns

unknown_map=dict()
unknown_map['Unknown_TG']=code_map['Telangana_TG']
unknown_map['Unknown_MN']=code_map['Manipur_MN']
unknown_map['Unknown_GA']=code_map['Goa_GA']
unknown_map['Unknown_AS']=code_map['Assam_AS']
unknown_map['Unknown_SK']=code_map['Sikkim_SK']
#print(code_map['Assam_AS'])


# In[8]:


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

    
    


# In[10]:


#Question 2
#overall number of cases



#print(dist_covid)
#print(dataset['2020-06-02']['UN'])

overall_cases=dict()

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
       #print(x)
       for states in dataset[x].keys():
           d=dataset[x][states]
           if 'districts' in d.keys():
               for keys in d['districts'].keys():
                   if 'delta' in dataset[x][states]['districts'][keys].keys():
                       if 'confirmed' in dataset[x][states]['districts'][keys]['delta'].keys():
                               if keys+'_'+states in overall_cases.keys():
                                   overall_cases[keys+'_'+states]=overall_cases[keys+'_'+states]+dataset[x][states]['districts'][keys]['delta']['confirmed']
                                   #overall_cases[states][keys][1]=overall_cases[states][keys][1]+dataset[x][states]['districts'][keys]['delta']['confirmed']
                               else:
                                   #print(keys+ states)
                                   overall_cases[keys+'_'+states]=dataset[x][states]['districts'][keys]['delta']['confirmed']
                                   #overall_cases[states][keys][1]=dataset[x][states]['districts'][keys]['delta']['confirmed']
                           
                           
                   
#print(overall_cases)
total=0
for x in overall_cases.keys():
   total=total+overall_cases[x]
#print(total)

#print(len(overall_cases))
                         
                              


# In[11]:




#print(state_covid['TG'])

overall_list=list()

lookup_ovr=dict()

count=1
for keys in overall_cases:
    if keys in code_map.keys():
        if code_map[keys] not in lookup_ovr.keys():
            lookup_ovr[code_map[keys]]=dict()
        lookup_ovr[code_map[keys]][1]=overall_cases[keys]
        overall_list.append([code_map[keys],1, overall_cases[keys]])
    elif keys in unknown_map.keys():
        if unknown_map[keys] not in lookup_ovr.keys():
            lookup_ovr[unknown_map[keys]]=dict()
        lookup_ovr[unknown_map[keys]][1]=overall_cases[keys]
        overall_list.append([unknown_map[keys],1, overall_cases[keys]])

overall_list_sorted=sorted(overall_list, key=lambda x:x[0])
overall_list_sorted.insert(0,['districtid','timeid','cases'])  
#print(lookup_ovr)
#print(len(lookup_ovr))
#print(overall_list_sorted)
#print(len(overall_list_sorted))
#print(lookup_ovr[273])
                            
                   
#print(overall_list_sorted)



# In[12]:


#saving lookup_overall for future

with open('lookup_overall.json', 'w') as fp:
    json.dump(lookup_ovr, fp)
fp.close()


# In[13]:


#creating cases-overall.csv 

file = open('cases-overall.csv', 'w+', newline ='') 
with file:     
    write = csv.writer(file) 
    write.writerows(overall_list_sorted) 
file.close()


# In[14]:


#question 2
#monthly cases


monthly_cases=dict()
month_id=1
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
        #print(x)
        for states in dataset[x].keys():
            d=dataset[x][states]
            if 'districts' in d.keys():
                for keys in d['districts'].keys():
                    if 'delta' in dataset[x][states]['districts'][keys].keys():
                        if 'confirmed' in dataset[x][states]['districts'][keys]['delta'].keys():
                                if keys+'_'+states in monthly_cases.keys():
                                    if month_id not in monthly_cases[keys+'_'+states].keys():
                                        monthly_cases[keys+'_'+states][month_id]=dataset[x][states]['districts'][keys]['delta']['confirmed']
                                        
                                    monthly_cases[keys+'_'+states][month_id]=monthly_cases[keys+'_'+states][month_id]+dataset[x][states]['districts'][keys]['delta']['confirmed']
                                    
                                else:
                                    monthly_cases[keys+'_'+states]=dict()
                                    #if month_id not in monthly_cases[keys+'_'+states].keys():
                                    #    overall_cases[keys+'_'+states][month_id]=0
                                   
                                    monthly_cases[keys+'_'+states][month_id]=dataset[x][states]['districts'][keys]['delta']['confirmed']
                                    
                                    
                                    
                                    
    month_id=month_id+1

                                    
#print(monthly_cases)                                    
                                    
                                    


# In[16]:


#creating all entries

for districts in monthly_cases:
    for i in range(1,8):
        if i not in monthly_cases[districts]:
            monthly_cases[districts][i]=0

#print(monthly_cases)
    

#overall_list_sorted=sorted_list = sorted(overall_list, key=lambda x:x[0])
#print(lookup_ovr)
#print(len(lookup_ovr))
#print(overall_list_sorted)
#print(len(overall_list_sorted))
                            
#overall_list_sorted.insert(0,['districtid','timeid','cases'])                     



# In[18]:


#writing to csv

monthly_list=list()
lookup_month=dict()


for d in monthly_cases:
    for timeid in monthly_cases[d]:
        if d in code_map.keys():
            if code_map[d] not in lookup_month.keys():
                lookup_month[code_map[d]]=dict()
            lookup_month[code_map[d]][timeid]=monthly_cases[d][timeid]
            monthly_list.append([code_map[d],timeid,monthly_cases[d][timeid]])
            
            
        elif d in unknown_map.keys():
            if unknown_map[d] not in lookup_month.keys():
                lookup_month[unknown_map[d]]=dict()
            lookup_month[unknown_map[d]][timeid]=monthly_cases[d][timeid]
            monthly_list.append([unknown_map[d],timeid,monthly_cases[d][timeid]])
        
        
        
#print(monthly_list)
#print(len(monthly_list))
#print(len(lookup_month))
#print(lookup_month)
    
monthly_list_sorted=sorted(monthly_list, key=lambda x:(int(x[0]),int(x[1])))

monthly_list_sorted.insert(0,['districtid','timeid','cases'])                     

    
#print(monthly_list_sorted)       


# In[19]:


#saving lookup_monthly for future

with open('lookup_month.json', 'w') as fp1:
    json.dump(lookup_month, fp1)
fp1.close()


# In[20]:


#creating cases-month.csv 

file = open('cases-month.csv', 'w+', newline ='') 
with file:     
    write = csv.writer(file) 
    write.writerows(monthly_list_sorted) 
file.close()


# In[22]:


#question2
#weekly cases


weekly_cases=dict()
week_id=1
counter=1
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
        #print(x)
        for states in dataset[x].keys():
            d=dataset[x][states]
            if 'districts' in d.keys():
                for keys in d['districts'].keys():
                    if 'delta' in dataset[x][states]['districts'][keys].keys():
                        if 'confirmed' in dataset[x][states]['districts'][keys]['delta'].keys():
                                if keys+'_'+states in weekly_cases.keys():
                                    if week_id not in weekly_cases[keys+'_'+states].keys():
                                        #weekly_cases[keys+'_'+states][week_id]=dataset[x][states]['districts'][keys]['delta']['confirmed']
                                        weekly_cases[keys+'_'+states][week_id]=0
                                    weekly_cases[keys+'_'+states][week_id]=weekly_cases[keys+'_'+states][week_id]+dataset[x][states]['districts'][keys]['delta']['confirmed']
                                    
                                else:
                                    weekly_cases[keys+'_'+states]=dict()
                                    #if month_id not in monthly_cases[keys+'_'+states].keys():
                                    #    overall_cases[keys+'_'+states][month_id]=0
                                   
                                    weekly_cases[keys+'_'+states][week_id]=dataset[x][states]['districts'][keys]['delta']['confirmed']
                                    
                                    
                                    
                                    
        counter=counter+1
        if counter>7:
            counter=1
            week_id=week_id+1

                                    
#print(weekly_cases)                                    
                               


# In[23]:


#creating all entries

for districts in weekly_cases:
    for i in range(1,26):
        if i not in weekly_cases[districts]:
            weekly_cases[districts][i]=0

#print(weekly_cases)
    


# In[25]:


#writing to csv

weekly_list=list()
lookup_week=dict()


for d in weekly_cases:
    for timeid in weekly_cases[d]:
        if d in code_map.keys():
            if code_map[d] not in lookup_week.keys():
                lookup_week[code_map[d]]=dict()
            lookup_week[code_map[d]][timeid]=weekly_cases[d][timeid]
            weekly_list.append([code_map[d],timeid,weekly_cases[d][timeid]])
            
            
        elif d in unknown_map.keys():
            if unknown_map[d] not in lookup_week.keys():
                lookup_week[unknown_map[d]]=dict()
            lookup_week[unknown_map[d]][timeid]=weekly_cases[d][timeid]
            weekly_list.append([unknown_map[d],timeid,weekly_cases[d][timeid]])

#print(weekly_list)
#print(len(monthly_list))
#print(len(lookup_week))
#print(lookup_week)
    
weekly_list_sorted=sorted(weekly_list, key=lambda x:(int(x[0]),int(x[1])))

weekly_list_sorted.insert(0,['districtid','timeid','cases'])     

#print(weekly_list_sorted)
    
        


# In[26]:


#saving lookup_weekly for future

with open('lookup_week.json', 'w') as fp2:
    json.dump(lookup_week, fp2)
fp1.close()


# In[27]:


#creating cases-month.csv 

file = open('cases-week.csv', 'w+', newline ='') 
with file:     
    write = csv.writer(file) 
    write.writerows(weekly_list_sorted)
file.close()


# In[ ]:




