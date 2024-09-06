import cv2 as cv

# lire une image
img = cv.imread("assets/ton_image.jpg")

# Redimensionner une image
img = cv.resize(img, (700, 500))

# Recadrer une image
cropped_img = img[0:200, 200:500]

# CrEer une matrice 5x5 avec 1 comme elements
kernel = np.ones((5, 5))

# BrouillEr une image
blur_img = cv.GaussianBlur(img, (13, 13), 0)

# determiner les bords sur une image
canny_img = cv.Canny(blur_img, 100, 100)

# Augmenter l'epaisseur des bords detectEs
dilated_img = cv.dilate(
    canny_img,
    kernel,
    iterations=1,
)

# Transformer une image du BGR(Blue,Green,Red) -> GRAY(gris)
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


# Afficher les images
cv.imshow("image", img) # image Originale
cv.imshow("Cropped image", cropped_img)
cv.imshow("Blur image", blur_img)
cv.imshow("Dilated image", dilated_img)
cv.imshow("kanny image", canny_img)

# Ajouter un delais lors de la lecture si 0 l'image va s'afficher d'une maniere permanante
cv.waitKey(0)
