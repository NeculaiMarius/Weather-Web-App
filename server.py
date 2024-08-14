from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app=Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/weather')

def get_weather():
    city= request.args.get('city')

    #Check for empty strings or strings with only empty spaces
    if not bool(city.strip()):
        city="Bucharest"

    weather_data= get_current_weather(city)

    #City is not found by API
    if not weather_data['cod']==200:
        return render_template("city-not-found.html")
    
    #Templates based on weather
    if weather_data["weather"][0]["main"]=='Clear':
        return render_template(
            "clear.html",
            title=weather_data["name"],
            status=weather_data["weather"][0]["description"].capitalize(),
            temp=f"{weather_data['main']['temp']:.1f}",
            feels_like=f"{weather_data['main']['feels_like']:.1f}"
        )
    
    if weather_data["weather"][0]["main"] in ['Rain','Drizzle']:
        return render_template(
            "rain.html",
            title=weather_data["name"],
            status=weather_data["weather"][0]["description"].capitalize(),
            temp=f"{weather_data['main']['temp']:.1f}",
            feels_like=f"{weather_data['main']['feels_like']:.1f}"
        )
    
    if weather_data["weather"][0]["main"]=='Clouds':
        return render_template(
            "clouds.html",
            title=weather_data["name"],
            status=weather_data["weather"][0]["description"].capitalize(),
            temp=f"{weather_data['main']['temp']:.1f}",
            feels_like=f"{weather_data['main']['feels_like']:.1f}"
        )
    
    if weather_data["weather"][0]["main"]=='Thunderstorm':
        return render_template(
            "thunderstorm.html",
            title=weather_data["name"],
            status=weather_data["weather"][0]["description"].capitalize(),
            temp=f"{weather_data['main']['temp']:.1f}",
            feels_like=f"{weather_data['main']['feels_like']:.1f}"
        )
    
    if weather_data["weather"][0]["main"]=='Snow':
        return render_template(
            "snow.html",
            title=weather_data["name"],
            status=weather_data["weather"][0]["description"].capitalize(),
            temp=f"{weather_data['main']['temp']:.1f}",
            feels_like=f"{weather_data['main']['feels_like']:.1f}"
        )

    return render_template(
        "weather.html",
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}"
    )

if __name__=="__main__":
    serve(app,host="0.0.0.0",port=8000)