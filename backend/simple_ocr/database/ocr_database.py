import io
from PIL import Image


def read_image_content(file):
    """
    read image content from fileStorage
    :param file:
    :return:
    """
    im = Image.open(file)
    img_byte = io.BytesIO()
    im.save(img_byte, format='PNG')
    content = img_byte.getvalue()
    return content


def ocr_response_process(response):
    """
    OCR response process
    :param response:
    :return: ['Letter1', 'Letter2'...]
    """
    content = []
    if response.get('words_result'):
        for one in response['words_result']:
            content.append(one['words'])
    return content


if __name__ == '__main__':
    demo1 = {
        'words_result': [{
            'words': 'TRUE PEACE'
        }, {
            'words': 'IS THE'
        }, {
            'words': 'PRESENCE'
        }, {
            'words': 'OF JUSTICE'
        }],
        'log_id': 1368075975727775744,
        'words_result_num': 4
    }
    print(ocr_response_process(demo1))
