import requests
import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv'
    response = requests.get(url)
    df = pd.read_csv(response.content)
    data = df[df['Country/Region'] == 'Czechia'].to_dict('records')
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
