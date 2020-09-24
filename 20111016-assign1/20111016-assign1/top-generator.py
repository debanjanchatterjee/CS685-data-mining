#!/usr/bin/env python
# coding: utf-8

# In[17]:


import csv


# In[18]:


with open('zscore-overall.csv', newline='') as f:
    reader = csv.reader(f)
    overall_list = list(reader)
f.close()

#print(overall_list)


# In[19]:


with open('zscore-month.csv', newline='') as f:
    reader = csv.reader(f)
    monthly_list = list(reader)
f.close()
#print(monthly_list)


# In[20]:


with open('zscore-week.csv', newline='') as f:
    reader = csv.reader(f)
    weekly_list = list(reader)
f.close()


# In[21]:


#overall
ovr_op=list()
ovr=overall_list[1:]

#print(ovr)
ovrn=sorted(ovr, key=lambda x:(int(x[1]),float(x[2])))
ovrs=sorted(ovr, key=lambda x:(int(x[1]),float(x[3])))
#ovr=sorted(ovr, key=lambda x:int(x[2]))
#print(len(ovrn))

#print(ovrn)


# In[22]:


#overall

ovr_op.append(['timeid','method','spot','districtid1','districtid2','districtid3','districtid4','districtid5'])
ovr_op.append(['1','neighborhood','cold', ovrn[0][0],ovrn[1][0],ovrn[2][0],ovrn[3][0],ovrn[4][0]])
ovr_op.append(['1','neighborhood','hot', ovrn[626][0],ovrn[625][0],ovrn[624][0],ovrn[623][0],ovrn[622][0]])
ovr_op.append(['1','state','cold', ovrs[0][0],ovrs[1][0],ovrs[2][0],ovrs[3][0],ovrs[4][0]])
ovr_op.append(['1','state','hot', ovrs[626][0],ovrs[625][0],ovrs[624][0],ovrs[623][0],ovrs[622][0]])
#print(ovr_op)  
    


# In[23]:


#creating cases-overall.csv 

file = open('top-overall.csv', 'w+', newline ='') 
with file:     
    write = csv.writer(file) 
    write.writerows(ovr_op) 
file.close()


# In[9]:


#monthly
month_op=list()
month=monthly_list[1:]

#print(ovr)
monthn=sorted(month, key=lambda x:(int(x[1]),float(x[2])))
months=sorted(month, key=lambda x:(int(x[1]),float(x[3])))
#ovr=sorted(ovr, key=lambda x:int(x[2]))
#print(len(monthn))
#print(len(months))

#print(monthn)
#print(months)


# In[10]:


#monthly


month_op.append(['timeid','method','spot','districtid1','districtid2','districtid3','districtid4','districtid5'])
base=0
for t in range(1,8):
    base=(t-1)*627
    end=t*627
    month_op.append([t,'neighborhood','cold', monthn[base+0][0],monthn[base+1][0],monthn[base+2][0],monthn[base+3][0],monthn[base+4][0]])
    month_op.append([t,'neighborhood','hot', monthn[end-1][0],monthn[end-2][0],monthn[end-3][0],monthn[end-4][0],monthn[end-5][0]])
    month_op.append([t,'state','cold', months[base+0][0],months[base+1][0],months[base+2][0],months[base+3][0],months[base+4][0]])
    month_op.append([t,'state','hot', months[end-1][0],months[end-2][0],months[end-3][0],months[end-4][0],months[end-5][0]])

#print(month_op) 


# In[11]:


#creating cases-overall.csv 

file = open('top-month.csv', 'w+', newline ='') 
with file:     
    write = csv.writer(file) 
    write.writerows(month_op) 
file.close()


# In[12]:


#weekly
week_op=list()
week=weekly_list[1:]

#print(ovr)
weekn=sorted(week, key=lambda x:(int(x[1]),float(x[2])))
weeks=sorted(week, key=lambda x:(int(x[1]),float(x[3])))
#ovr=sorted(ovr, key=lambda x:int(x[2]))
#print(len(weekn))
#print(len(months))

#print(monthn)
#print(months)


# In[13]:


#weekly


week_op.append(['timeid','method','spot','districtid1','districtid2','districtid3','districtid4','districtid5'])
base=0
for t in range(1,26):
    base=(t-1)*627
    end=t*627
    week_op.append([t,'neighborhood','cold', weekn[base+0][0],weekn[base+1][0],weekn[base+2][0],weekn[base+3][0],weekn[base+4][0]])
    week_op.append([t,'neighborhood','hot', weekn[end-1][0],weekn[end-2][0],weekn[end-3][0],weekn[end-4][0],weekn[end-5][0]])
    week_op.append([t,'state','cold', weeks[base+0][0],weeks[base+1][0],weeks[base+2][0],weeks[base+3][0],weeks[base+4][0]])
    week_op.append([t,'state','hot', weeks[end-1][0],weeks[end-2][0],weeks[end-3][0],weeks[end-4][0],weeks[end-5][0]])

#print(week_op) 


# In[14]:


#creating cases-overall.csv 

file = open('top-week.csv', 'w+', newline ='') 
with file:     
    write = csv.writer(file) 
    write.writerows(week_op) 
file.close()


# In[ ]:




