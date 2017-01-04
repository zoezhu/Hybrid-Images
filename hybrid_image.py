# Key Method: Impliment the first picture with laplacian pyramid, while the second one with Gaussian pyramid
# Principle: The difference between laplacian pyramid and Gaussian pyramid is that, the first one is calculated based on the seconde one, when we shrink a picture by half, the picture losses half of its information, we continue to shirnk it, we get a pyramid of pictures with less information, that is Gaussian pyramid. (Then we amplify the pictures to original size, the total imformation is the same as the small one. So the picture stays at low frequency which is blur.) Based on Gaussian pyramid, if we use original picture substracts the later one which contains less information we will get lossed information and that will be the lines of the picture which is high frequency, and that groups of substractions constitude laplacian pyramid.

import cv2
import numpy as np

# An important thing here is that the pictures' width and length should can be divided by 2**layer, layer is a variable we can see later
A = cv2.imread('/Users/zz/Desktop/h7.jpeg') # high picture
B = cv2.imread('/Users/zz/Desktop/zzt1.jpeg') # low picture

# Layer is the times we shrink and amplify the origin picture by half or double
layer = 4
new_A = [A.copy()]
new_B = B.copy()

# Shrink those two pictures first, for we need the difference between the result and origin ones of the first picture, we need to store the last layer of picture A
for i in range(layer):
    # pyrDown is the function to shrink the picture by half
    lower_A = cv2.pyrDown(new_A[i])
    new_A.append(lower_A)
    new_B = cv2.pyrDown(new_B)

up_A = new_A[layer]
for i in range(layer):
    # pyrUp is the function to double amplify thepicture
    up_A = cv2.pyrUp(up_A)
    # By double layer times, we get new_B is what we want. (Gaussian pyramid)
    new_B = cv2.pyrUp(new_B)

# What we need from A is the difference between origin picture and result picture. (laplacian pyramid)
first_p = cv2.subtract(A, up_A)

result = cv2.add(first_p, new_B)

cv2.imwrite('/Users/zz/Desktop/hh_1.png',first_p) # high frequency
cv2.imwrite('/Users/zz/Desktop/hh_2.png',new_B) # low frequency
cv2.imwrite('/Users/zz/Desktop/result_h.png',result) # hybrid image
