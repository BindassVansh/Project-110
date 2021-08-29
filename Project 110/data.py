import pandas as pd
import plotly.express as pe
import plotly.figure_factory as pff
import random
import statistics

df = pd.read_csv('data.csv')
data = df["reading_time"].tolist()
finalList = []

def datapoints() :
    sampledata = []
    for i in range(len(data)):
        position = random.randint(0,len(data)-1)
        reading = data[position]
        sampledata.append(reading)

    mean = statistics.mean(sampledata)
    finalList.append(mean)

for i in range(0,1000):
    datapoints()

graph = pff.create_distplot([finalList],["Reading Time"],show_hist=False)
graph.show()

