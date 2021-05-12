## Description

Let's add the ability to remove cards from the site. To do so, you need to make a request with a city database id to the server. Also, just in case a user has put the wrong city name in the request, you need to send an error message to the user.

## Theory

Flask can obtain values from the request URL. Below is an example of how you can take a city id from the URL and delete it from the database:

    @app.route('/delete/<city_id>', methods=['GET', 'POST'])
    def delete(city_id):
        city = City.query.filter_by(id=city_id).first()
        db.session.delete(city)
        db.session.commit()
        return redirect('/')

It takes a city id from the route, deletes it from the database, and redirects a user to the main page.

Also, Flask can send flash messages to the user by passing a message in the `flash()` method:

    from flask import flash
    
    ...
    
    @app.route('/', methods=['POST'])
    def add():
        ...
        if city == None:
            flash("The city doesn't exist!")
        return redirect('/')

After that, you can show the message in the template:

    {% with message = get_flashed_messages() %}
    {% if message %}
    <div class="alert alert-primary" role="alert">
        {{message[0]}}
    </div>
    {% endif %}
    {% endwith %}

## Objectives

Handle the wrong input:

- If the user enters a city name that doesn't exist, output the following message: `The city doesn't exist!`
- If the user enters a city name that has already been added to the database, output the following message: `The city has already been added to the list!`

Add the ability to delete cards. Each card should contain a form with a button inside. When the button is pressed, make a POST or a GET request to the server with a city id. For example, `/delete/{{city.id}}`. This class is `delete-button`. On the server side, take a city id, delete it from the database, and redirect a user to the main page.
