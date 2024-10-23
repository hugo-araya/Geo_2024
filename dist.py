import math
lat1 = -33.4398
lon1 = -70.65503
lat2 = -35.434637
lon2 = -71.6206103
R = 6378
dlat = math.pi/180*(lat2 - lat1)
dlon = math.pi/180*(lon2 - lon1)
"""
a = sin²(Δlat/2) + cos(lat1) · cos(lat2) · sin²(Δlong/2)
c = 2 · atan2(√a, √(1−a))
d = R · c
"""
a = math.sin(dlat/2)*math.sin(dlat/2) + math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)*math.sin(dlon/2)
c = 2 * math.atan2(math.sqrt(a),math.sqrt(1-a))
d = R*c
print(d)