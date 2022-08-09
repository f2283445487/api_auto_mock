import logging


def init_logger(name):
    logger = logging.getLogger(name)
    logger.handlers.clear()
    formatter = logging.Formatter('%(asctime)s : %(message)s', "%Y-%m-%d %H:%M:%S")
    file_handler = logging.FileHandler("./log/api_auto.log", mode='a')
    file_handler.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    return logger


def api_log(func):
    def log(self, *args, **kwargs):
        func(self, *args, **kwargs)
        init_logger(self.route).info(
            "请求url:{}---请求体json:{}---返回码{}".format(self.url, self.api_json, self.res.status_code))
        return

    return log
