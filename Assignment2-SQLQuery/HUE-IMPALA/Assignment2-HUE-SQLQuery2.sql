/* Query2: 1 sort (Order By) clause, 1 Group By clause and 1 AVG operation */

/* Query to get average of total profit, regionwise, order by region and total profit*/
SELECT region, AVG(totalprofit) FROM `100salesrecords` GROUP BY region ORDER BY region, AVG(totalprofit)
