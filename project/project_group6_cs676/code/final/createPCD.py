# Write point cloud data to PCD

f = open("data.pcd", "w")

def writeHeaders(points):
  f.write("VERSION .7\nFIELDS x y z\nSIZE 4 4 4\nTYPE F F F\nCOUNT 1 1 1\nWIDTH ")
  f.write(str(points) + "\n")
  f.write("HEIGHT 1\nPOINTS ")
  f.write(str(points) + "\n")
  f.write("DATA ascii\n")

def writePointCloud(pointCloud):
  points = len(pointCloud)
  writeHeaders(points)
  for p in pointCloud:
    f.write(str(p[0]) + " " + str(p[1]) + " " + str(p[2]) + "\n")
