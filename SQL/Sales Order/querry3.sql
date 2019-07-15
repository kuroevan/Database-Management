select order_details.OrderNumber, order_details.ProductNumber, order_details.QuantityOrdered, order_details.QuotedPrice
from order_details inner join products on products.ProductNumber = order_details.ProductNumber
where CategoryID=2 and ProductName not like '%Helmet'