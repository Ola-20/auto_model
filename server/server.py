#This server will route all request to a module called util which will contain actual code that will return output
#This output will then be served by the server
from flask import Flask, jsonify, request
import util
app = Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    # we use the jsonify module to create a key: value pair.
    #The util.get_location_names function will store different city locations in the 'locations'
    # key and serve as dropdown option in the web UI that we will create.

    response = jsonify({
        'locations': util.get_location_name()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/get_year')
def get_year():
    # The util.get_year function will store different year in the 'year'
    # key and serve as dropdown option in the UI.

    response = jsonify({
        'year': util.get_year()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
@app.route('/get_transmission')
def get_transmission():
    # The util.get_transmission function will store different transmission in the 'transmission'
    # key and serve as dropdown option in the UI.

    response = jsonify({
        'transmission': util.get_transmission()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
@app.route('/predict_used_car_price', methods= ['POST'])
def predict_car_price():
    # request object has a form method.
    # below the variable odo in the backend is expecting the form method to retrieve any entry by a user into
    # 'odo' key in the front end
    # The process is also repeated for the other backend variable below.
    odo = float(request.form['odo'])
    location = request.form['location']
    year = request.form['year']
    transmission = request.form['transmission']

    # Below create a dictionary. The key = estimated price,
    # The value =module util with the get_estimated_price function. we pass all the retrieved parameters to the function
    # Therefore the predicted values will be stored in the key(estimated_price)
    response = jsonify({
        'estimated_price': util.get_estimate_price(odo , location, year, transmission)
    })

    # Below will allow request from any origin to access this aplication
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print("Starting python Flask server for used Hunda civic price prediction.......")
    util.load_saved_artifacts() # this includes the model in the pickle file format from util.py
    app.run()  # After loadintg the artifacts, It will the run the above flask app and return the estimate.