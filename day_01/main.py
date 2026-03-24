from pathlib import Path

import folium
import osmnx as ox

# from matplotlib import pyplot as plt

day_root = Path(__file__).parent


def to_point(gdf):
    if gdf.empty:
        return gdf

    # No idea what's going on here.
    return gdf.to_crs(epsg=3857).centroid.to_crs(4326).to_frame("geometry")


city_name = "Prague, Czech Republic"
admin = ox.geocode_to_gdf(city_name)
# admin.plot()
# plt.show()

pubs = ox.features_from_place(
    city_name,
    tags={"amenity": "pub"},
)
pubs = to_point(pubs)

sports = ox.features_from_place(
    city_name,
    tags={"leisure": "sports_centre"},
)
sports = to_point(sports)

healthcare = ox.features_from_place(
    city_name,
    tags={"amenity": ["hospital", "clinic", "doctors", "pharmacy"]},
)
healthcare = to_point(healthcare)

# The content doesn't make use of f-strings.
print(f"Pubs {len(pubs)}, Sports {len(sports)}, Healthcare {len(healthcare)}")

minx, miny, maxx, maxy = admin.total_bounds
fit_bounds = [[miny, minx], [maxy, maxx]]
center = [(miny + maxy) / 2, (minx + maxx) / 2]

m = folium.Map(
    location=center,
    # https://python-visualization.github.io/folium/latest/getting_started.html#Choosing-a-tileset
    tiles="CartoDB dark_matter",
    control_scale=True,
)
admin_layer = folium.FeatureGroup(name="Admin Boundary")
pubs_layer = folium.FeatureGroup(name="Pubs")
sports_layer = folium.FeatureGroup(name="Sports Centres")
healthcare_layer = folium.FeatureGroup(name="Healthcare", show=False)

folium.GeoJson(
    admin,
    style_function=lambda feature: {
        "fillColor": "#ffffff",
        "color": "#ffffff",
        "weight": 3,
        "fillOpacity": 0.15,
    },
).add_to(admin_layer)


def add_points(gdf, feature_group, color):
    if gdf is None or gdf.empty:
        return

    for _, row in gdf.iterrows():
        point = row.geometry
        if point is None:
            continue

        folium.CircleMarker(
            location=[point.y, point.x],
            radius=2,
            weight=0.5,
            fill=True,
            fill_opacity=0.8,
            color=color,
            fill_color=color,
        ).add_to(feature_group)


add_points(pubs, pubs_layer, "#ff9933")  # Orange
add_points(sports, sports_layer, "#44e0ff")  # Cyan
add_points(healthcare, healthcare_layer, "#ff4444")  # Magenta


admin_layer.add_to(m)
pubs_layer.add_to(m)
sports_layer.add_to(m)
healthcare_layer.add_to(m)

folium.LayerControl(
    collapsed=False,
    position="topright",
).add_to(m)

if fit_bounds:
    m.fit_bounds(fit_bounds)

m.save(day_root / "map.html")
