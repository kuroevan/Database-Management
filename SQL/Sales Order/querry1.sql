SELECT Customers.CustomerID,
Customers.CustFirstName,
Customers.CustLastName
FROM Customers
WHERE NOT EXISTS
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
WHERE Products.ProductName LIKE '%Tire'
AND Orders.CustomerID =
Customers.CustomerID)