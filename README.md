# 🎓 Student Management System

A web-based **Student Management System** developed using **Python and Django**. This project is designed to manage student information and provides CRUD operations for adding, viewing, updating, and deleting student records.

The project also includes **Course Management** and **Attendance Management** models, along with basic Home, About, and Contact pages.

---

## 📌 Project Overview

The **Student Management System** is a Django-based web application created to understand and implement the fundamentals of web development using the Django framework.

The application allows users to manage student records through a simple interface and demonstrates how Django handles:

* Models
* Views
* Forms
* Templates
* URL routing
* Database operations
* CRUD functionality
* Django migrations

---

## ✨ Features

### 👨‍🎓 Student Management

The system provides the following student management operations:

* ➕ Add a new student
* 📋 View all students
* ✏️ Edit student information
* 🗑️ Delete student records
* 💾 Store student information in the database
* 🔍 Retrieve student records from the database

Student information includes:

* Name
* Email
* Mobile Number
* City

---

### 📚 Course Management

The project includes a Course model with information such as:

* Course Name
* Course Code
* Start Date
* End Date
* Faculty Name
* Active/Inactive Status

Course codes are uniquely maintained in the database.

---

### 📝 Attendance Management

The project also includes an Attendance model connected with students.

Attendance supports three statuses:

* ✅ Present
* ❌ Absent
* ⏰ Late

It also stores:

* Student
* Date
* Attendance Status
* Remarks

---

### 🏠 Other Pages

The application also contains basic pages such as:

* Home
* About
* Contact

---

## 🛠️ Technologies Used

| Technology | Purpose                |
| ---------- | ---------------------- |
| Python     | Programming Language   |
| Django     | Web Framework          |
| HTML5      | Frontend Structure     |
| CSS3       | Styling                |
| SQLite     | Database               |
| Git        | Version Control        |
| GitHub     | Source Code Management |

---

## 📂 Project Structure

```text
Django/
│
├── README.md
│
└── myproject/
    │
    ├── manage.py
    ├── db.sqlite3
    │
    ├── myproject/
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── asgi.py
    │   └── wsgi.py
    │
    └── student/
        │
        ├── migrations/
        │   ├── 0001_initial.py
        │   ├── 0002_course.py
        │   ├── 0003_attendance.py
        │   └── __init__.py
        │
        ├── static/
        │   ├── css/
        │   │   └── style.css
        │   └── images/
        │
        ├── templates/
        │   ├── index.html
        │   ├── about.html
        │   ├── contact.html
        │   └── student_crud/
        │       ├── list.html
        │       ├── add.html
        │       └── edit.html
        │
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── forms.py
        ├── models.py
        ├── urls.py
        └── views.py
```

---

## 🗃️ Database Models

### Student Model

The `Student` model stores basic student information.

```text
Student
│
├── Name
├── Email
├── Mobile
└── City
```

### Course Model

The `Course` model stores course-related information.

```text
Course
│
├── Course Name
├── Course Code
├── Start Date
├── End Date
├── Faculty Name
└── Active Status
```

### Attendance Model

The `Attendance` model records student attendance.

```text
Attendance
│
├── Student
├── Date
├── Status
└── Remarks
```

The Attendance model has a relationship with the Student model using a **ForeignKey**.

---

## 🔄 CRUD Operations

This project demonstrates the four basic CRUD operations.

### Create

Users can add new student records using the student form.

### Read

All students can be displayed from the database.

### Update

Existing student information can be edited.

### Delete

Student records can be removed from the database.

---

## 🧩 Django Components Used

### Models

The project uses Django models to define and manage database tables.

Main models:

```text
Student
Course
Attendance
```

### Views

The application contains views for:

```text
Home
About
Contact
Student List
Add Student
Edit Student
Delete Student
```

### Forms

Django Forms are used for handling student data and validating submitted information.

### URLs

Django URL routing connects application URLs with their corresponding views.

Example:

```python
from django.urls import path
from . import views

urlpatterns = [
    # Application URLs
]
```

### Templates

HTML templates are used to display the application pages and student information.

---

## ⚙️ Installation and Setup

Follow the steps below to run this project on your computer.

### 1. Clone the Repository

```bash
git clone https://github.com/devanshisha2112/Django.git
```

### 2. Open the Project Directory

```bash
cd Django
```

Then move into the Django project folder:

```bash
cd myproject
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
source venv/bin/activate
```

### 5. Install Django

```bash
pip install django
```

If a `requirements.txt` file is added to the project in the future, you can install dependencies using:

```bash
pip install -r requirements.txt
```

### 6. Apply Migrations

Run:

```bash
python manage.py makemigrations
```

Then:

```bash
python manage.py migrate
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

The application will be available at:

```text
http://127.0.0.1:8000/
```

---

## 🖥️ Application Pages

The application includes pages for:

### Home Page

Displays the main application information.

### Student List

Displays all student records stored in the database.

### Add Student

Allows users to add a new student.

### Edit Student

Allows users to modify existing student information.

### Delete Student

Allows users to remove a student record.

### About

Provides information about the application.

### Contact

Provides the contact page.

---

## 📸 Screenshots

Screenshots can be added here to showcase the application.

Example:

```markdown
## 📸 Screenshots

### Home Page
![Home Page](screenshots/home.png)

### Student List
![Student List](screenshots/student-list.png)

### Add Student
![Add Student](screenshots/add-student.png)

### Edit Student
![Edit Student](screenshots/edit-student.png)
```

---

## 🎯 Learning Objectives

This project helped in understanding and practicing:

* Python programming
* Django framework
* Django project structure
* Django application structure
* URL routing
* Django Views
* Django Models
* Django Forms
* HTML Templates
* Static Files
* Database integration
* SQLite database
* CRUD operations
* ForeignKey relationships
* Django migrations
* Git and GitHub

---

## 🔮 Future Enhancements

The project can be extended with the following features:

* 🔐 User authentication and login
* 👤 Student registration
* 📊 Student dashboard
* 📚 Complete course management interface
* 📝 Complete attendance management interface
* 📈 Attendance percentage calculation
* 🔎 Search and filter students
* 📄 Generate student reports
* 📧 Email notifications
* 📱 Improved responsive design
* 👨‍🏫 Faculty management
* 📊 Dashboard with statistics

---

## 🤝 Contributing

Contributions are welcome.

To contribute:

1. Fork this repository
2. Create a new branch
3. Make your changes
4. Commit your changes
5. Push your branch
6. Create a Pull Request

---

## 📄 License

This project is created for **educational and learning purposes**.

---

## 👩‍💻 Author

**Devanshi Shah**

BSc IT Student

GitHub:
https://github.com/devanshisha2112

---

## ⭐ Acknowledgement

This project was developed as part of learning and practicing **Python Django web development**.

If you find this project useful, consider giving the repository a ⭐ star.

