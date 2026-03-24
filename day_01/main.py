from pathlib import Path

import folium
import osmnx as ox


# Utils
def to_point(gdf):
    if gdf.empty:
        return gdf

    # No idea what's going on here.
    return gdf.to_crs(epsg=3857).centroid.to_crs(4326).to_frame("geometry")


def add_markers(points, feature_group, color):
    for _, row in points.iterrows():
        point = row.geometry
        if point is None:
            continue

        marker = folium.CircleMarker(
            location=(point.y, point.x),
            radius=2,
            weight=0.5,
            fill=True,
            fill_opacity=0.8,
            color=color,
            fill_color=color,
        )
        marker.add_to(feature_group)


day_root = Path(__file__).parent

city_name = "Prague, Czech Republic"
m = folium.Map(
    # https://python-visualization.github.io/folium/latest/getting_started.html#Choosing-a-tileset
    tiles="CartoDB dark_matter",
    control_scale=True,
)

admin_gdf = ox.geocode_to_gdf(city_name)

minx, miny, maxx, maxy = admin_gdf.total_bounds
m.fit_bounds(([miny, minx], [maxy, maxx]))

# Admin boundary
admin_group = folium.FeatureGroup(name="Admin Boundary")
admin_layer = folium.GeoJson(
    admin_gdf,
    style_function=lambda feature: {
        "fillColor": "#ffffff",
        "color": "#ffffff",
        "weight": 3,
        "fillOpacity": 0.15,
    },
)
admin_layer.add_to(admin_group)
admin_group.add_to(m)

# admin.plot()
# from matplotlib import pyplot as plt
# plt.show()

# Pubs
pubs_gdf = ox.features_from_place(
    city_name,
    tags={"amenity": "pub"},
)
print(f"Pubs: {len(pubs_gdf)}")

pubs_points = to_point(pubs_gdf)
pubs_group = folium.FeatureGroup(name="Pubs")
add_markers(pubs_points, pubs_group, "#FF9933")
pubs_group.add_to(m)

# Sports
sports_gdf = ox.features_from_place(
    city_name,
    tags={"leisure": "sports_centre"},
)
print(f"Sports: {len(sports_gdf)}")

sports_points = to_point(sports_gdf)
sports_group = folium.FeatureGroup(name="Sports Centres")
add_markers(sports_points, sports_group, "#44E0FF")
sports_group.add_to(m)

# Healthcare
healthcare_gdf = ox.features_from_place(
    city_name,
    tags={"amenity": ["hospital", "clinic", "doctors", "pharmacy"]},
)
print(f"Healthcare: {len(healthcare_gdf)}")

healthcare_points = to_point(healthcare_gdf)
healthcare_group = folium.FeatureGroup(name="Healthcare", show=False)
add_markers(healthcare_points, healthcare_group, "#FF4444")
healthcare_group.add_to(m)

# Layer control
layer_control = folium.LayerControl(collapsed=False)
layer_control.add_to(m)

# Export
m.save(day_root / "map.html")
