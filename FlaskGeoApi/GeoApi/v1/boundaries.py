from .. import app
from flask import jsonify
#import pandas as pd
#import geopandas as gpd

@app.route("/v1/boundary")
def boundary():

    #df = pd.DataFrame(
    #{'City': ['Buenos Aires', 'Brasilia', 'Santiago', 'Bogota', 'Caracas'],
     #'Country': ['Argentina', 'Brazil', 'Chile', 'Colombia', 'Venezuela'],
     #'Latitude': [-34.58, -15.78, -33.45, 4.60, 10.48],
     #'Longitude': [-58.66, -47.91, -70.66, -74.08, -66.86]})

    #gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude))

    #return gdf.head().to_json()
    return jsonify("Hello","user")


@app.route("/v1/test")
def test():

    return jsonify("Hello","user")

