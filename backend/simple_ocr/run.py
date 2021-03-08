from flask import Flask
from route.ocr import app_ocr

app = Flask(__name__)

app.register_blueprint(app_ocr)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3080, debug=True, threaded=True)
