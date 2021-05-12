from flask import Flask, render_template, flash, request
from flask import redirect
import sys
from sqlalchemy.exc import IntegrityError
import os

import db_api
import weather_api

app = Flask(__name__)
app.secret_key = os.urandom(24) 

@app.route('/')
def index():
    weathers=[ weather_api.get_weather(city.name, city.id) for city in db_api.get_cities()]
    return render_template('index.html', weather=weathers)

@app.route('/add', methods=['POST'] )
def add_city():
    try:
        city_name = request.form['city_name']
        if str.lower(city_name) in [str.lower(city.name) for city in db_api.get_cities()]:
            flash("The city has already been added to the list!")
        elif weather_api.check_city_name(city_name) is not True:
            flash("The city doesn't exist!")
        else:
            db_api.add_cities(name=city_name)
        return redirect('/')
    except IntegrityError:
        flash('The city has already been added to the list!')
        return redirect('/')

@app.route('/delete/<city_id>', methods=['GET', 'POST'])
def delete(city_id):
    db_api.delete_cities(city_id=city_id)
    return redirect('/')


# don't change the following way to run flask:
if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port)
    else:
        app.run()

