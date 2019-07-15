SELECT Customers.CustFirstName,
Customers.CustLastName,
RD.OrderDate, RD.ProductName,
 RD.QuantityOrdered, RD.QuotedPrice
FROM Customers
INNER JOIN
(SELECT Orders.CustomerID, Orders.OrderDate, 
Products.ProductName, 
Order_Details.QuantityOrdered, 
Order_Details.QuotedPrice
FROM ((Orders 
INNER JOIN Order_Details
ON Orders.OrderNumber =
Order_Details.OrderNumber) 
INNER JOIN Products
ON Order_Details.ProductNumber
= Products.ProductNumber) 
WHERE Products.ProductNumber = 10 and Products.ProductName like '%Bike') 
AS RD 
ON Customers.CustomerID = RD.CustomerID
