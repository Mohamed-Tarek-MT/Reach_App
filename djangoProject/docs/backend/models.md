# Backend Models

This section outlines the models used in the backend.

### **1. Post**
- **Fields**:
  - `user`: Links the post to its author.
  - `content`: Text content of the post.
  - `image`: Optional image associated with the post.
  - `created_at`: Timestamp when the post was created.
- **Properties**:
  - `likes_count`: Number of likes on the post.
  - `comments_count`: Number of comments on the post.

### **2. Comment**
- **Fields**:
  - `post`: Links the comment to a post.
  - `user`: Links the comment to its author.
  - `content`: Text content of the comment.
  - `created_at`: Timestamp when the comment was created.

### **3. Like**
- **Fields**:
  - `post`: Links the like to a post.
  - `user`: Links the like to a user.
  - `created_at`: Timestamp when the like was created.
