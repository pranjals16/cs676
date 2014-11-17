# Implementation of SfM

import sys
import cv2
import numpy as np
from featureMatcher import matchFeatures
from findCameraMatrices import *
from Triangulation import TriangulatePoints
from createPCD import writePointCloud

if __name__ == "__main__":
  if len(sys.argv) != 3:
    print "Usage: ", sys.argv[0], "<image_1> <image_2>"
    exit(1)

  print "Reading images..."

  img1 = cv2.imread(sys.argv[1])
  img2 = cv2.imread(sys.argv[2])

  print "Finding and matching features..."
  (pts1, pts2) = matchFeatures(img1, img2)

  pts1 = np.float32(pts1)
  pts2 = np.float32(pts2)

  print "Calculating fundamental matrix..."
  F, mask = cv2.findFundamentalMat(pts1,pts2,cv2.FM_RANSAC,0.006*np.amax(pts1),0.99)

  print "Calculating essential matrix..."
  K = getCalibrationMatrix(img1)

  E = getEssentialMatrix(F, K)

  print "Calculating camera matrix..."
  P1 = findCameraMatrix(E)

  # P is the canonical matrix
  P = np.array([[1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0]])

  pointCloud = TriangulatePoints(pts1, pts2, K, P, P1)
  writePointCloud(pointCloud)
