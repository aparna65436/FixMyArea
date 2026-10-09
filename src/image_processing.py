import cv2


def resize_image(image, new_width=400):
    """Resize an image while preserving its aspect ratio."""

    if image is None:
        raise ValueError("Image could not be loaded.")

    if new_width <= 0:
        raise ValueError("Width must be greater than zero.")

    original_height, original_width = image.shape[:2]

    new_height = int(
        original_height * new_width / original_width
    )

    resized_image = cv2.resize(
        image, (new_width, new_height)
    )

    return resized_image


if __name__ == "__main__":
    # Read the image
    image = cv2.imread("data/test.jpg")

    if image is None:
        raise FileNotFoundError(
            "Could not find or read data/test.jpg"
        )

    # Resize the image
    resized_image = resize_image(image)

    # Save the resized image
    cv2.imwrite("data/resized_test.jpg", resized_image)

    # Print dimensions
    print("Original shape:", image.shape)
    print("Resized shape:", resized_image.shape)

    # Display image
    cv2.imshow("Resized FixMyArea Image", resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

