CREATE DATABASE ECommerceIntentoryDB_LTT

USE ECommerceIntentoryDB_LTT

CREATE TABLE [dbo].[Product] (
	ID int PRIMARY KEY,
	Name varchar(255),
	Description varchar(255),
	Price decimal(19, 0),
	Quantity int,
	ProductType varchar(255),
)

CREATE TABLE [dbo].[Customer] (
	ID int PRIMARY KEY,
	Name varchar(255),
	Phone varchar(15),
	Addres varchar(255)
)

CREATE TABLE [dbo].[Order] (
	ID int PRIMARY KEY,
	CreationDate timestamp,
	CustomerID int

	CONSTRAINT [FK_Order_Customer_CustomerID] FOREIGN KEY([CustomerID])
	REFERENCES [dbo].[Customer] ([ID])
)

CREATE TABLE [dbo].[OrderDetail] (
	OrderID int,
	ProductID int,
	Quantity int,
	Price decimal(19, 0)

	PRIMARY KEY (OrderID, ProductID),
	CONSTRAINT [FK_OrderDetail_Order_OrderID] FOREIGN KEY([OrderID])
	REFERENCES [dbo].[Order] ([ID]),
	CONSTRAINT [FK_OrderDetail_Product_ProductID] FOREIGN KEY([ProductID])
	REFERENCES [dbo].[Product] ([ID])
)

CREATE TABLE [dbo].[InventoryTransaction] (
	ID int PRIMARY KEY,
	CreationDate timestamp
)

CREATE TABLE [dbo].[TransactiondDetail] (
	ProductID int,
	InventoryTransactionID int,
	ImportQuan int,
	ExportQuan int

	PRIMARY KEY (ProductID, InventoryTransactionID),
	CONSTRAINT [FK_TransactiondDetail_Product_ProductID] FOREIGN KEY([ProductID])
	REFERENCES [dbo].[Product] ([ID]),
	CONSTRAINT [FK_TransactiondDetail_InventoryTransaction_InventoryTransactionID] FOREIGN KEY([InventoryTransactionID])
	REFERENCES [dbo].[InventoryTransaction] ([ID])
)