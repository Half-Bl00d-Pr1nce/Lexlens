import cv2
import easyocr


reader = easyocr.Reader(["en"])


def extract_text(image_path):

    image = cv2.imread(image_path)

    rotated_image = cv2.rotate(
    image,
    cv2.ROTATE_90_CLOCKWISE
    )

    results = reader.readtext(rotated_image)

    return results


if __name__ == "__main__":

    results = extract_text(
        "uploads/book_image1.jpg"
    )

    for result in results:

        bounding_box, text, confidence = result

        print(
            f"Text: {text} | "
            f"Confidence: {confidence:.2f}"
        )