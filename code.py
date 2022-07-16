import pandas as pd 
import plotly.express as px
import csv 
df=pd.read_csv("data_for_analysis.csv")
mean=df.groupby(["student_id","level"],as_index=False)["attempt"].mean()

fig=px.scatter(mean,x="student_id",y="level",color="attempt",size="attempt")
fig.show()