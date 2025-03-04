

# While loops
i = 0
while i < 3:
  print("cool")
  i = i + 1

  

# For loops
# the pythonic way of doing something as while did but cleaner + use of range function
  for _ in range(3):
    print("cool")


# While True loops

# using a break statement in an infinite loop to run the loop at least once

while True:
  n = int(input("enter a number: "))
  if n > 0:
    break

