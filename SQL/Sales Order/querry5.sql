SELECT vendors.VendorID, vendors.VendName
FROM vendors
WHERE EXISTS
(SELECT *
FROM (product_vendors
INNER JOIN products
ON product_vendors.ProductNumber =
products.ProductNumber)
INNER JOIN categories
ON products.CategoryID =
categories.CategoryID
WHERE categories.CategoryDescription='Accessories' or categories.CategoryDescription='Clothing' or categories.CategoryDescription='Car racks'
AND product_vendors.VendorID = vendors.VendorID)