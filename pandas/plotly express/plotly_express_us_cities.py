import plotly.express as px
import pandas as pd

us_cities = "https://raw.githubusercontent.com/plotly/datasets/master/2014_us_cities.csv"

df = pd.read_csv(us_cities)

fig = px.scatter_mapbox(df, lat="lat", lon="lon", hover_name="name", hover_data=["pop"],
                        color_discrete_sequence=["fuchsia"], zoom=3, height=300)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
