# deploydemo

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
    - Ensure you have the following files in your repository:
        - `build.sh`: Script to build the project.
        - `runtime.txt`: Runtime configurations.
        - `vercel.json`: Vercel configurations.
          
## Explanation of `build.sh`

The `build.sh` script is used to build the project before deployment. You may need to modify the following lines according to your project's requirements:

```sh
#!/bin/bash
# filepath: /e:/deploydemo/build.sh

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput 
```

## Explanation of `runtime.txt`
The runtime.txt file specifies the Python runtime version to be used by Vercel. This ensures that the correct version of Python is used during deployment. For example:
```sh

python-3.12.4

```

Python version: Ensure the specified Python version matches the version used in your development environment to avoid compatibility issues.

## Explanation of `vercel.json`
The vercel.json file configures the Vercel deployment. You may need to modify the following lines according to your project's requirements:
```sh
{
  "version": 2,
  "builds": [
    {
      "src": "build.sh",
      "use": "@vercel/static-build",
      "config": {
        "distDir": "staticfiles"
      }
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "/staticfiles/$1"
    }
  ]
}
```

builds: Specifies the build script and the output directory. Ensure build.sh is correctly referenced and distDir points to the directory where static files are collected.
routes: Defines routing rules. Modify the src and dest paths according to your project's structure and requirements.