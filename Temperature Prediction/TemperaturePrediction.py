"""
Predicting the temperatures:

Given the hourly temperature data for each 24 hours period in p prior days spanning from startDate to endDate inclusive, predict
the hourly temperature data for the next n days starting the first hour after endDate.

Function Description:
Complete the function predictTemperature in the editor below. The function must return an array of floating point numbers, one predicted temperature for each
hour of n days immediately following endDate in chronological order.

"""



from datetime import datetime
import numpy as np
from scipy import interpolate

def predictTemperature(startDate, endDate, temperature, n):
    d1 = datetime.strptime(startDate, "%Y-%m-%d")        # changes dataTime string to dateTime object
    d2 = datetime.strptime(endDate, "%Y-%m-%d")
    p = abs((d2 - d1).days) + 1                          # finds the difference between the starting and the ending date
    m = 24 * p                                           # find the total number of hours for training
    z = 24 * n                                           # find the total number of hours for testing
    training_features = [i for i in range(m)]            # an array of training features
    testing_features = [i for i in range(z)]             # an array of testing features
    answer = []                                          # the array containting the answers

    model = interpolate.UnivariateSpline(training_features, temperature, s=4)    # interpolation using a smoothing factor of 4.

    for day in testing_features:                         # predicts the temperature for the next days
        answer.append(model(day))  

    return answer                                        # returns the answer array