#!/usr/bin/env python
# coding: utf-8

# Importing required libraries 

# In[30]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 


# In[31]:


train_data=pd.read_excel('/Users/devansh/Desktop/Study material/Data Science/Data_Train.xlsx')


# printing all the values presentin the data set

# In[32]:


train_data.head()


# Checking for data with missing value

# In[33]:


train_data.isna().sum()


# Dropping the data with missing values

# In[34]:


train_data.dropna(inplace=True)


# checking for the data types present in tha data

# In[35]:


train_data.dtypes


# function to replace the object data type with the date time data type to make it easier for compiuter to understand

# In[36]:


def change_into_datetime(col):
    train_data[col]=pd.to_datetime(train_data[col])


# Printing all the coluymns in the dataset

# In[37]:


train_data.columns


# using a loop for easy conversion of data types

# In[38]:


for i in ['Date_of_Journey','Dep_Time', 'Arrival_Time']:
    change_into_datetime(i)


# Checking if the operation performed is successful or not

# In[39]:


train_data.dtypes


# Converting date of journey to month and day format for easy computing

# In[40]:


train_data['journey_day']=train_data['Date_of_Journey'].dt.day
train_data['journey_month']=train_data['Date_of_Journey'].dt.month
train_data.drop('Date_of_Journey',axis=1,inplace=True)


# Checking if operation performed are successful or not

# In[41]:


train_data.head()


# Creating function to change Arrival time and departure time to hour and minute format

# In[42]:


def change_to_hour(df,col):
    df[col+'_hour']=df[col].dt.hour
def change_to_minute(df,col):
    df[col+'_minute']=df[col].dt.minute
def drop_columns(df,col):
    df.drop(col,axis=1,inplace=True)


# creating a for loop for saving time

# In[43]:


for i in ['Dep_Time', 'Arrival_Time']:
    change_to_hour(train_data,i)
    change_to_minute(train_data,i)
    drop_columns(train_data,i)


# Checking if the data has been modified or not

# In[44]:


train_data.head()


# In[45]:


duration=list(train_data['Duration'])


# In[46]:


for i in range(len(duration)):
    if len(duration[i].split(' '))==2:
        pass
    else:
        if 'h' in duration[i]:
            duration[i]=duration[i]+' 0 min'
        else:
            duration[i]='0 h '+ duration[i]


# In[47]:


train_data['Duration']=duration


# In[48]:


train_data.head()


# Splittiing the duration in hours and minute

# In[51]:


def hour(x):
    return x.split(' ')[0][0:-1]

def minute(x):
    return x.split(' ')[1][0:-1]


# In[52]:


train_data['Duration_hour']=train_data['Duration'].apply(hour)


# In[53]:


train_data['Duration_min']=train_data['Duration'].apply(minute)


# dropping/deleting the duration column

# In[24]:


train_data.drop('Duration',axis=1,inplace=True)


# printing the value to check if the function applied worked or not

# In[25]:


train_data.head()


# Changing the data type of Duration hour and minute to int as they are stored in object data type

# In[26]:


train_data.dtypes


# In[27]:


train_data['Duration_hour']=train_data['Duration_hour'].astype(str)


# In[28]:


train_data.dtypes


# In[29]:


train_data['Duration_hour']=train_data.Duration_hour.astype(int)


# In[ ]:




