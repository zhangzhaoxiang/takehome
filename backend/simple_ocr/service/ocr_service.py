from aip import AipOcr
from config import config
from utility import CONST
from database import ocr_database

ocr_client = AipOcr(appId=config.appId, apiKey=config.apiKey,
                    secretKey=config.secretKey)


def general_image(file):
    """
    general OCR
    :param file: image file
    :return: {"content": [ 'Letter1', 'Letter2'...]}
    """
    if not file:
        return {"content": None, "message": CONST.NO_FILE}
    # file type
    filename = file.filename
    if not filename.lower().endswith(CONST.IMAGE_TYPE):
        return {"content": None, "message": CONST.FILE_TYPE_ERROR}

    # read image content
    content = ocr_database.read_image_content(file)

    # OCR use baidu API
    response = ocr_client.basicGeneral(content)
    # print(response)
    """
    {
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
    """

    # OCR response process
    content = ocr_database.ocr_response_process(response)
    result = {'content': content, 'message': CONST.SUCCESS}
    # save data

    return result
