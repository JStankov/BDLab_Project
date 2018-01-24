
# coding: utf-8

# In[2]:


import pandas as pd, numpy as np, matplotlib.pyplot as plt, sklearn
import re

#File located in Anaconda3 working directory        
#reads in the csv with pandas and puts it into a pandas frame, separator in the file is defined as ',' 
dataset = pd.read_csv('yellow_tripdata_2017-03.csv', header=0, sep=',', nrows=10000)
dataset.head(10)


# In[3]:


#1) First try to model - as described in proposal - For a more accurate model go to 2)
#We decompose the fare amount in order to find out the extra_time*price component 
#initial question: how much time was spent in traffic jambs or at traffic lights additionally?
#Firstly, we save the values which compose the price in arrays 

total_fare = dataset["fare_amount"].values
distance = dataset['trip_distance'].values 
print(total_fare)
night_shift_dummy = []
rush_hour_dummy = []

#We need to know whether there are surcharges for the night shift or the rush hour
#In order to fill the dummies the pick-up time has to be sliced and analysed
pickup_time = dataset.as_matrix(columns=["tpep_pickup_datetime"])

time_list = []
for i in pickup_time:
    for j in i:
        a,b,c,d = re.split(' |:|:|: ',j)
        time_list.append(b)
        
for i in time_list:
    n = int(i)
    if n >= 20 or n <= 6:
        night_shift_dummy.append(1)
    else:
        night_shift_dummy.append(0)
        
for i in time_list:
    n = int(i)
    if n >= 16 and n <= 20:
        rush_hour_dummy.append(1)
    else:
        rush_hour_dummy.append(0)
        
night_shift_array = np.asarray(night_shift_dummy)
rush_hour_array = np.asarray(rush_hour_dummy)


# In[4]:


#from the total fare subtract the base price, the amount payed for the distance travelled and the dummies 
time_component = total_fare - 2.6 - (distance *0.6*5) -  (night_shift_array*0.8) - rush_hour_array   

#print(time_component) some people travelled out of the city, which does not underly the formula above.
#This results in negative values and would have to be improved in the next steps


# In[5]:


#extra time in minutes. 60 seconds cost 50ct 
extra_time = (time_component/0.5)
series_extra_time = pd.Series(extra_time, name='extra_time')


# In[6]:


#Y = extra_time
#X = n in time_list, PULocationID and DOLocationID -we assume that the independent variables in the regression will be
#the daytime and the pick-up and drop-off locations
#create a dataframe for X
df_X = dataset[["PULocationID", "DOLocationID"]]

daytime_list = []
for i in time_list:
    n = int(i)
    daytime_list.append(n)

series_daytime = pd.Series(daytime_list, name='Daytime')
#the set of independent variables is saved in X
X = pd.concat([df_X, series_daytime], axis=1)

# Split the data into training/testing sets - testing set should be data from a different month
#source: http://scikit-learn.org/stable/auto_examples/linear_model/plot_ols.html
X_train = X[:-900]
X_test = X[-900:]

# Split the targets into training/testing sets
Y_train = series_extra_time[:-900]
Y_test = series_extra_time[-900:]



# In[7]:


from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

lr = LinearRegression()

lr.fit(X_train,Y_train )
print('Coefficients: \n', lr.coef_)

#predicts the Y-values using the testing set
Y_pred = lr.predict(X_test)

# The mean squared error - compares the predicted y-values with the real values of the test-data
print("Mean squared error: %.2f"
      % mean_squared_error(Y_test, Y_pred))
# Explained variance score (coefficient of determination): 1 is perfect prediction
print('Variance score: %.2f' % r2_score(Y_test, Y_pred))

#The model we intended to build turns out to be very inaccurate in this way. The reason must be that the decomposition of the fare is incorrect - 
#We can see it in the extra_time array, which consists of negative values.
#The formula might be accurate for shorter trips, but for longer trips the guests seem to arrange a fare with the taxi driver.



# In[16]:


#2) Second Try - drop decomposition and use the fare as Y
#Y fare_amount
#X variables from prvious model + trip_distance
#X:
df2_X = dataset[["PULocationID", "DOLocationID", "trip_distance"]]
X2 = pd.concat([df2_X, series_daytime], axis=1)
print(X2)
#Y:
Y2 = pd.Series(dataset.fare_amount, name='Fare Amount')

#train and test
X2_train = X2[:-2000]
X2_test = X2[-2000:]

# Split the targets into training/testing sets
Y2_train = Y2[:-2000]
Y2_test = Y2[-2000:]


# In[15]:


lr2 = LinearRegression()

lr2.fit(X2_train,Y2_train )
print('Coefficients: \n', lr.coef_)

#predicts the Y-values using the testing set
Y2_pred = lr2.predict(X2_test)

# The mean squared error - compares the predicted y-values with the real values of the test-data
print("Mean squared error: %.2f"
      % mean_squared_error(Y2_test, Y2_pred))
# Explained variance score (coefficient of determination): 1 is perfect prediction
print('Variance score: %.2f' % r2_score(Y2_test, Y2_pred))


# In[17]:


print(Y2_pred)
print(Y2_test)


# In[18]:




