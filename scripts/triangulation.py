# triangulates GPS position
#
# needs scipy

import numpy as np
import math

# try on this set.
demoPos = [[0.672308, 0.556435], [0.702773, 0.760115], [0.879798, 0.862075], [0.648783, 0.832054], [0.286069, 0.768317], [0.0742173, 0.497004]]

x = zip(*demoPos)[0]
y = zip(*demoPos)[1]

# declare variables that might be useful outside fn scope
min_val = 0
max_val = 0
R = 0

# takes position coordinates (lists)
def computeGPSMapper(x,y):
  # fit a line
	line_coef = np.polyfit(x, y, 1)
  theta = -math.atan2(line_coef[0], 1)
  # translate all coerdinates lower by line_coef[1] 
  points = [[p[0], p[1] - line_coef[1]] for p in demoPos]
  # rotation matrix
  R = [[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]] 
  rotated_points = np.dot(R, zip(*points))
  # normalise
  rotated_x = rotated_points[0]
  min_val = min(rotated_x)
  max_val = max(rotated_x)
  #final_x = [(x_val - min_val) / (max_val - min_val) for x_val in rotated_x]



def placeOnALine( id, lon, lat ):
  "returns relative position in range [0,1] "
  rotated_points = np.dot(R, zip(*points))
  return ((lon*nx + lat*ny) + offset)*scale


  