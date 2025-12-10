# 📚 Student File Management System

A comprehensive student file management system built with **Django**, featuring CRUD operations for managing student records efficiently. This project demonstrates core concepts of web development including database management, form handling, and template rendering.

---

## 🚀 Features

- 📋 View all student records in a clean, organized interface
- ➕ Create new student entries with detailed information
- 🔍 Locate and search for specific student records
- ❌ Delete student records with confirmation
- 📊 Store and manage student data including marksheets
- 🎨 Modern, responsive UI with custom CSS styling
- 💾 SQLite database integration for persistent data storage
- 🔒 Built-in Django admin panel for advanced management

---

## 🧠 What I Learned

- Building full-stack web applications with **Django framework**
- Implementing CRUD operations with Django ORM
- Creating and managing Django models, views, and templates
- Form handling and validation using Django Forms
- Database migrations and schema management
- Static file management for CSS and media files
- URL routing and view-template integration
- Best practices for Django project structure

---

## 📂 Tech Stack

- **Backend**: Django (Python)
- **Database**: SQLite
- **Frontend**: HTML, CSS
- **Forms**: Django Forms
- **Template Engine**: Django Template Language

---

## 📁 Project Structure

```
sfs_project/
├── manage.py
├── sfs.db
├── media/
├── sfs_project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── sfsapp/
    ├── models.py
    ├── views.py
    ├── forms.py
    ├── admin.py
    ├── migrations/
    ├── static/
    │   └── css/
    │       └── mystyle.css
    └── templates/
        ├── home.html
        ├── create.html
        ├── locate.html
        └── delete.html
```

---

## 🛠️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/ritikajaiswal02/Student_file_management_system_Django.git
   cd Student_file_management_system_Django
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # source venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install django
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Open your browser and navigate to `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

---

## 📸 Features Overview

### Home Page
View all student records with complete details at a glance.

### Create Student
Add new student entries with fields for personal and academic information.

### Locate Student
Search and find specific student records quickly.

### Delete Student
Remove student records with proper confirmation flow.

---

## 🎯 Future Enhancements

- 🔐 User authentication and authorization
- 📧 Email notifications for important updates
- 📈 Advanced analytics and reporting features
- 🔄 Export data to CSV/Excel formats
- 📱 Mobile app integration
- 🌐 REST API for third-party integrations
- 🔍 Advanced search and filtering options

---

## 👩‍💻 Author

**Ritika Jaiswal**

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

---

## ⭐ Show your support

Give a ⭐️ if you like this project!
