Run the Site
------------

Activate virtual environment:

.. code-block:: bash

   source env_oc_lettings_project/Scripts/activate

Enter the project root directory:

.. code-block:: bash

   cd /path/to/da_python_p13_v2

Generate a New Django SECRET_KEY
--------------------------------

Enter django shell:

.. code-block:: bash

   python manage.py shell

Generate a new django secret key (in the shell):

.. code-block:: python

   import secrets
   print(secrets.token_hex(24))

Copy the secret key then exit the shell with:

.. code-block:: python

   exit()

Export the django SECRET_KEY and the sentry DSN:

.. code-block:: bash

   export SECRET_KEY='your_new_secret_key'
   export SENTRY_DSN='your_sentry_dsn_here'

Make the migrations before running the django application (if needed):

.. code-block:: bash

   python manage.py makemigrations
   python manage.py migrate

Run the Django application:

.. code-block:: bash

   python manage.py runserver

Access the django application from browser:

- Go to `<http://localhost:8000>`_ in a browser.
- Confirm that the site works and is navigable (you should see several profiles and locations).

Linting
-------

.. code-block:: bash

   cd /path/to/da_python_p13_v2
   source env_oc_lettings_project/Scripts/activate
   flake8

Tests & Coverage
----------------

.. code-block:: bash

   cd /path/to/da_python_p13_v2
   source env_oc_lettings_project/Scripts/activate
   pytest

Database
--------

.. code-block:: bash

   cd /path/to/da_python_p13_v2
   flake8

Open a shell session:

.. code-block:: bash

   sqlite3

Connect to the database:

.. code-block:: bash

   .open oc-lettings-site.sqlite3

Display tables in the database:

.. code-block:: bash

   .tables

Display columns in the profiles table:

.. code-block:: bash

   pragma table_info(Python-OC-Lettings-FR_profile);

Run a query on the profiles table:

.. code-block:: bash

   select user_id, favorite_city from Python-OC-Lettings-FR_profile where favorite_city like 'B%';

Exit:

.. code-block:: bash

   .quit

Admin Panel
-----------

- Go to `<http://localhost:8000/admin>`_
- Log in with user `admin`, password `Abc1234!`