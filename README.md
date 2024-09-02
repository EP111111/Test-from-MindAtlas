# Test-from-MindAtlas

# Course Report

This project is a web application that generates a report of users enrolled in courses, showing their completion status. It uses PHP, MySQL, JavaScript, and CSS to display data in a user-friendly format. The application includes filtering capabilities to search for specific users or courses.

## Features

- Filter users and courses using various criteria.
- Display results in a dynamic table with pagination and search functionality.
- Backend implementation using PHP and MySQL.
- Frontend implementation using Bootstrap for styling, and DataTables for enhanced table features.

## Prerequisites

Before you begin, ensure you have the following installed:

- **PHP** (version 7 or above)
- **MySQL** database server
- **A web server** like Apache (e.g., XAMPP, MAMP)


## Set Up the Database

### Create and Set Up the Database

Save the provided Python script as `setup_database.py` and run it to initialize the database. The script will:

- Create the `stu_enroll` database.
- Create the `Users`, `Courses`, and `Enrolments` tables.
- Insert sample data into the tables.

Run the script using Python:

```bash
python DB_setup.py
```

Ensure you have MySQL running and accessible with the credentials provided in the script (host, user, password).

![image](https://github.com/user-attachments/assets/09af2e78-fd5f-4d81-8198-45038a647573)

## Configure Database Connection
Open data.php and update the database connection settings as follows:

- $host: The hostname of your MySQL server (e.g., localhost).
- $user: The MySQL username (e.g., root).
- $password: The MySQL password (e.g., root).
- $dbname: The name of the database (e.g., stu_enroll).
Ensure these settings match your MySQL server configuration.

## Start the Web Server
Place the project files in the web server’s root directory (e.g., htdocs for XAMPP or MAMP). Start the server, and ensure PHP is enabled.

## Access the Application
Open your web browser and navigate to:

```bash
http://localhost/course.html
```

## Usage
### Filtering Data
Use the form at the top of the page to enter filter criteria:

- Name: Search by user name.
- User ID: Filter by specific user ID.
- Course ID: Filter by specific course ID.

Click the "Filter" button to update the table with the filtered results.

## Technologies Used
- **PHP**: For server-side processing and database queries.
- **MySQL**: As the database to store user and course data.
- **JavaScript/jQuery**: For DOM manipulation and handling Ajax requests.
- **DataTables**: A jQuery plugin for enhancing the HTML table.
- **Bootstrap**: For responsive design and styling.
  
## Viewing Results
The results will be displayed in a table below the form. Columns include:

- User Name: The full name of the user.
- Course Description: The description of the course.
- Completion Status: The status of the enrolment ("not started", "in progress", "completed").

![image](https://github.com/user-attachments/assets/c4a7a42c-1530-4afe-81eb-2f66ab220942)

