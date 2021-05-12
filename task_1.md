## Description

Flask is a lightweight web application framework. It is designed for a quick start, and you can scale up your solutions to the level of complex applications if you want to. It is one of the most popular Python web application frameworks. The Flask framework allows you to start a web application from a single Python file.

## Theory

Create a Flask application object to start working with it:

    from flask import Flask
    
    app = Flask(__name__)

Pass `__name__` to the constructor so that Flask knows where to look for templates, static files, and so on. For more information, have a look at the [Flask documentation](https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask). We will talk about templates and static files in the next stages.

You are going to configure the project through this object; it allows you to create routes (views), a database, run the server, and so on.

We need to show Flask how to handle the incoming requests. Create a method and bind it to a URL.

    @app.route('/')
    def index():
        return 'Hi! This is the response from the Flask application'
    

If a user goes to the root URL, Flask will call the `index` method and return the result of its execution. The name of the method should be unique for each route. You can add any other routes to your application:

    @app.route('/profile')
    def profile():
        return 'This is profile page'
    
    
    @app.route('/login')
    def log_in():
        return 'This is login page'

You can learn more about routing in [the Flask documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/#routing).

All you need to do is to run your application. Use the following construction to run a flask application:

    if __name__ == '__main__':
        if len(sys.argv) > 1:
            arg_host, arg_port = sys.argv[1].split(':')
            app.run(host=arg_host, port=arg_port)
        else:
            app.run()

## Objectives

Create a simple web application that handles the requests to the `'/'`URL and returns `Hello, world!` as a response.
