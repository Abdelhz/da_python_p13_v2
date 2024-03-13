Prerequisites
=============

- GitHub account with read access to this repository.
- Git CLI.
- SQLite3 CLI.
- Python interpreter, version 3.6 or higher.
- Git for windows installed (If using windows as OS)
- Docker engine installed in your system. Visit `Docker Installation Procedure <https://docs.docker.com/engine/install/>`_ for installation procedure.
- A Sentry account with a created project and a `Sentry DSN key`. Visit `Sentry <https://sentry.io>`_ and `Sentry Getting Started <https://docs.sentry.io/product/sentry-basics/integrate-backend/getting-started/>`_ for more details.
- A CircleCI Account with CircleCi project connected to your project repository on `GitHub`, `Gitlab` or `BitBucket`. (Adding the django `SECRET_KEY`, `SENTRY_DSN`, `DOCKERHUB_USER`, `$DOCKERHUB_PASS` and `$TAG` with the value `CIRCLE_SHA1_LATEST` to the circleci environment variables). Visit `CircleCI <https://circleci.com>`_ and `CircleCI Docs <https://circleci.com/docs/>`_ for more details.
- A Docker Account with Docker `username` for `$DOCKERHUB_USER` and `password` for `$DOCKERHUB_PASS` added as environment variables for `Docker HUB` access. Visit `Docker <https://www.docker.com/>`_.
- A Render Account (with Web service created for the Docker HUB main image after creating and pushing this image) and adding `SECRET_KEY` and `SENTRY_DSN` as environment variables. Visit `Render <https://www.render.com>`_