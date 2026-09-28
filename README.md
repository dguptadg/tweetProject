# Django Tweet Project

A simple Django-based social media application that allows users to register, log in, create tweets with images, edit tweets, and delete tweets through a clean web interface.

## Features

- User registration, login, and logout
- Create tweets with text and image uploads
- View all tweets on the home page
- Edit existing tweets
- Delete tweets with a confirmation page
- Authentication-protected create, update, and delete operations
- Django template-based frontend with Bootstrap styling
- Local media handling for uploaded tweet images

## Tech Stack

- Python
- Django
- HTML
- Bootstrap
- SQLite
- Git and GitHub

## Screenshots

### Tweet Home Page

<img width="1402" height="672" alt="Screenshot 2026-09-28 182034" src="https://github.com/user-attachments/assets/d4b2805a-19d8-40c3-8257-a61e7fd2f8b5" />

### Delete Tweet Confirmation

<img width="1403" height="566" alt="Screenshot 2026-09-28 182056" src="https://github.com/user-attachments/assets/c868f356-7ad7-466b-a74c-925d3fcd2cb9" />

## Project Structure

```text
tweet/
├── manage.py
├── media/
├── static/
├── templates/
│   ├── layout.html
│   └── registration/
│       ├── login.html
│       ├── logout.html
│       └── register.html
├── tweet/
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── tweetapp/
    ├── migrations/
    ├── templates/
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── models.py
    ├── urls.py
    └── views.py
```

## Main Application Flow

1. Users can register and log in to the application.
2. Authenticated users can create tweets containing text and an image.
3. Tweets are displayed on the main tweet page.
4. Existing tweets can be edited through a Django form.
5. Tweets can be deleted after confirmation.
6. Users can log out through Django's authentication system.

## Django Concepts Used

- URL routing
- Function-based views
- Django models
- Model forms
- Templates and template inheritance
- User authentication
- `login_required`
- CSRF protection
- File and image uploads
- Database migrations
- CRUD operations

## Repository Note

Sensitive configuration files and local development files are intentionally excluded from GitHub through `.gitignore`, including the virtual environment, local database, media uploads, and private settings.

## Future Improvements

- Improve UI and responsive design
- Add user profiles
- Add likes and comments
- Add tweet search
- Add pagination
- Deploy the application using a production database and cloud storage
