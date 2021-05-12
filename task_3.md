## Description

Static data is boring. Let's add a feature to display the weather of your favorite city. Make a POST request to the server with the city name, and the server will show you the weather in that city. To get the weather data, you need access to a weather service API.

## Theory

Flask routes can handle only GET requests by default. To handle POST requests, add a `methods` list and specify the request type for this route:

    @app.route('/add', methods=['POST'])
    def add_city():
        pass
    

In the example above, the `'/add'` route can handle only POST requests. If you want to handle both `POST` and `GET` requests, set it to `methods=['GET', 'POST']`.

To pass the data from the website to the server you need to create a form inside an HTML template. It will take a city name from the input field and make a POST request to the specific URL with the city name when the submit button is pressed.

To get the data from the `POST` request on the server side, you can use the `request` object. You can learn more about `request` objects in the [Flask documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/#the-request-object).

Once you got the city name, you need to get the weather data in that city. You can use the [OpenWeather API](https://openweathermap.org/current) to get the current weather data. To use this API you need an API KEY (see the [How To Start](https://openweathermap.org/appid) section on the OpenWeather API site). API has no limitations, you can use any service that provides the weather data or you can generate data randomly.

You need the city name, current temperature in celsius, and the current weather state. Once you get it, you can put it all into a dictionary and pass it to the template. Use the `render_template()` method to pass this data to your dictionary:

    return render_template('index.html', weather=dict_with_weather_info)

We passed the `dict_with_weather_info` dictionary to the `index.html` template. We can access the dictionary using the `weather` variable in the template. [Jinja documentation](https://jinja.palletsprojects.com/en/2.11.x/templates/#variables) can help you with variables and show how to put them into HTML tags.

Don't forget to check whether the variable has been passed to the template with the [IF block](https://jinja.palletsprojects.com/en/2.11.x/templates/#if) to avoid exceptions.

## Objectives

Return the HTML template with 3 predefined weather cards once the program visited the URL. Once a user enters a city name and presses the button with the `submit-button` class, get the city name from the POST request, find the weather data of that city, pass it into the template, and return the template as a response. As a result, the page should contain 4 weather cards, one of which is a city from the user input.

If you use your own template, the template should contain:

- One `<input>` field with an `input-city` id,
- One `<button>` with a `submit-button` city,
- One `<div>` block with a `cards` class, where you will put all your cards.
- One `<div>` block with the `cards` class. It should contain three `<div>` blocks with the `card` class. These `<div>` blocks represent a card with a city.

Each div block with card class should contain:

- `<div>` block with a `degree` class that represents the current temperature in a city.
- `<div>` block with a `state` class that represents the current weather state in a city.
- `<div>` block with a `city` class that represents a city name.

You can add additional classes to the `<div>` block to set a background image according to the current city time: `night`, `day`, and `evening-morning`.

Mind that the HTML form is already implemented in the premade template from the previous stage. It passes the city name to the server when the `Add` button is pressed.
