import cv2

from src.ocr import extract_text


def visualize_ocr(image_path):

    image = cv2.imread(image_path)

    rotated_image = cv2.rotate(
        image,
        cv2.ROTATE_90_CLOCKWISE
    )

    results = extract_text(image_path)

    for bounding_box, text, confidence in results:

        top_left = tuple(
            map(int, bounding_box[0])
        )

        bottom_right = tuple(
            map(int, bounding_box[2])
        )

        cv2.rectangle(
            rotated_image,
            top_left,
            bottom_right,
            (0, 255, 0),
            2
        )

        cv2.putText(
            rotated_image,
            text,
            top_left,
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 0, 255),
            1
        )

    cv2.imwrite(
        "ocr_visualization.jpg",
        rotated_image
    )


if __name__ == "__main__":

    visualize_ocr(
        "uploads/book_image1.jpg"
    )