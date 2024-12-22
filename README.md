# deplopydemo# deploydemo

This is a demo of a simple Django CRUD operation app. This app is deployed on Vercel.

## How to Deploy

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd deploydemo
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up the database:
    ```sh
    python manage.py migrate
    ```

5. Create a superuser to access the Django admin:
    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```sh
    python manage.py runserver
    ```

7. Deploy to Vercel:
    - Install the Vercel CLI:
        ```sh
        npm install -g vercel
        ```
    - Link the project to Vercel:
        ```sh
        vercel
        ```
    - Deploy the project:
        ```sh
        vercel --prod
        ```

## Repository Structure

- [dempodeploy](http://_vscodecontentref_/1)
  - `.env`: Environment variables for the project.
  - `build.sh`: Script to build the project.
  - [db.sqlite3](http://_vscodecontentref_/2): SQLite database file.
  - `demoapp/`: Contains the Django app.
    - [__init__.py](http://_vscodecontentref_/3): Initializes the app.
    - `admin.py`: Admin configurations.
    - `apps.py`: App configurations.
    - [migrations/](http://_vscodecontentref_/4): Database migrations.
    - `models.py`: Database models.
    - `signal.py`: Signal handlers.
    - `templates/`: HTML templates.
    - `tests.py`: Unit tests.
    - `urls.py`: URL configurations.
    - `views.py`: View functions.
  - [dempodeploy](http://_vscodecontentref_/5): Contains the project settings.
    - [__init__.py](http://_vscodecontentref_/6): Initializes the project.
    - `asgi.py`: ASGI configurations.
    - `settings.py`: Project settings.
    - `urls.py`: URL configurations.
    - `wsgi.py`: WSGI configurations.
  - `manage.py`: Django management script.
  - `media/`: Media files.
    - `images/`: Image files.
  - `requirements.txt`: Python dependencies.
  - `runtime.txt`: Runtime configurations.
  - `static/`: Static files.
    - `demo.css`: CSS file.
    - `demo.js`: JavaScript file.
  - `staticfiles/`: Collected static files.
  - `vercel.json`: Vercel configurations.
- [README.md](http://_vscodecontentref_/7): Project documentation.
- [venv](http://_vscodecontentref_/8): Virtual environment.