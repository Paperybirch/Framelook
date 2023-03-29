mport numpy as np
import math
import pandas as pd
import plotly.express as px
path = './framelook/test.csv'
a=pd.read_csv(path)
a=a.fillna(0)
#print(a)
year=a.loc[:,'Year']
visit_dur=a.loc[:,'Visit_duration']
#fig = px.scatter(y=visit_dur, x=year)
fig = px.histogram([1,1,1,1,1,3,3,3,3,3,4,5,6,7,2,2,2,3,4,5,6])
fig.show()

z=np.unique(visit_dur)
print(z)
