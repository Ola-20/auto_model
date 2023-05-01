
# This is the utility file that provides all the necessary codes for the computation of the price and
# will be refrenced by the server.py file
import json
import pickle
import numpy as np


__location = None
__column_data = None
__years = None
__transmission = None
__model = None

def get_estimate_price(odo, location, year, transmission):
    # get the index of location, year, transmission from the loaded column_data
    # which will be converted to 0 and 1 in the one hot below
    loc_index = __column_data.index(location.lower())
    year_index = __column_data.index(year.lower())
    trans_index = __column_data.index(transmission.lower())

    x = np.zeros(len(__column_data))
    x[0] = odo
    if loc_index >= 0:
        x[loc_index] = 1
    if year_index >= 0:
        x[year_index] = 1
    if trans_index >= 0:
        x[trans_index] = 1

    return round(__model.predict([x])[0])


def get_location_name():
    return __location

def get_year():
    return __years

def get_transmission():
    return __transmission

def load_saved_artifacts(): # This will load both the columns and the auto_predictor from the saved artifacts into memory
    print("loading saved artifacts...... starts")
    global __column_data
    global __location
    global __years
    global __transmission
    global __model
    with open("./artifacts/columns.json", 'r') as f:
        __column_data = json.load(f)['column_data'] # loading all the columns
        # slice the columns for specific variables
        __location = __column_data[1:3]
        __years = __column_data[3:10]
        __transmission = __column_data[10:12]
    with open("./artifacts/auto_predictor.pickle", 'rb') as f:
        __model = pickle.load(f)
        print("Loading saved artifact......done")


if __name__ =="__main__":
    load_saved_artifacts()
    print(get_location_name())
    print(get_year())
    print(get_transmission())
    print(get_estimate_price(35765.0, 'calgary', '2019', 'automatic'))

'''
import sklearn
print(sklearn.__version__)
'''