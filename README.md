﻿# ToDo List Project

A ToDo List web application built using Django. This project helps users manage their daily tasks with features like task creation, updating, deletion, and marking tasks as completed. 

## Installation

```
git clone https://github.com/haldaniko/ToDoList-DjangoWebsite.git
cd ToDoList-DjangoWebsite

# on macOS
python3 -m venv venv
source venv/bin/activate

# on Windows
python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
   
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata data.json
python manage.py runserver
```

Application will be available at http://127.0.0.1:8000

## Demo
![demo.png](demo.png)
