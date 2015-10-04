# triangulates GPS position
#
# needs scipy

import numpy as np
import math

# try on this set.
demoPos = [[0.672308, 0.556435], [0.702773, 0.760115], [0.879798, 0.862075], [0.648783, 0.832054], [0.286069, 0.768317], [0.0742173, 0.497004]]

x = zip(*demoPos)[0]
y = zip(*demoPos)[1]




# takes position coordinates (lists) and returns [R, min_val, max_val]
def computeGPSMapper(x,y):
  # fit a line
  line_coef = np.polyfit(x, y, 1)
  theta = -math.atan2(line_coef[0], 1)
  offset = line_coef[1];
  # translate all coerdinates lower by line_coef[1] 
  points = [[p[0], p[1] - line_coef[1]] for p in demoPos]
  # rotation matrix
  R = [[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]] 
  rotated_points = np.dot(R, zip(*points))
  # normalise
  rotated_x = rotated_points[0]
  min_val = min(rotated_x)
  max_val = max(rotated_x)
  return [R, min_val, max_val]
  #final_x = [(x_val - min_val) / (max_val - min_val) for x_val in rotated_x]

# setting globals
[R, offset, min_val, max_val] = computeGPSMapper(x,y)


def placeOnALine( id, lon, lat ):
  "returns relative position in range [0,1] "
  rotated_point = np.dot(R, [lon, lat])[0]
  return (rotated_point - min_val) / (max_val - min_val)
[0.556435, 0.672308]

