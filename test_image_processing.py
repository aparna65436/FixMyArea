
import cv2
from src.image_processing import resize_image

image = cv2.imread("data/test.jpg")

for width in [100, 200, 400, 600]:
    resized_image = resize_image(image, width)
    print(f"Width requested: {width}")
    print("Actual shape:", resized_image.shape)
    print()