
# coding: utf-8

# In[2]:


from sqlalchemy import create_engine
import pandas as pd

# Note: Due to memory issue reduced no.of records to 50 rows
data = pd.read_csv('C:\\PGDDS\\BigData\\50SalesRecords.csv')

# Create the db engine
engine = create_engine('sqlite:///:memory:')

# Store the dataframe as a table
data.to_sql('data_table', engine)

# Query 1 to get total revenue for online saleschannel, regionwise and itemtypewise*/
print('Query 1 to get total revenue for online saleschannel, regionwise and itemtypewise')
res1 = pd.read_sql_query('SELECT t1.region, t1.itemtype, SUM(t1.totalrevenue) FROM (SELECT * FROM data_table WHERE saleschannel = \'Online\')t1 GROUP BY t1.region, t1.itemtype', engine)
print('Result 1')
print(res1)
print('\n----------------------------------------------------------------------------------------\n')


# Query 2 to get average of total profit, regionwise, order by region and total profit
print('Query 2 to get average of total profit, regionwise, order by region and total profit')
res2 = pd.read_sql_query('SELECT region, AVG(totalprofit) FROM data_table GROUP BY region ORDER BY region, AVG(totalprofit)', engine)
print('Result 2')
print(res2)
print('\n----------------------------------------------------------------------------------------\n')

