from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/nasa_data')
def display_nasa_data():
    try:
        #since the API is free and open from NASA organisation, you should reach out to their page and request for your API, they will probably provide it immediately if you need for exercise.
        api_url = "https://api.nasa.gov/techtransfer/patent/?engine&api_key=t1YcXQbB9AQs7hiAXw1xWUpZ1WcWp8ku0TZ7v4gn"
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()

            formatted_data = []
            for record in data['results']:
                record[3] = strip_html(record[3])
                formatted_data.append(record)
            
            data['results'] = formatted_data
            return jsonify(data)  # Return the data as JSON response
        else:
            return f"Request failed with status code {response.status_code}"

    except requests.exceptions.RequestException as e:
        return f"Request error: {e}"


def strip_html(text):
    from bs4 import BeautifulSoup
    return BeautifulSoup(text, "html.parser").get_text()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
