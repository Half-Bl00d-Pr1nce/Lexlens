import cv2


def detect_underlines(image_path):

    image = cv2.imread(image_path)

    rotated_image = cv2.rotate(
        image,
        cv2.ROTATE_90_CLOCKWISE
    )

    gray_image = cv2.cvtColor(
        rotated_image,
        cv2.COLOR_BGR2GRAY
    )

    binary_image = cv2.threshold(
        gray_image,
        0,
        255,
        cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
    )[1]

    horizontal_kernel = cv2.getStructuringElement(
        cv2.MORPH_RECT,
        (20, 1)
    )

    horizontal_lines = cv2.morphologyEx(
        binary_image,
        cv2.MORPH_OPEN,
        horizontal_kernel
    )

    contours, _ = cv2.findContours(
        horizontal_lines,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    underlines = []

    for contour in contours:

        x, y, width, height = cv2.boundingRect(contour)

        if width >= 40 and height < 10:

            underlines.append(
                (x, y, width, height)
            )

    return rotated_image, underlines


if __name__ == "__main__":

    image, underlines = detect_underlines(
        "uploads/book_image5.jpg"
    )

    for x, y, width, height in underlines:

        cv2.rectangle(
            image,
            (x, y),
            (x + width, y + height),
            (0, 0, 255),
            2
        )

    cv2.imwrite(
        "underline_visualization5.jpg",
        image
    )

    print(
        f"Detected {len(underlines)} possible underlines"
    )