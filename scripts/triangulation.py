# triangulates GPS position
#
# needs scipy

demoPos = [[0.672308, 0.556435], [0.702773, 0.760115], [0.879798, 0.862075], [0.648783, 0.832054], [0.286069, 0.768317], [0.0742173, 0.497004]]


# normals, compute and update with computeGPSMapper
nx = 1
ny = 1
offset = 0
scale = 1

def computeGPSMapper( args ):
   "takes all know GPS locations and computes the projection on the line "
   function_suite
   return [expression]


def placeOnALine( id, lon, lat ):
   "returns relative position in range [0,1] "
   return ((lon*nx + lat*ny) + offset)*scale