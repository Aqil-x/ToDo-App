# Python To-Do Application

A command-line To-Do application built with Python that allows users to create, view, and delete tasks. The application uses local file storage to retain tasks between sessions.

This project demonstrates Python programming fundamentals, user input handling, file management, control flow, and basic application design.

## Features

* Add new tasks
* View all current tasks
* Delete existing tasks
* Automatically save tasks to a local file
* Load previously saved tasks when the application starts
* Simple command-line interface

## Technologies Used

* **Python 3**
* **File I/O** – Used to store and retrieve tasks
* **Git & GitHub** – Version control and project management

## How It Works

When the application starts, it checks the local task data file and loads any previously saved tasks.

Users can then select an option from the menu to:

1. View their current tasks
2. Add a new task
3. Delete a task
4. Exit the application

Any changes made to the task list are saved locally so that tasks can be accessed again when the application is restarted.

## Getting Started

### Prerequisites

You will need:

* Python 3.x
* A terminal or command prompt

You can check whether Python is installed by running:

```bash
python --version
```

### Installation

Clone the repository:

```bash
git clone https://github.com/Aqil-x/Python-ToDo-Application.git
```

Navigate into the project:

```bash
cd Python-ToDo-Application
```

Run the application:

```bash
python main.py
```

## Project Structure

```text
Python-ToDo-Application/
│
├── main.py
├── .gitignore
└── README.md
```

The task data file is generated locally by the application and is excluded from the Git repository using `.gitignore`.

## Example

When the application is launched, users are presented with a menu allowing them to manage their tasks.

```text
1. View Tasks
2. Add Task
3. Delete Task
4. Exit
```

Users can select an option and follow the prompts to manage their task list.

## What I Learned

Through this project, I developed experience with:

* Python programming fundamentals
* Functions and program structure
* Lists and data handling
* Conditional statements and loops
* User input validation
* Reading and writing files
* Building a command-line application
* Using Git and GitHub for version control

## Future Improvements

Planned improvements for the application include:

* Task completion status
* Task priorities
* Due dates
* Task categories
* Search and filtering
* Improved input validation
* Automated unit tests
* A graphical user interface
* Database-based task storage

## Author

**Aqil Ahmed**

BSc (Hons) Computer Science
University of Salford

GitHub: [Aqil-x](https://github.com/Aqil-x)
