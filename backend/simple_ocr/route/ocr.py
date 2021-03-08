from flask import Blueprint, request, jsonify, make_response

from service import ocr_service

app_ocr = Blueprint("ocr", __name__, url_prefix="/ocr")


@app_ocr.route("/general_image", methods=['POST'])
def general_image():
    """
    general OCR
    :return:
    """
    file = request.files.get("image")
    result = ocr_service.general_image(file)
    return make_response(jsonify(result))
