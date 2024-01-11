CREATE DATABASE BlogDB_LTT

USE BlogDB_LTT

CREATE TABLE [dbo].[User] (
	ID int PRIMARY KEY,
	Username varchar(255),
	Email varchar(255)
)

CREATE TABLE [dbo].[Post] (
	ID int PRIMARY KEY,
	Title varchar(255),
	Content text,
	CreatedAt datetime,
	UserID int

	FOREIGN KEY (UserID) REFERENCES [dbo].[User]([ID])
) 

CREATE TABLE [dbo].[Comment] (
	ID int PRIMARY KEY,
	PostID int,
	UserID int,
	Content text,
	CreatedAt datetime

	FOREIGN KEY (PostID) REFERENCES [dbo].[Post]([ID]),
	FOREIGN KEY (UserID) REFERENCES [dbo].[User]([ID])
)

-- Insert a sample row for User
INSERT INTO [dbo].[User] VALUES (1, 'Cedric', 'cedric@gmail.com')