# https://atlo.team/boda/ > Road accidents data set - requires manual download.
from pathlib import Path

import folium
import geopandas as gpd
from branca import colormap as cm

day_root = Path(__file__).parent

m = folium.Map(tiles="CartoDB positron")
gdf = gpd.read_file(day_root / "data" / "budbalesetroads.geojson")

minx, miny, maxx, maxy = gdf.total_bounds
m.fit_bounds([[miny, minx], [maxy, maxx]])

# Color map
colormap = cm.LinearColormap(
    caption="Traffic accidents (2015-2018)",
    colors=list(reversed(cm.linear.RdYlGn_11.colors)),
    vmin=gdf["_Medianmean"].min(),
    vmax=gdf["_Medianmean"].max(),
).to_step(n=10)

# TODO: How to print this out to console?
# print(colormap)

colormap.add_to(m)

# Data layer
data_layer = folium.GeoJson(
    gdf,
    style_function=lambda feature: {
        "color": colormap(feature["properties"]["_Medianmean"]),
        "weight": 3,
        "opacity": 0.9,
    },
)

data_layer.add_to(m)

# Export
m.save(day_root / "map.html")
