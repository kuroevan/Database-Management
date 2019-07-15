SELECT Customers.CustomerID,
Customers.CustFirstName,
Customers.CustLastName
FROM Customers
WHERE EXISTS
(SELECT *
FROM (Orders
INNER JOIN Order_Details
ON Orders.OrderNumber =
Order_Details.OrderNumber)
INNER JOIN Products
ON Products.ProductNumber =
Order_Details.ProductNumber
WHERE Products.ProductName LIKE '%Bike'
AND Orders.CustomerID =
Customers.CustomerID)
AND NOT EXISTS
(SELECT *
FROM (Orders
INNER JOIN Order_Details
ON Orders.OrderNumber =
Order_Details.OrderNumber)
INNER JOIN Products
ON Products.ProductNumber =
Order_Details.ProductNumber
WHERE Products.ProductName LIKE '%Helmet'
AND Orders.CustomerID =
Customers.CustomerID)