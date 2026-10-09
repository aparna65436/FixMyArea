import cv2
from src.image_processing import resize_image
image = cv2.imread("data/test.jpg")

resized_image = resize_image(image, 200)

print("Resized shape:", resized_image.shape)