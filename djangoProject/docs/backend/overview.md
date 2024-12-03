# Backend Overview

The backend for Reach is built with Django and includes the following key functionalities:

- **User Management**: Handles user authentication, registration, and profiles.
- **Posts and Comments**: Enables users to create, like, and comment on posts.
- **Notifications**: Alerts users of interactions with their posts.
- **Media Management**: Supports uploading and displaying images.

## Key Components
- Models are defined in `models.py` and include `Post`, `Comment`, and `Like`.
- Views handle application logic, such as creating posts or adding comments.
- URLs define routing for all application endpoints.
