#!/usr/bin/env python
# coding: utf-8

# In[108]:


# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================
def cout(m, n, i, j):
    m.append(n)
    if(j == 0):
        m.append('None')
    else:
        m.append(i/j)

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '106061245.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
    mycsv = csv.DictReader(csvfile)
    header = mycsv.fieldnames
    for row in mycsv:
        if(row['PRES'] != '-99.000' and row['PRES'] != '-999.000'):
            data.append(row)
        
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

# Retrive ten data points from the beginning.
sum_C0A880 = 0
count_C0A880 = 0
sum_C0F9A0 = 0
count_C0F9A0 = 0
sum_C0G640 = 0
count_C0G640 = 0
sum_C0R190 = 0
count_C0R190 = 0
sum_C0X260 = 0
count_C0X260 = 0
for i in range(len(data)):
    if(data[i]['station_id'] == 'C0A880'):
        sum_C0A880 = sum_C0A880 + float(data[i]['PRES'])
        count_C0A880+=1
    if(data[i]['station_id'] == 'C0F9A0'):
        sum_C0F9A0 = sum_C0F9A0 + float(data[i]['PRES'])
        count_C0F9A0+=1        
    if(data[i]['station_id'] == 'C0G640'):
        sum_C0G640 = sum_C0G640 + float(data[i]['PRES'])
        count_C0G640+=1        
    if(data[i]['station_id'] == 'C0R190'):
        sum_C0R190 = sum_C0R190 + float(data[i]['PRES'])
        count_C0R190+=1        
    if(data[i]['station_id'] == 'C0X260'):
        sum_C0X260 = sum_C0X260 + float(data[i]['PRES'])
        count_C0X260+=1  

output = []
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []

cout(list1, 'C0A880', sum_C0A880, count_C0A880)
cout(list2, 'C0F9A0', sum_C0F9A0, count_C0F9A0)
cout(list3, 'C0G640', sum_C0G640, count_C0G640)
cout(list4, 'C0R190', sum_C0R190, count_C0R190)
cout(list5, 'C0X260', sum_C0X260, count_C0X260)

output.append(list1)
output.append(list2)
output.append(list3)
output.append(list4)
output.append(list5)
output.sort()
print(output)


# In[ ]:



