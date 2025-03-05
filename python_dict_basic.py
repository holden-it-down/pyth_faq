distances = {
    "voyager 1": 163,
    "voyager 2": 136,
    "pioneer 10": 80,
    "new horizons" : 58,
    "pioneer 11": 44
}

# Get all the keys

for distance in distances.keys():
  print(distance)


# Gets all the values

for distance in distances.values():
  print(distance)

# create or update a key value pair for a dictionary

distances.update("key", "value")


# get a singlue value off the key u know

distances.get("keyvalue") # returns the value if exists.
