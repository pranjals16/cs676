# Feature matching using FLANN

import cv2

def matchFeatures(img1, img2):
  # Initiate SIFT detector
  sift = cv2.SIFT()

  # find the keypoints and descriptors with SIFT
  kp1, des1 = sift.detectAndCompute(img1,None)
  kp2, des2 = sift.detectAndCompute(img2,None)

  # FLANN parameters
  FLANN_INDEX_KDTREE = 0
  index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
  search_params = dict(checks=50)   # or pass empty dictionary

  flann = cv2.FlannBasedMatcher(index_params,search_params)

  matches = flann.knnMatch(des1,des2,k=2)

  good = []
  pts1 = []
  pts2 = []

  # ratio test as per Lowe's paper
  for i,(m,n) in enumerate(matches):
    if m.distance < 0.8*n.distance:
      good.append(m)
      pts2.append(kp2[m.trainIdx].pt)
      pts1.append(kp1[m.queryIdx].pt)

  return (pts1, pts2)
