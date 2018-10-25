import os
import logging

from flask import Flask, flash, request, jsonify
from werkzeug.utils import secure_filename

from .formula_detection import detect_formula

UPLOAD_FOLDER = "/tmp/pepper_uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
ALLOWED_EXTENSIONS = set(["jpg"])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

logging.basicConfig(level=logging.INFO)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/calculate', methods=['POST'])
def calculate():
    # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return jsonify({
            "success": True,
            "result": "No file part in POST request"
        })
    file = request.files['file']

    # if user does not select file, browser also
    # submit an empty part without filename
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        target_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(target_path)

        formula = detect_formula(target_path)
        app.logger.info("Detected formula '%s'", formula)

        # calculate
        try:
            result = eval(formula)
        except SyntaxError:
            app.logger.info("No valid formula detected to validate")
            return jsonify({
                "success": False,
                "result": "no valid formula"
            })

        app.logger.info("Calculate formula '%s' and got result '%d'",
                formula, result)
        return jsonify({
            "success": True,
            "result": result
        })

    return jsonify({
        "success": True,
        "result": "Please upload a formula"
    })
