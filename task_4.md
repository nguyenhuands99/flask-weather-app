## Description

It is sad when all the cards disappear when you refresh the page. Let's work on this issue and add a database to your Flask application. Flask-SQLAlchemy allows you to add an SQLAlchemy database to the Flask application. It streamlines the usage of SQLAlchemy in Flask by providing useful defaults and extra helpers that make it easier to accomplish some of the standard tasks.

[Flask SQLAlchemy Quickstart tutorial](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/) can show you the database basics in the Flask application. The [Redirects and Errors](https://flask.palletsprojects.com/en/1.1.x/quickstart/#redirects-and-errors) section of the Flask documentation can help you with the URL redirection.

## Objectives

Create a database named `weather.db` that has the `City`model with the following fields:

- the`id` field. The column should have the Primary Key attribute.
- the `name` field. The column should have UNIQUE and NOT NULL attributes.

Template requirements are the same as in the previous stage:

If you use your own template, then the template should contain:

- One `<input>` field with an `input-city` id,
- One `<button>` with a `submit-button` city,
- One `<div>` block with a `cards` class, where you will put all your cards.
- One `<div>` block with the `cards` class. It should contain three `<div>` blocks with the `card` class. These `<div>` blocks represent a card with a city.

When a user enters a city name and presses the `Add` button, save the city name in the database and redirect to the `'/'` main page. 

Once the `'/'` page is visited, get the city names from the database, API weather data (in a loop form), and put all of them into cards of the `<div>` block. As a result, the weather data of each city should be put inside the `<div>` block with the `card` class. Check the [Loop Controls](https://jinja.palletsprojects.com/en/2.11.x/templates/#loop-controls) section for more details.

Each `<div>` block with the  `card` class should contain:

- `<div>` block with a `degree` class that represents the current temperature in a city.
- `<div>` block with a `state` class that represents the current weather state in a city.
- `<div>` block with a `city` class that represents a city name.

Don't forget to delete all the premade cards from the template. If the database has no city names, the `<div>` block with the `cards` class should be empty.
