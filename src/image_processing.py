import cv2


def preprocess_image(image_path):

    image = cv2.imread(image_path)

    gray_image = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    processed_image = cv2.threshold(
        gray_image,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]

    return processed_image

if __name__ == "__main__":

    processed_image = preprocess_image(
        "uploads/book_image1.jpg"
    )

    success = cv2.imwrite(
        "processed_image.jpg",
        processed_image
    )

    print("Image saved:", success)