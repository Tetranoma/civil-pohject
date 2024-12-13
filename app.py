import math

def distance(lat1, lon1, lat2, lon2):
  """
  Distance function that takes in two lat/lon pairs and returns the distance in miles.
  """
  lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
  dlon = lon2 - lon1
  dlat = lat2 - lat1
  a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
  c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
  radius = 3956.0
  return radius * c

def bearing(lat1, lon1, lat2, lon2):
  """
  Bearing function that takes in two lat/lon pairs and returns the bearing in degrees.
  """
  lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
  dlon = lon2 - lon1
  x = math.sin(dlon) * math.cos(lat2)
  y = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(dlon)
  initial_bearing = math.atan2(x, y)
  initial_bearing = math.degrees(initial_bearing)
  return (initial_bearing + 360) % 360

def shoelace_area(data):
  """
  Shoelace area function that takes in a list of lat/lon pairs and returns the area of the polygon.
  """
  n = len(data)
  data.append(data[0])
  area = 0.0
  for i in range(n):
    xi, yi = data[i]
    xn, yn = data[i + 1]
    area += xi * yn - yi * xn
  return abs(area) / 2.0

def main():
  count = int(input("Enter Number of Data Coordinates: "))
  data = []
  for i in range(count):
    lat = float(input("Enter Latitude: "))
    lon = float(input("Enter Longitude: "))
    data.append([lat, lon])
  perimeter = 0
  for i in range(len(data) - 1):
    lat1, lon1 = data[i]
    lat2, lon2 = data[i + 1]
    dist = distance(lat1, lon1, lat2, lon2)
    perimeter += dist
    bear = bearing(lat1, lon1, lat2, lon2)
    print(f"From coordinates {data[i][0]}, {data[i][1]} to {data[i + 1][0]}, {data[i + 1][1]}:\nDistance: {dist} miles\nBearing: {bear} degrees\n")
  print(f"Perimeter: {perimeter} miles\n")
  area = shoelace_area(data)
  print(f"Area: {area} square miles")

if __name__=="__main__":
  main()