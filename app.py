from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def upload_image():

    if request.method == "POST":

        image = request.files["image"]

        image_path = os.path.join(
            app.config["UPLOAD_FOLDER"],
            image.filename
        )

        image.save(image_path)

        return "Image uploaded successfully!"

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)