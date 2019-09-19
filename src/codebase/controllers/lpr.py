# pylint: disable=W0223,W0221,broad-except

import logging

from skimage import io
from hyperlpr import HyperLPR_PlateRecogntion

from codebase.web import APIRequestHandler


class LPRHandler(APIRequestHandler):

    def post(self):
        """识别车牌
        """
        body = self.get_body_json()
        url = body.pop("url")

        image = io.imread(url)
        info = HyperLPR_PlateRecogntion(image)
        if info:
            item = info[0]
            logging.info("识别车牌：%s", info)
            self.success(data={"lp": item[0], "precision": item[1], "pos": item[2]})
            return

        logging.info("识别失败：%s", url)
        self.success(status="unknown", message="车牌识别失败")
