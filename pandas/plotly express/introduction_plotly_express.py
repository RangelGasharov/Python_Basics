import plotly.express as px
import pandas as pd

country_data = px.data.gapminder()
print(country_data.tail())
map_fig = px.scatter_geo(country_data, locations="iso_alpha", projection="orthographic", color="continent",
                         opacity=.8, hover_name="country", hover_data=["pop"])
map_fig.show()

earthquakes = "https://raw.githubusercontent.com/\
plotly/datasets/master/earthquakes-23k.csv"

df = pd.read_csv(earthquakes)
# help(px.density_mapbox)

fig = px.density_mapbox(df, lat="Latitude", lon="Longitude", z="Magnitude", radius=10,
                        center=dict(lat=9, lon=9), zoom=1, hover_name="Date",
                        mapbox_style="open-street-map", title="Earthquake Data 1965-2016")
fig.show()
