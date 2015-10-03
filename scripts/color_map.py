# Specs
# 
# Two Functions:
# 1. Phase: phones with projected position > 0.5 have color inverted
# 2. Wave: need to insert more elements and map the same colors to lower values of colour
#
# Assume: list of [ pos, timestamp, color]
#         where pos is GPS position in range [0 or 1] 
#         where color is either 0 or 1. 

doWaveAtTime = -1 # some big number or -1 to skip
doPhaseAtTime = -1

baseColor = (1.0,1.0,1.0) #white

def toHashColor(color):
  triplet = (int(color*255*baseColor[0]), int(color*255*baseColor[1]), int(color*255*baseColor[2]))
  return '#'+''.join(map(chr, triplet)).encode('hex')


def phase( args ):
  " "
  x = [0]*len(demoPos)
  y = [0]*len(demoPos)
  for i in range(0, len(demoPos)):
    y[i] = demoPos[i][0]
    x[i] = demoPos[i][1]
  coef = numpy.polyfit(x,y, 2)
  return [expression]