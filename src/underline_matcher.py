from src.ocr import extract_text
from src.underline_detector import detect_underlines


def match_underlines(image_path):

    ocr_results = extract_text(image_path)

    rotated_image, underlines = detect_underlines(image_path)

    underlined_text = []

    for x, y, width, height in underlines:

        best_match = None
        best_distance = float("inf")

        underline_center = x + (width / 2)

        for bounding_box, text, confidence in ocr_results:

            word_x1 = min(point[0] for point in bounding_box)
            word_x2 = max(point[0] for point in bounding_box)
            word_y2 = max(point[1] for point in bounding_box)

            horizontal_overlap = (
                x < word_x2
                and (x + width) > word_x1
            )

            vertical_distance = abs(y - word_y2)

            # -----------------------------
            # NEW: Select individual word
            # -----------------------------

            selected_text = text

            words = text.split()

            cleaned_words = [
                word.strip(".,!?;:'\"()[]{}")
                for word in words
            ]

            if len(cleaned_words) > 1:

                box_width = word_x2 - word_x1

                total_characters = sum(
                    len(word)
                    for word in cleaned_words
                )

                current_x = word_x1

                for word in cleaned_words:

                    estimated_width = (
                        len(word) / total_characters
                    ) * box_width

                    estimated_x1 = current_x
                    estimated_x2 = current_x + estimated_width

                    if (
                        underline_center >= estimated_x1
                        and underline_center <= estimated_x2
                    ):
                        selected_text = word
                        break

                    current_x = estimated_x2

            else:
                selected_text = cleaned_words[0]

            # -----------------------------

            if (
                horizontal_overlap
                and vertical_distance <= 20
                and vertical_distance < best_distance
            ):

                best_match = selected_text
                best_distance = vertical_distance

        if (
            best_match is not None
            and best_match not in underlined_text
        ):
            underlined_text.append(best_match)

    return underlined_text


if __name__ == "__main__":

    image_path = "uploads/book_image1.jpg"

    underlined_words = match_underlines(image_path)

    print("\nPossible underlined text:")

    for word in underlined_words:
        print(word)