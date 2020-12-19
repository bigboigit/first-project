# Title: ML Final
# Kiarash Jalali
# 2020-11-30
# Page that makes prediction and cleans up the data

from CalculationFunctions import *
from DataProcessor import *
from sklearn.linear_model import LinearRegression

# Creating our model
predictor = LinearRegression(n_jobs=-1)
predictor.fit(X=train_input(input_data), y=train_output(output_data))

# Putting our test into into a variable
# So we can use it more than once
test = test_input(input_data)
outcome = predictor.predict(X=test)
coef = predictor.coef_

# Computing our percentage error
final_data = precentage(percenterror(test_output(output_data), outcome))