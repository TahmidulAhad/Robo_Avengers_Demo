# Robo Avengers Club Project

## Overview
The Robo Avengers project is designed to manage club members, components, and funding efficiently. This Django-based web application allows users to enter and manage member information, track components used in projects, and oversee funding activities.

## Project Structure
The project is organized into several key directories and files:

- **manage.py**: Command-line utility for managing the Django project.
- **robo_avengers/**: Contains the main Django project files including settings, URLs, and WSGI configuration.
- **members/**: Manages club members, including models, views, and templates for member entry and listing.
- **components/**: Handles components used in projects, with similar structure to the members app.
- **funding/**: Manages funding information, including forms and views for funding entry and listing.
- **templates/**: Contains base templates for the project.
- **static/**: Holds static files such as CSS for styling the application.
- **sql/**: Contains SQL scripts for initializing the MySQL database.
- **.env.example**: Example environment variables for configuration.
- **.gitignore**: Specifies files to ignore in version control.
- **requirements.txt**: Lists required Python packages for the project.

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd robo_avengers
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up the database:
   - Configure your MySQL database settings in `robo_avengers/settings.py`.
   - Run the SQL initialization script located in `sql/mysql_init.sql`.

5. Apply migrations:
   ```
   python manage.py migrate
   ```

6. Create a superuser to access the admin panel:
   ```
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```
   python manage.py runserver
   ```

## Usage
- Access the application at `http://127.0.0.1:8000/`.
- Use the admin panel to manage members, components, and funding.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License.