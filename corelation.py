import csv
import plotly_express as px
import numpy as np

with open("data.csv") as f:
    df = csv.DictReader(f)

    marks = []
    days = []

    for data in df:
        marks.append(float(data["Marks In Percentage"]))
        days.append(float(data["Days Present"]))

    corelation = np.corrcoef(marks, days)

    print(corelation[0,1])

    fig = px.scatter(df, x = marks, y = days)

    fig.show()
