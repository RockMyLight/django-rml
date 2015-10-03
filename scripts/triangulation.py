# triangulates GPS position
#
# needs scipy

import numpy

# try on this set.
demoPos = [[0.672308, 0.556435], [0.702773, 0.760115], [0.879798, 0.862075], [0.648783, 0.832054], [0.286069, 0.768317], [0.0742173, 0.497004]]


# normals, compute and update with computeGPSMapper
nx = 1
ny = 1
offset = 0
scale = 1

def computeGPSMapper( args ):
  "takes all know GPS locations and computes the projection on the line "
  x = [0]*len(demoPos)
  y = [0]*len(demoPos)
  for i in range(0, len(demoPos)):
    y[i] = demoPos[i][0]
    x[i] = demoPos[i][1]
  coef = numpy.polyfit(x,y, 2)
  return [expression]


def placeOnALine( id, lon, lat ):
  "returns relative position in range [0,1] "
  return ((lon*nx + lat*ny) + offset)*scale