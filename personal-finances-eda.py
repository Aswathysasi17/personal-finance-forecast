#!/usr/bin/env python
# coding: utf-8

# # Personal Finance EDA

# In[1]:


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns

from plotly.subplots import make_subplots
import plotly.graph_objects as go


# In[2]:


datos = pd.read_csv('/kaggle/input/personal-finance/personal_transactions.csv')
datos.Date = pd.to_datetime(datos.Date)


# In[3]:


datos.head()


# In[4]:


datos.info()


# ## Debits Analysis

# In[5]:


debits = datos[datos["Transaction Type"] == 'debit']


# In[6]:


def count_sum(data ,column: str, plot = "Pie"):
    by_column = data                .groupby(column)                .agg({"Transaction Type": "count", "Amount": "sum"})                .rename(columns={"Transaction Type": "Total"})                .reset_index()
    by_column.columns = [column, "Total", "Sum"]
    
    labels = by_column[column]

    fig = None
    
    if plot == 'Pie':
        fig = make_subplots(1, 2, specs=[[{'type':'domain'}, {'type':'domain'}]],
                    subplot_titles=['Sum', 'Total'])
        fig.add_trace(
            go.Pie(
                labels=labels,
                values=by_column["Sum"],
                name="Sum"
            ),
        1, 1)
        fig.add_trace(
            go.Pie(
                labels=labels,
                values=by_column["Total"],
                name="Total"
            ),
        1, 2)
    elif plot == 'Scatter':
        fig = make_subplots(1, 2,
                    subplot_titles=['Sum', 'Total'])
        fig.add_trace(
            go.Scatter(
                x=labels,
                y=by_column["Sum"],
                name="Sum"
            ),
        1, 1)
        fig.add_trace(
            go.Scatter(
                x=labels,
                y=by_column["Total"],
                name="Total"
            ),
        1, 2)
        

    fig.update_layout(title_text=f"{column} Analysis")
    fig.show()
    
    return by_column


# ### ¿Cómo se reparten mis gastos según categoría? - Debits by Category?

# In[7]:


gastos_by_cat = count_sum(debits, "Category")
gastos_by_cat


# ### ¿Cúales son mis medios de pago favoritos? - Debits by Payment Account?

# In[8]:


gastos_by_payment_way = count_sum(debits, "Account Name")
gastos_by_payment_way


# ### Total \$ Gastos por fecha 

# In[9]:


gastos_by_date = count_sum(debits, "Date", plot="Scatter")
gastos_by_date


# ## Income Analysis

# In[10]:


credits = datos[datos["Transaction Type"] == 'credit']


# ### Income by Account?

# In[11]:


income_by_account = count_sum(credits, "Account Name")
income_by_account


# In[ ]:





#  
