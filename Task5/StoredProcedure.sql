-- Blog posts management
USE BlogDB_LTT

GO

CREATE PROCEDURE ManagePosts(
	@Action varchar(20),
	@PostID int,
	@UserID int,
	@CommentID int,
	@Title varchar(255),
	@PostContent text,
	@CommentContent text
)
AS
BEGIN
	IF @Action = 'addPost'
		INSERT INTO [dbo].[Post] (ID, Title, Content, UserID, CreatedAt) VALUES (@PostID, @Title, @PostContent, @UserID, GETDATE()) 

	ELSE IF @Action = 'getPost'
		SELECT * FROM [dbo].[Post] WHERE ID = @PostID

	ELSE IF @Action = 'editPost'
		UPDATE [dbo].[Post]
		SET Title = @Title, Content = @PostContent
		WHERE ID = @PostID

	ELSE IF @Action = 'deletePost'
		DELETE FROM [dbo].[Post] WHERE ID = @PostID

	ELSE IF @Action = 'addComment'
		INSERT INTO [dbo].[Comment] (ID, PostID, UserID, Content, CreatedAt) VALUES (@CommentID, @PostID, @UserID, @CommentContent, GETDATE()) 

	ELSE IF @Action = 'getComment'
		SELECT * FROM [dbo].[Comment]
		WHERE PostID = @PostID AND UserID = @UserID

	ELSE IF @Action = 'editComment'
		UPDATE [dbo].[Comment]
		SET Content = @CommentContent
		WHERE ID = @CommentID

	ELSE IF @Action = 'deleteComment'
		DELETE FROM [dbo].[Comment]
		WHERE ID = @CommentID

	ELSE IF @Action = 'fetchPostRelatedData'
		SELECT P.Title, P.Content, P.UserID, P.CreatedAt AS 'Posted At', C.Content, C.CreatedAt  AS 'Commented At'
		FROM [dbo].[Post] P, [dbo].[Comment] C
		WHERE P.ID = @PostID AND P.ID = C.PostID
END

GO

EXEC ManagePosts
	@Action = 'addPost',
	@PostID = 1,
	@UserID = 1,
	@CommentID = NULL,
	@Title = 'News for upcomding updates',
	@PostContent = 'This is the details of the update',
	@CommentContent = NULL

EXEC ManagePosts
	@Action = 'getPost',
	@PostID = 1,
	@UserID = NULL,
	@CommentID = NULL,
	@Title = NULL,
	@PostContent = NULL,
	@CommentContent = NULL

EXEC ManagePosts
	@Action = 'addComment',
	@PostID = 1,
	@UserID = 1,
	@CommentID = 1,
	@Title = NULL,
	@PostContent = NULL,
	@CommentContent = 'Waiting for this update'

EXEC ManagePosts
	@Action = 'addComment',
	@PostID = 1,
	@UserID = 1,
	@CommentID = 2,
	@Title = NULL,
	@PostContent = NULL,
	@CommentContent = 'Amazing'

EXEC ManagePosts
	@Action = 'getComment',
	@PostID = 1,
	@UserID = 1,
	@CommentID = NULL,
	@Title = NULL,
	@PostContent = NULL,
	@CommentContent = NULL

EXEC ManagePosts
	@Action = 'fetchPostRelatedData',
	@PostID = 1,
	@UserID = NULL,
	@CommentID = NULL,
	@Title = NULL,
	@PostContent = NULL,
	@CommentContent = NULL