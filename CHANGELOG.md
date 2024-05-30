# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Django Web Framework was added to the project in the current version 5.0.4.
- Created a new django project "django_tournament" inside the poetry project.
- Added django-allauth as authentification and user management framework.
- Added django-webtest to the development and test dependencies for test-driven development.
- Added "coverage" as dependency in dev and test group to generate test coverage reports
- Added a Django App for static pages, currently serving a dummy index page for the whole project ("Hello World" type).
- Added a Django App for managing Tournaments. This is the main app for the project
  - A tournament is defined by a start date and an end date.
  - Teams are defined by name, club of origin, city of origin and a colour scheme (primary and secondary colour) and have a team leader who is a registered user of the app.
  - Teams have Players as Team Members.
    - Per-Team info for players can be stored on the intermediate Model (such as jersey numbers).
  - Players are Users of the App.
  - Teams are Participants of Tournaments
