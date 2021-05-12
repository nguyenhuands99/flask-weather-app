## Description

It is neither practical nor interesting when the server responds with plain text only. It is much better when the server sends an HTML template with a nice design.

Returning an HTML template in Flask is easy. You can use the `render_template` method. It takes the name of the template. Once it gets the name of the template, the `render_template` method searches for the template in the `templates` folder and returns it. This folder must be at the same level as the Python file with the Flask class object.

## Theory

This is a sample of a Flask project structure:

    .
    ├── templates
    │   └── index.html
    ├── static
    │   └── style.css
    └── app.py

Flask can also work with static files: CSS files, images, JavaScript files, and so on. These files should be stored in the `static` folder. To access and import these files to the HTML templates, use the `url_for` method. If you open a predefined `index.html` file in the templates folder, you will see the following line (it imports a CSS file to an HTML page):

    <link rel="stylesheet" target="_blank" href="{{ url_for('static', filename='style.css') }}">

Flask uses the Jinja template engine by default. It allows you to add the data to your HTML file. When you call the `render_template` method, the Jinja engine goes through the HTML file looking for the special delimiters (`{{ }}`, `{% %}`, ...) to work with them. For the example above, it will find `{{ url_for('static', filename='style.css') }}` . Then the engine will call the `url_for` method to return the path to the style.css file and insert that path to the `href` attribute. We will discuss Jinja in detail in the next stages.

To return the HTML file as a response, return the result of the `render_template` execution:

    from flask import render_template
    
    # ....
    
    @app.route('/')
    def index():
        return render_template('template_name.html')

You can create any other folder to store HTML files in the `templates` folder. However, you should specify the path to the exact file in the `render_template` method. For example: `render_template('folder_name/template_name.html')`

## Objectives

In this stage, your web application should handle requests to the `'/'` URL and return the HTML templatefile as a response. You can download an archive with the predefined `template` and `static` folders from [here](https://stepik.org/media/attachments/lesson/494358/web.zip). Put them with your `app.py` file.

If you want to design the web page by yourself, you can create a template on your own. The template should contain:

- One `<input>` field with an `input-city` id,
- One `<button>` with a `submit-button` city,
- One `<div>` block with a `cards` class, where you will put all your cards.
- One `<div>` block with the `cards` class. It should contain three `<div>` blocks with the `card` class. These `<div>` blocks represent a card with a city.

Each `<div>` block with the `card` class should contain:

- One `<div>` block with a `degrees` class that represents the current temperature in a city.
- One `<div>` block with a `state` classthat represents the current weather state in a city.
- One `<div>` block with a `city` class that represents a city name.

This is what your web page may look like with the `'/'` URL:

![](https://ucarecdn.com/e17bc1bc-4fc5-4b9c-9866-8a9076935316/)
