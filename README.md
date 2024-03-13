# Summary

Orange County Lettings is a startup in the real estate rental sector. The startup is in the midst of expanding in the United States.

## Prerequisites

- GitHub account with read access to this repository.
- Git CLI.
- SQLite3 CLI.
- Python interpreter, version 3.6 or higher.
- Git for windows installed (If using windows as OS)
- Docker engin installed in your system. Visite `https://docs.docker.com/engine/install/` for installation procedure.
- A Sentry account with a created project and a `Sentry DSN key`. Visite `https://sentry.io` and `https://docs.sentry.io/product/sentry-basics/integrate-backend/getting-started/` for more details.
- A CircleCI Account with CircleCi project connected to your project repository on `GitHub`, `Gitlab` or `BitBucket`. (Adding the django `SECRET_KEY`, `SENTRY_DSN`, `DOCKERHUB_USER`, `$DOCKERHUB_PASS` and `$TAG` with the value `CIRCLE_SHA1_LATEST` to the circleci environment variables). Visite `https://circleci.com` and `https://circleci.com/docs/` for more details.
- A Docker Account with Docker `username` for `$DOCKERHUB_USER` and `password` for `$DOCKERHUB_PASS` added as environment variables for `Docker HUB` access. Visite `https://www.docker.com/`.
- A Render Account (with Web service created for the Docker HUB main image after creating and pushing this image) and adding `SECRET_KEY` and `SENTRY_DSN` as environment variables. Visite `https://www.render.com`

## Local Development

Throughout the rest of the local development documentation, it is assumed that the `python` command in your OS shell executes the above Python interpreter (unless a virtual environment is activated).

Works on macOS / Linux / or windows git bash :

### Clone the repository

You can fork the project from `https://github.com/Abdelhz/da_python_p13_v2.git` to you own github repository

- Create a new folder for the project :

```bash
mkdir oc_lettings_project
cd oc_lettings_project
```

clone the project from your own github repository after forking it from `https://github.com/Abdelhz/da_python_p13_v2.git`

```bash
git clone "Your own Github repository"
```

OR :

```bash
git clone https://github.com/Abdelhz/da_python_p13_v2.git
```

Then you have to push this project to your own repository.

### Create the virtual environment

Enter the parent directory :

```bash
cd /path/to/oc_lettings_project
```

Create the python virtual environment :

```bash
python -m venv env_oc_lettings_project
```

activate virtual environment :

```bash
source env_oc_lettings_project/Scripts/activate
```

Install dependencies :

```bash
pip install -r da_python_p13_v2/requirements.txt
```

Deactivate the virtual environment (if needed) :

```bash
source env_oc_lettings_project/Scripts/deactivate
```

### Run the site

activate virtual environment :

```bash
source env_oc_lettings_project/Scripts/activate
```

Enter the project root directory :

```bash
cd /path/to/da_python_p13_v2
```

#### Generate a new django SECRET_KEY

Enter django shell :

```bash
python manage.py shell
```

Generate a new django secret key (in the shell) :

```python
import secrets
print(secrets.token_hex(24))
```

Copy the secret key then exit the shell with :

```python
exit()
```

Export the django SECRET_KEY and the sentry DSN :

```bash
export SECRET_KEY='your_new_secret_key'
export SENTRY_DSN='your_sentry_dsn_here'
```

Make the migrations before running the django application (if needed) :

```bash
python manage.py makemigrations
python manage.py migrate
```

Run the Django application :

```bash
python manage.py runserver
```

Access the django application from browser

- Go to `http://localhost:8000` in a browser.
- Confirm that the site works and is navigable (you should see several profiles and locations).

#### Linting

```bash
cd /path/to/da_python_p13_v2
source env_oc_lettings_project/Scripts/activate
flake8
```

#### Tests & coverage

```bash
cd /path/to/da_python_p13_v2
source env_oc_lettings_project/Scripts/activate
pytest
```

#### Database

```bash
cd /path/to/da_python_p13_v2
flake8
```

Open a shell session :

```bash
sqlite3
```

Connect to the database :

```bash
.open oc-lettings-site.sqlite3
```

Display tables in the database :

```bash
.tables
```

Display columns in the profiles table :

```bash
pragma table_info(Python-OC-Lettings-FR_profile);
```

Run a query on the profiles table :

```bash
select user_id, favorite_city from Python-OC-Lettings-FR_profile where favorite_city like 'B%';
```

Exit :

```bash
.quit
```

#### Admin panel

- Go to `http://localhost:8000/admin`
- Log in with user `admin`, password `Abc1234!`

# BUILDING AND DEPLOYING

## Local Docker Running

In the project root directory the `docker_local_commands.sh` does the following when ran :

- Build the docker image.
- Push the docker image to the docker HUB.
- Pull back the Image from the docker HUB.
- Run locally the docker image.

In order to use this file you need to modify it as following :

- Open the file `docker_local_commands.sh` in editor;
- Replace the `Your username` in `DOCKERHUB_USER="Your username"` with you actual Docker `username`;
- Replace the `Your password` in `DOCKERHUB_PASS="Your password"` with you actual Docker `password`;
- Replace the `Your secret key` in `SECRET_KEY="Your secret key"` with you actual Django `secret key` that you generated before;
- Replace the `Your secret key` in `SENTRY_DSN="Your SENTRY_DSN key"` with you actual Sentry `DNS key` that you get from your sentry project on sentry website;

After setting up the `docker_local_commands.sh`

Run this command from terminal in the project root directory :

```bash
bash docker_local_commands.sh
```

- On a browser go to `http://localhost:8000/` to access the locally ran website.

## Online deployment

After doing the following :

- Creating and setting up a CircleCi and project with your github project and the needed environment variables.
- Creating and setting up a docker account
- Creating an Render account and new web service linked to your main image in docker hub.

### Deployment RUN

- Add the `URL` given by your `Render Web Service` to the `ALLOWED_HOSTS` list in your `settings.py`.
- After adding the `Render web service URL`, simply commit your code and push it to your github (the one linked to your CircleCI Pipeline), the pipeline will do the work
- Visite the `URL` given by your `Render Web Service`.

### Environment variables to SETUP

#### CircleCI environment variables

| Name                     | Value                        | Description |
| ------------------------ | ---------------------------- | ----------- |
| DOCKERHUB_PASS           | `Your Docker username`       | This is the username from the Docker account credentials            |
| DOCKERHUB_USER           | `Your Docker password`       | This is the password from the Docker account credentials             |
| RENDER_DEPLOY_HOOK_URL   | `Your render web service hook` | Obtained from the render web service settings page after creating the render web service and linking it to your docker image from docker hub. |
| SECRET_KEY               | `Your django secret key`     | Generated earlier |
| SENTRY_DSN               | `Your Sentry DSN key`        | Obtained from sentry website in your project |
| TAG                      | `Your main image TAG`        | The custom tag you chose for the main image |

The CircleCI pipeline defined by the config.yml file has 3 main job executed in the workflows :

| Job Name              | Requires           | Branch Filters |
| --------------------- | ------------------ | -------------- |
| build_and_testing_Suite | None               | Every branch          |
| containerize          | build_and_testing_Suite | Only master branch   |
| deploy                | containerize       | Only master branch    |
