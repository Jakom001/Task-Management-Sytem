# Task Management System ✔️
The Task Management System is a web-based application designed to streamline task management within an organization. It provides a centralized platform for creating, assigning, and tracking tasks, enabling teams to collaborate efficiently and enhance productivity.

The Task Management System is made with Python and Django for learning purposes

<a><img src="https://user-images.githubusercontent.com/95726794/212497770-a3e241e7-0c77-4573-9d22-8f0ae813e958.png" width="70%" heigth="70%"></a>
<br></br>
<a><img src="https://user-images.githubusercontent.com/95726794/212497784-80a48617-759c-4415-aa1c-4591b9892c3d.png" width="70%" heigth="70%"></a>

## Table of Contents:
- [Features](#features)
- [Screenshots](#screenshots)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Contributing](#contributing)
- [License](#license)

## Screenshots
[Click Here](screenshots/README.md)
![Login](/images/login.png)
_The login interface allows users to authenticate and access the system._

![Dashboard](/images/dashboard.png)
_The dashboard provides an overview of tasks and their status._

![Task Creation](/images/task-creation.png)

## Features
- Login Page with User authentication
- Dashboard Page with statistics and graphs
- DataTables with print, copy, to CSV, and to PDF buttons

- User-friendly interface for task creation, assignment, and tracking
- Role-based access control (admin, user, ICT staff) with different privileges
- Real-time task status updates and notifications
- Priority and deadline management for effective task prioritization
- Robust reporting and analytics for performance monitoring

- Tickets Management (CRUD)
- Users Management (CRUD)
- Task Management Sytem (TMS)
  - Search and add tickets to list
  - Update tickets
  - Remove tickets from the list
  - Update Item Quantity and Recalculate Total
  - Assign a task to staff members

- User Management
  - List all users
  - User updates

## Tech Stack

- Frontend: HTML, CSS, JavaScript, Boostrap, DataTables,
- Backend: Django, Python, Ajax, SQLite,

## Installation

    To install and run the Task Management System, follow the steps below:

  1. Clone or download the repository:

  ```bash
  ` git clone `https://github.com/Jakom001/Task-Management-Sytem.git`

  2. Go to the project directory

  ` cd cd Task-Management-System`

  3. Create a virtual environment :

  PowerShell:
  ```
   python -m venv venv
   venv\Scripts\Activate.ps1
  ```

  Linux:
  ```
  python3 -m venv venv
  source venv/bin/activate
  ```

  4. Install dependencies:
  ` pip install -r requirements.txt`

  5.  Update pip and setuptools
  ` python -m pip install --upgrade pip setuptools`

  6. Install GTK to create the PDF files:
   [Official documentation](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#installation)

  7. If you have Windows (Important)‼:
    Add GTK to your path variables, suppose you installed GTK at:
    `C:\Program Files\GTK3-Runtime Win64\bin`
    That will be your new path variable

  - [Tutorial add to path variable](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#installation)

  - [If you get an error like cannot load library](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#missing-library)

  8. Restart your computer

## Run it locally

1. Go to the project directory: `cd django_point_of_sale`

2. Make database migrations:
  `python manage.py makemigrations` and
  `python manage.py migrate`

3. Create superuser `python manage.py createsuperuser`

   with the following data: `username: admin,
    password: admin,
    email: admin@admin`

4. Run the server: `python manage.py runserver`

5. Open a browser and go to: `http://127.0.0.1:8000/`

## Contributing

Contributions are always welcome!

- Fork this repository;

- Create a branch with your feature: `git checkout -b my-feature`;

- Commit your changes: `git commit -m "feat: my new feature"`;

- Push to your branch: `git push origin my-feature`.

## Authors
Andrew Peter
petremosh85@gmail.com
- [@jakom001](https://www.github.com/jakom001)

##  License

This project is under [MIT License.](https://choosealicense.com/licenses/mit/)

[Back to top ⬆️](#Task-Management-System-)
