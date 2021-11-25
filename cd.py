import plotly.express as px
import csv

with open("coffeedata.csv") as csvFile:
    df = csv.DictReader(csvFile)
    fig = px.scatter(df,x = "Coffee in ml", y = "sleep in hours")
    fig.show()

    