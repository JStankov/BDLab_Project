# BD_Project - Taxi Price Prediction - by Luis and Jelena
We use the NYC taxi dataset and streaming data pipeline (consisting of Kafka and Spark) to eventually construct a regression model capable of forecasting the price of a future taxi ride.

Our architecture (grey elements not implemented yet)




##Prerequisites
Cloudera Quickstart VM 5.12
CDH 5.12, Kafka, Spark installed and aditionally Yarn and Zookeeper as active Services
Python2.7 and the Jupyter Notebook (or Anaconda )
Libraries and packages: pandas, sklearn, numpy, kafka and csv databricks (package for pyspark for the preliminary architecture)

Set the following paths so you can use jupyter to work with pyspark:
export PYSPARK_DRIVER_PYTHON=jupyter
export PYSPARK_DRIVER_PYTHON_OPTS='notebook'
export PATH=/home/cloudera/anaconda2/bin:$PATH
export PYSPARK_PYTHON=/home/cloudera/anaconda2/bin/python

##Data Slicing and Kafka Producer

##Spark Consumer

##Spark DataFrames and Model construction

