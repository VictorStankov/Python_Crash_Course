import json
from pygal_maps_world.maps import World
from country_codes import get_country_code
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS

filename = 'gdp_json.json'
with open(filename) as f:
    pop_data = json.load(f)

gdp = {}
for gdp_dict in pop_data:
    if gdp_dict['Year'] == 2010:
        country_name = gdp_dict['Country Name']
        gdp_val = float(gdp_dict['Value'])
        code = get_country_code(country_name)
        if code:
            gdp[code] = gdp_val

wm_style = RS('#336699', base_style=LCS)
wm = World(style=wm_style)
wm.title = "World GDP in 2010, by Country"
wm.add("GDP", gdp)

wm.render_to_file('world_gdp.svg')
