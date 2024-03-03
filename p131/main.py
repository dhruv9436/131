import csv

rows=[]

with open ("main.csv","r") as f:
    csv_reader=csv.reader(f)
    for row in csv_reader:
        rows.append(row)

headers=rows[0]
planet_data_rows=rows[1:]
#print(headers)
#print(planet_data_rows[0])

headers[0]="row_num"

solar_system_planet_count={}

for planet_data in planet_data_rows:
    if solar_system_planet_count.get(planet_data[11]):
        solar_system_planet_count[planet_data[11]]+=1 # {KOI_851 =2}
    else:
        solar_system_planet_count[planet_data[11]]=1 # {'KOI_851'=1, ' magnum_230'= 4, }


max_solar_system= max(solar_system_planet_count, key=solar_system_planet_count.get)

print("The solar system "+max_solar_system+" has the maximun number of planets which is "+str(solar_system_planet_count[max_solar_system]))



temp_planet_data_rows =list(planet_data_rows)
for planet_data in temp_planet_data_rows:
    planet_mass=planet_data[3]
    if (planet_mass.lower()=="unknown"):
        planet_data_rows.remove(planet_data)
        continue
    else:
        planet_mass_value=planet_mass.split(" ")[0]
        planet_mass_ref=planet_mass.split(" ")[1]
        if(planet_mass_ref =="Jupiters"):
            planet_mass_value=float(planet_mass_value) * 317.8
            planet_data[3]=planet_mass_value
        if(planet_mass_ref=="Earths"):
            planet_mass_value=float(planet_mass_value)
            planet_data[3]=planet_mass_value

    planet_radius = planet_data[7]
    if planet_radius.lower() == "unknown":
        planet_data_rows.remove(planet_data)
        continue
    else:
        planet_radius_value = planet_radius.split(" ")[0]
        planet_radius_ref =planet_radius.split(" ")[1]
        if planet_radius_ref =="Jupiter":
            planet_radius_value =float(planet_radius_value) *11.2
            planet_data[7] =planet_radius_value
        if planet_radius_ref =="Earth":
            planet_radius_value =float(planet_radius_value)
            planet_data[7] =planet_radius_value
            
print(len(planet_data_rows))

KOI_351=[]

for planet_data in planet_data_rows:
    if (planet_data[11] == max_solar_system):
        KOI_351.append(planet_data)

print(len(KOI_351))
print(KOI_351[0])

import plotly.express as px

KOI_351_masses=[]
KOI_351_names=[]

for planet_data in KOI_351:
    KOI_351_names.append(planet_data[1])
    KOI_351_masses.append(planet_data[3])
    
KOI_351_masses.append(1)
KOI_351_names.append('Earth')
fig =px.bar(x=KOI_351_names,y=KOI_351_masses)
fig.show()


