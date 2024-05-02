#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import plotly.colors as colors
pio.templates.default = "plotly_white"


# In[7]:


data = pd.read_csv(r'C:\Users\RAJESH KUMAR\Desktop\Python projects\Store Sales & Profit (Python)\Sample - Superstore.csv', encoding ='unicode_escape')


# In[8]:


data.shape


# In[9]:


data.head()


# In[11]:


#Looking at descriptive statistics of data 
print(data.head()) 


# In[ ]:


#The dataset has an order date column. We can use this column to create new columns like order month, order year, and order day,
which can be very valuable for sales and profit analysis according to time periods. 
Now we will add this columnb:


# In[23]:


data['Order Date'] = pd.to_datetime(data['Order Date'])
data['Ship Date'] = pd.to_datetime(data['Ship Date']) 

data['Order Month'] = data['Order Date'].dt.month 
data['Order Year'] = data['Order Date'].dt.year
data['Order Day of Week'] = data['Order Date'].dt.dayofweek

data.describe()


# In[13]:


#find monthly sales 
sales_by_month = data.groupby('Order Month')['Sales'].sum().reset_index()
fig = px.line(sales_by_month, 
              x='Order Month', 
              y='Sales', 
              title='Monthly Sales Analysis')
fig.show()


# In[16]:


#find the Sales by Category

sales_by_category = data.groupby('Category')['Sales'].sum().reset_index()


fig = px.pie(sales_by_category, 
             values='Sales', 
             names='Category', 
             hole=0.5, 
             color_discrete_sequence=px.colors.qualitative.Pastel)

fig.update_traces(textposition='inside', textinfo='percent+label')
fig.update_layout(title_text='Sales Analysis by Category', title_font=dict(size=24))

fig.show()


# In[19]:


#Now let's find sales by sub-category

sales_by_subcategory = data.groupby('Sub-Category')['Sales'].sum().reset_index()
fig = px.bar(sales_by_subcategory, 
             x='Sub-Category', 
             y='Sales', 
             title='Sales Analysis by Sub-Category')
fig.show()


# In[27]:


#Now calculate the monthly profit

profit_by_month = data.groupby('Order Month')['Profit'].sum().reset_index()
fig = px.line(profit_by_month, 
              x='Order Month', 
              y='Profit', 
              title='Monthly Profit Analysis')
fig.show()


# In[32]:


#Now calculate profit by Sub-category

profit_by_category = data.groupby('Category')['Profit'].sum().reset_index()

fig = px.pie(profit_by_category, 
             values='Profit', 
             names='Category', 
             hole=0.5, 
             color_discrete_sequence=px.colors.qualitative.Pastel)

fig.update_traces(textposition='inside', textinfo='percent+label')
fig.update_layout(title_text='Profit Analysis by Category', title_font=dict(size=24))

fig.show()


# In[34]:


#Profit analysis by sub-category

profit_by_subactegory = data.groupby('Sub-Category')['Profit'].sum().reset_index()
fig = px.bar(profit_by_subactegory, 
              x='Sub-Category', 
              y='Profit', 
              title='Profit Analysis by Sub-Category')
fig.show()


# In[38]:


#Analysis of Sales & Profit by customer segments
sales_profit_by_segment = data.groupby('Segment').agg({'Sales': 'sum', 'Profit': 'sum'}).reset_index()

color_palette = colors.qualitative.Pastel

fig = go.Figure()
fig.add_trace(go.Bar(x=sales_profit_by_segment['Segment'], 
                     y=sales_profit_by_segment['Sales'], 
                     name='Sales',
                     marker_color=color_palette[0]))
fig.add_trace(go.Bar(x=sales_profit_by_segment['Segment'], 
                     y=sales_profit_by_segment['Profit'], 
                     name='Profit',
                     marker_color=color_palette[1]))

fig.update_layout(title='Sales and Profit Analysis by Customer Segment',
                  xaxis_title='Customer Segment', yaxis_title='Amount')

fig.show()


# In[ ]:


#From the above bar graph we can conclude that there is higher profits from the product sales for consumers, 
#but the profit from corporate product sales is better in the sales-to-profit ratio.
#we can also validate our findings


# In[39]:


#Validation

sales_profit_by_segment = data.groupby('Segment').agg({'Sales': 'sum', 'Profit': 'sum'}).reset_index()
sales_profit_by_segment['Sales_to_Profit_Ratio'] = sales_profit_by_segment['Sales'] / sales_profit_by_segment['Profit']
print(sales_profit_by_segment[['Segment', 'Sales_to_Profit_Ratio']])


# In[ ]:


Analyzing sales and profit data from stores helps businesses figure out where they can do better and make 
smart decisions using that information. 
They can use it to improve how they run their stores, set prices, advertise, and manage their stock. 
This helps them make more money and grow their business.

