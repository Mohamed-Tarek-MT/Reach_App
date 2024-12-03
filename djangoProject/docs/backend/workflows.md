# Backend Workflows

This section details key workflows in the backend.

### **1. User Registration and Authentication**
- **Endpoints**:
  - `/signup/`: Creates a new user account.
  - `/login/`: Authenticates existing users.
  - `/logout/`: Logs out a user.
- **Related Views**: `signup`, `login_view`, `logout_view`

### **2. Post Management**
- **Endpoints**:
  - `/create_post/`: Allows users to create a new post.
  - `/delete_post/<post_id>/`: Deletes a user’s post.
- **Related Views**: `create_post`, `delete_post`

### **3. Interactions**
- **Endpoints**:
  - `/like_post/<post_id>/`: Allows users to like/unlike a post.
  - `/add_comment/<post_id>/`: Adds a comment to a post.
- **Related Views**: `like_post`, `add_comment`

### **4. Notifications**
- **Endpoint**: `/notifications/`
- **Description**: Displays likes and interactions on a user's posts.
- **Related View**: `notifications`
