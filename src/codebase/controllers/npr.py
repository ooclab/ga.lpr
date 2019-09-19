# pylint: disable=W0223,W0221,broad-except

import logging

from skimage import io
from hyperlpr import HyperLPR_PlateRecogntion

from codebase.web import APIRequestHandler


class NPRHandler(APIRequestHandler):

    def post(self):
        """识别车牌
        """
        body = self.get_body_json()
        url = body.pop("url")

        image = io.imread(url)
        info = HyperLPR_PlateRecogntion(image)
        logging.info("识别车牌：%s", info)
        self.success(data=info)
