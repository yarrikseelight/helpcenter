# Django Help Center App 🧑‍💻📚

This is a reusable Django app for creating a support/help center, including article management, video embedding, FAQs, and search functionality. The app is designed to be easily integrated into any Django project. 

**📁 Note**: This GitHub repository contains a complete Django project for demonstration purposes.
The reusable app itself is located in the helpcenterapp/ directory — you can copy this folder into your own Django project to integrate the Help Center functionality. 

**📁 Note 2**: The app includes a built-in search bar, but it does not have any search algorithms. Please feel free to implement your own search functionality according to your requirements. 

## Table Of Contents

- [Features](#features-)
- [Installation](#installation-%EF%B8%8F)
    - [Step 1: Copy the App](#step-1-copy-the-app-to-your-project-)
    - [Step 2: Install Dependencies](#step-2-install-dependencies-)
    - [Step 3: Add to Installed Apps](#step-3-add-the-app-to-installed_apps-%EF%B8%8F)
    - [Step 4: Set Up URLs](#step-4-set-up-urls-)
    - [Step 5: Migrate the Database](#step-5-migrate-the-database-%EF%B8%8F)
    - [Step 6: Static and Media URL Patterns](#step-6-add-media-and-static-url-patterns-)
- [Usage](#usage-)
- [Optional Configuration](#optional-configuration-%EF%B8%8F)


## Features 🌟

- **Article Management**: Allows you to create, manage, and display articles 📄.
- **Category and Subcategory System**: Articles are organized into categories and subcategories 🗂️.
- **Video Embedding**: Embed YouTube videos directly into articles 🎥.
- **Rich Text**: Articles support rich text formatting, including bullet points, images, and more ✍️.
- **FAQ Section**: Add frequently asked questions related to each article ❓.
- **Responsive Design**: The app is fully responsive, with layouts that adjust for smaller screens 📱.

---

## Installation ⚙️

### Step 1: Copy the app to your project 📂

1. Copy the `helpcenterapp` folder into your Django project directory.

2. If you haven't already, create a directory for your `media` and `static` files in the root directory of your project.

---

### Step 2: Install dependencies 📦

1. **Rich Text Field**: The app uses the `django-ckeditor` for rich text support. Install it using pip:

    ```bash
    pip install django-ckeditor
    ```

2. **Static and Media Configuration**:
    - Make sure your `settings.py` has proper settings for static and media files. The following settings were used when making this app (you may need to adjust them depending on your project structure):
      ```python
      STATIC_URL = 'static/'
      STATICFILES_DIRS = [BASE_DIR / 'static']
      
      MEDIA_URL = '/uploads/'
      MEDIA_ROOT = BASE_DIR / 'media'
      ```

---

### Step 3: Add the app to `INSTALLED_APPS` ⚙️

In your `settings.py`, add `helpcenterapp` and `ckeditor` to the `INSTALLED_APPS` list:

```python
INSTALLED_APPS = [
    # Other apps...
    'ckeditor',
    'helpcenterapp',
]

```

---
### Step 4: Set up URLs 🔗

In your project's urls.py, include the helpcenterapp URLs. Add the following to the urlpatterns list:

```python
from django.urls import path, include

urlpatterns = [
    # Other URL patterns...
    path('support/', include('helpcenterapp.urls')),
]
```

---
### Step 5: Migrate the Database 🛠️

```python
python manage.py makemigrations helpcenterapp
python manage.py migrate
```

---

---
### Step 6: Add Media and Static URL Patterns 🌐

In your project's urls.py, add the following to serve media files during development (ensure this is only in development):

```python
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## Usage 📝

- **Add Articles**: You can now add articles in the Django admin interface. Each article can include text, video links, and FAQs.
- **Display Articles**: Articles will be automatically displayed on your website based on the URL structure you've set up in the helpcenterapp URLs.

## Optional Configuration 🛠️

- **Customize Templates**: The default templates can be found inside the helpcenterapp/templates/ folder. Feel free to modify them to match your site's theme.
- **Custom Fields**: If you need additional fields in articles, simply extend the Article model and run migrations.

