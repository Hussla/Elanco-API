from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Make GET request to the API
    response = requests.get('https://engineering-task.elancoapps.com/api/raw')

    # Check if request was successful (status code 200)
    if response.status_code == 200:
        # Extract data from response (assuming JSON format)
        raw = response.json()
        
        # Find the application with the highest cost
        

        return render_template('index.html', raw=raw)
    else:
        return 'Failed to retrieve data from the API', 500

if __name__ == '__main__':
    app.run(debug=True)
