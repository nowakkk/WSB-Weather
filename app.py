from flask import Flask, render_template, request
from models import weather, news as n, forecast

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    data = ''
    chart = ''
    city_info = ''
    if request.method == 'POST':
        user_input = request.form['user_input']
        print("POST method")

        if not user_input:
            # User input is empty, handle the error or display a message
            error_message = 'Please provide a valid input.'
            return render_template('index.html', error_message=error_message)

        try:
            pogoda = weather.Weather(user_input)
            data = pogoda.get_all_data()
            prognoza = forecast.Forecast(user_input)
            chart = prognoza.get_chart_html()
            news = n.News(user_input)
            city_info = news.get_news()
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    return render_template('index.html', data=data, chart=chart, city_info=city_info)


if __name__ == '__main__':
    app.run()
