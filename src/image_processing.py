import cv2

def resize_image(image, new_width=400):
    if image is None:
        raise ValueError("Image could not be loaded.")
    original_height, original_width = image.shape[:2]

    new_height = int(original_height * new_width / original_width)

    resized_image = cv2.resize(image, (new_width, new_height))

    return resized_image


# Read the image
image = cv2.imread("data/test.jpg")

# Resize the image
resized_image = resize_image(image)

# Save the resized image
cv2.imwrite("data/resized_test.jpg", resized_image)

# Print dimensions
print(resized_image.shape)

# Display image
cv2.imshow("Resized FixMyArea Image", resized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()