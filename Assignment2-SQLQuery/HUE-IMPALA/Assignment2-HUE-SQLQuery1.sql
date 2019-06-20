/* Query1: 1 nested (inner) query, 2 Group By clause and 1 SUM operation */

/* Query to get total revenue for online saleschannel, regionwise and itemtypewise*/
SELECT t1.region, t1.itemtype, SUM(t1.totalrevenue) FROM (SELECT * FROM `100salesrecords` WHERE saleschannel = 'Online')t1 GROUP BY t1.region, t1.itemtype 
