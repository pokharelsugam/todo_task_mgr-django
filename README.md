# Django Todo Task Manager

Simple task Manager built with Django

## Features

- View Task, Add Task, Edit Task, Delete Task with task name, description and status

## Project Structure


<pre><code>
.
└── todo-task-mgr-django
    ├── env
    ├── taskmanager 
    │   ├── __pycache__
    │   ├── migrations
    │   ├── static
    │   │   └── css
    │   │       └── styles.css
    │   ├── templates
    │   │   ├── index.html
    │   │   ├── add-task.html
    │   │   └── edit-task.html
    │   ├── __init__.py
    │   ├── views.py
    │   ├── models.py
    │   ├── admin.py
    │   ├── urls.py
    │   ├── tests.py
    │   └── apps.py
    ├── TTM
    │   ├── __pycache__
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── manage.py
    └── db.sqlite3
    </code></pre>

## Getting Started

### Prerequisites

- Python 3.6+
- Django 3.2+
- Git

### Installation

1. Install Python
2. Install Django
   <pre><code>
   pip install django
   </code></pre>
4. Install Virtual Environment
   <pre><code>
   pip install virtualenv
   </code></pre>
6. Clone the repository
   <pre><code>
   git clone https://github.com/pokharelsugam/todo_task_mgr-django.git
   cd todo_task_mgr-django
   </code></pre>
8. Create a virtual environment and activate it.
   <pre><code>
   virtualenv env
   env\scripts\activate
   pip install django
   </code></pre>
10. Run the migrations
    <pre><code>
    python manage.py makemigrations #may or may not be required
    python manage.py migrate	#must be required
    </code></pre>
12. Create a superuser
    <pre><code>
    python manage.py createsuperuser
    </code></pre>
14. Start the development server
    <pre><code>
    python manage.py runserver
    </code></pre>    

## Usage
<ul>
<li>Navigate to http://127.0.0.1:8000/admin to access the admin interface and manage your ims data.</li>
<li>Add New Task</li>
<li>Edit Task</li>
<li>Delete Task</li>
</ul>
