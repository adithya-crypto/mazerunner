import sknw
import cv2
from skimage.morphology import skeletonize
import networkx as nx


def image(name):
    # Open Maze image
    img = cv2.imread(name)
    # kernel = np.ones((1,1),np.uint8)

    # Convert to GrayScaledImage
    grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # BınaryThreshold + OtsuThreshold + BinaryThreshold
    retval, threshold = cv2.threshold(
        grayscaled, 10, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
    )
    retval, threshold2 = cv2.threshold(threshold, 10, 255, cv2.THRESH_BINARY_INV)
    threshold2[threshold2 == 255] = 1

    # Skeletonize the Thresholded Image
    skel = skeletonize(threshold2)
    return skel, img


def TreeGeneration(skel):
    tree = sknw.build_sknw(skel, multi=False)
    T = nx.Graph(tree)
    return T, tree
