# Find camera matrices
import cv2
import numpy as np

def getCalibrationMatrix(img):
  rows, cols, _ = img.shape
  maxWH = max(rows, cols)
  return np.array([[maxWH, 0, cols/2.0], [0, maxWH, rows/2.0], [0, 0, 1]])

def getEssentialMatrix(fundamentalMatrix, calibrationMatrix):
  calibrationMatrixT = calibrationMatrix.T
  return (calibrationMatrixT.dot(fundamentalMatrix)).dot(calibrationMatrix)

def decomposeEtoRandT(E):
  w, u, vt = cv2.SVDecomp(E)
  W = np.array([[0,-1,0],[1,0,0],[0,1,1]])
  Wt = W.T
  R1 = (u.dot(W)).dot(vt)
  R2 = (u.dot(Wt)).dot(vt)
  t1 = u[:,2]
  t2 = -u[:,2]
  return (R1, R2, t1, t2)

def findCameraMatrix(E):
  (R1, R2, t1, t2) = decomposeEtoRandT(E)
  P1 = np.array([[R1[0,0],R1[0,1],R1[0,2],t1[0]],
                 [R1[1,0],R1[1,1],R1[1,2],t1[1]],
                 [R1[2,0],R1[2,1],R1[2,2],t1[2]]])
  return P1

