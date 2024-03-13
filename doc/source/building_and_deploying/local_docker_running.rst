Building and Deploying
======================

Local Docker Running
--------------------

In the project root directory the ``docker_local_commands.sh`` does the following when ran:

- Build the docker image.
- Push the docker image to the docker HUB.
- Pull back the Image from the docker HUB.
- Run locally the docker image.

In order to use this file you need to modify it as following:

- Open the file ``docker_local_commands.sh`` in editor;
- Replace the ``Your username`` in ``DOCKERHUB_USER="Your username"`` with you actual Docker ``username``;
- Replace the ``Your password`` in ``DOCKERHUB_PASS="Your password"`` with you actual Docker ``password``;
- Replace the ``Your secret key`` in ``SECRET_KEY="Your secret key"`` with you actual Django ``secret key`` that you generated before;
- Replace the ``Your secret key`` in ``SENTRY_DSN="Your SENTRY_DSN key"`` with you actual Sentry ``DNS key`` that you get from your sentry project on sentry website;

After setting up the ``docker_local_commands.sh``

Run this command from terminal in the project root directory:

.. code-block:: bash

   bash docker_local_commands.sh

- On a browser go to ``http://localhost:8000/`` to access the locally ran website.