# Snail needs to get out of the well that is 3m deep. In every 10 minutes he advances 30cm, but then he has to take a break 1 minute, during that time he goes 20cm back. How much time will pass until the snail gets out of the well.

from datetime import timedelta

# Convert seconds to hhmmss
def conv(sec):
  min = sec // 60
  s = sec % min
  h = min // 60
  m = min % 60
  return "%02d:%02d:%02d" % (h, m, s)
  


# Setting variables
time = 0
distance = 0
distance_gain = 30
rest_distance_drop = 20
is_end = False

# Main logic
while is_end == False:

  # Move up
  distance+=distance_gain
  # Add time
  time+=10

  # Print iteration results
  print("Time is: ", time)
  print("Distance is: ", distance)
  print("-------------------")

  # Check if we hit 3 meters
  if distance >= 300:
    is_end = True
    print("OUT OF THE WELL!")
  else:

    # Resting for 1 minute
    time+=1

    # Deduct distance we lost while resting
    distance-=rest_distance_drop

# Calculate the exact time the snail reached the top of the well

difference = distance - 300
exact_time = time - (10 - 10*difference/distance_gain)
delta = timedelta(seconds=exact_time)
delta_sec = exact_time * 60

# Printing the results
print("The exact time that snail reached 3 meters and left the well is: ", conv(delta_sec))
