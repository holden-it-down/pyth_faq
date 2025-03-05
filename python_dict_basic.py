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

# going through all keys and values with dict.items()

for a, b in dict.items():
    print(a, b)

# Removing a certain key element pair on your dict with DICT.POP()

distances.pop("keyname") 


# How to delete the dict or the contents of all the keys and values

distances.clear()
