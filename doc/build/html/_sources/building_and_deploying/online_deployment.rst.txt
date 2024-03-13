Building and Deploying
======================

Online Deployment
-----------------

After doing the following:

- Creating and setting up a CircleCi and project with your github project and the needed environment variables.
- Creating and setting up a docker account
- Creating an Render account and new web service linked to your main image in docker hub.

Deployment RUN
~~~~~~~~~~~~~~

- Add the ``URL`` given by your ``Render Web Service`` to the ``ALLOWED_HOSTS`` list in your ``settings.py``.
- After adding the ``Render web service URL``, simply commit your code and push it to your github (the one linked to your CircleCI Pipeline), the pipeline will do the work
- Visit the ``URL`` given by your ``Render Web Service``.

Environment Variables to Setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

CircleCI Environment Variables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1

   * - Name
     - Value
     - Description
   * - DOCKERHUB_PASS
     - ``Your Docker username``
     - This is the username from the Docker account credentials
   * - DOCKERHUB_USER
     - ``Your Docker password``
     - This is the password from the Docker account credentials
   * - RENDER_DEPLOY_HOOK_URL
     - ``Your render web service hook``
     - Obtained from the render web service settings page after creating the render web service and linking it to your docker image from docker hub.
   * - SECRET_KEY
     - ``Your django secret key``
     - Generated earlier
   * - SENTRY_DSN
     - ``Your Sentry DSN key``
     - Obtained from sentry website in your project
   * - TAG
     - ``Your main image TAG``
     - The custom tag you chose for the main image

The CircleCI pipeline defined by the config.yml file has 3 main job executed in the workflows:

.. list-table::
   :header-rows: 1

   * - Job Name
     - Requires
     - Branch Filters
   * - build_and_testing_Suite
     - None
     - Every branch
   * - containerize
     - build_and_testing_Suite
     - Only master branch
   * - deploy
     - containerize
     - Only master branch