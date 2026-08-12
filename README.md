# DevTrack 🚀

A simple Django-based project and task management application.

## 📌 About

DevTrack was created while learning Django from scratch. It allows users to register, log in, create projects, and manage tasks inside their projects.

The project demonstrates the basic concepts of building a complete Django web application.

## ✨ Features

- User Registration
- User Login & Logout
- User-specific Projects
- Create Projects
- Edit Projects
- Delete Projects
- Create Tasks
- Task Completion Status
- Django Admin
- SQLite Database
- Authentication & Authorization
- Responsive UI
- Git & GitHub Version Control

## 🛠️ Technologies

- Python
- Django 6.1
- SQLite
- HTML
- CSS
- Git
- GitHub

## 🗄️ Database Structure

```text
User
 │
 └── Projects
       │
       └── Tasks

A user can have multiple projects, and each project can have multiple tasks.

📂 Project Structure
devtrack/
│
├── config/
├── core/
├── screenshots/
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
⚙️ Installation

Clone the repository:

git clone https://github.com/Ahsanmohyuddin/devtrack.git
cd devtrack

Create a virtual environment:

python -m venv venv

Activate it on Windows:

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run migrations:

python manage.py migrate

Start the server:

python manage.py runserver

Open:

http://127.0.0.1:8000/
👨‍💻 Admin

Create a Django superuser:

python manage.py createsuperuser

Then visit:

http://127.0.0.1:8000/admin/
📸 Screenshots

Screenshots of the application are available in the screenshots/ folder.

🎯 Learning Goals

This project helped me learn:

Django project structure
URLs and Views
Templates
Models and Databases
Django ORM
Forms and ModelForms
Authentication
Authorization
CRUD operations
Database relationships
Git and GitHub
🚀 Future Improvements
REST API
PostgreSQL
Better dashboard
Task editing and deletion
Search and filtering
AI integration
Deployment
👤 Author

Ahsanmohyuddin

GitHub:
https://github.com/Ahsanmohyuddin


### Then save it as

```text
devtrack/README.md

Then run:

git add README.md requirements.txt
git commit -m "Add project documentation"
git push

After that, refresh your GitHub repository. The README will automatically appear on the front page.

This is enough for GitHub. Keep the much longer explanation we made separately for your class/project documentation, not inside the repository README.
