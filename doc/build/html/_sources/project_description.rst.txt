Project Description
===================

Orange County Lettings is a startup in the real estate rental sector. The startup is in the midst of expanding in the United States.

The company has therefore decided to hire new recruits, of which you are a part. As a developer, you are expected to play a significant role in enhancing the company's website, both in terms of code and deployment.

This documentation details the changes made to the project.

The project has been enhanced in the following ways:

- Refactoring of the codebase by improving the `modularity` to improve readability and maintainability.
- Eliminating some technical debts but implementing a test suite using `pytest-django` and `pytest-cov`.
- Creation of a `CI/CD` pipeline using `CircleCI` that run the `test suite`, `containerize` the application using `docker`, and `deploy` the application to `Render` using an `URL hook`.
- Implement monitoring and error tracking system using `Sentry`.