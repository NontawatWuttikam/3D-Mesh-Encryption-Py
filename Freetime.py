#########################################################
#                                                       #
#   These Code has nothing to do with the project       #
#                                                       #
#                                                       #
#########################################################

import cv2
import numpy as np

centCol = 0
centCol2 = 0
centCol3 = 0


while True:
    a = np.zeros((200,200,3), np.uint8)
    flag = None
    flag2 = None
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            if (i-100)**2 + (j-(centCol))**2 <= 20**2:
                if flag is None:
                    flag = [i,j-20]
                a[i,j,0] = (255*(i - flag[0]))/40
                a[i,j,1] = (255*(j - flag[1]))/40
                a[i,j,2] = (255*(i - flag[0]))/40
            if (i-centCol2)**2 + (j-(100))**2 <= 20**2:
                if flag2 is None:
                    flag2 = [i,j-20]
                a[i,j,0] = (255*(i - flag2[0]))/40
                a[i,j,1] = (255*(j - flag2[1]))/40
                a[i,j,2] = (255*(j - flag2[1]))/40
            if (i-centCol3)**2 + (j-(centCol3))**2 <= 20**2:
                if flag2 is None:
                    flag2 = [i,j-20]
                a[i,j,0] = (255*(i - flag2[0]))/40
                a[i,j,1] = (255*(j - flag2[1]))/40
                a[i,j,2] = (255*(j - flag2[1]))/40
    centCol = (centCol + 3) % 200
    centCol3 = (centCol + 5) % 200

    centCol2 = (centCol2 + 7) % 200

    # print(centCol)
    cv2.imshow('rolling ball',a)
    cv2.waitKey(1)