# -*- coding: utf-8 -*-
import datetime
import json
import logging
import os

from concurrent_log_handler import ConcurrentRotatingFileHandler

from conf.config import LOG_PATH, DATE_TIME_FORMAT, DEBUG_MODE


def create_logger(file_path=LOG_PATH):
    # file_util.prepare_path(file_path)

    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)
    # write log to console
    handler_console = logging.StreamHandler()
    handler_console.setLevel(logging.INFO)
    handler_console.setFormatter(JSONFormatter())
    log.addHandler(handler_console)

    if DEBUG_MODE:
        err_handler = ConcurrentRotatingFileHandler(os.path.join(file_path, "err.log"), maxBytes=3 * 1024 * 1024,
                                                    backupCount=10, encoding="utf_8")
        err_handler.setLevel(logging.INFO)
        err_handler.setFormatter(JSONFormatter())
        err_filter = logging.Filter()
        err_filter.filter = lambda record: record.levelno >= logging.ERROR
        err_handler.addFilter(err_filter)

        warn_handler = ConcurrentRotatingFileHandler(os.path.join(file_path, "warn.log"), maxBytes=3 * 1024 * 1024,
                                                     backupCount=10, encoding="utf_8")
        warn_handler.setLevel(logging.INFO)
        warn_handler.setFormatter(JSONFormatter())
        warn_filter = logging.Filter()
        warn_filter.filter = lambda record: record.levelno == logging.WARN
        warn_handler.addFilter(warn_filter)

        info_handler = ConcurrentRotatingFileHandler(os.path.join(file_path, "info.log"), maxBytes=3 * 1024 * 1024,
                                                     backupCount=10, encoding="utf_8")
        info_handler.setLevel(logging.INFO)
        info_handler.setFormatter(JSONFormatter())
        info_filter = logging.Filter()
        info_filter.filter = lambda record: record.levelno == logging.INFO
        info_handler.addFilter(info_filter)

        log.addHandler(err_handler)
        log.addHandler(warn_handler)
        log.addHandler(info_handler)
    return log


class JSONFormatter(logging.Formatter):

    def format(self, record):
        extra = {
            'time': datetime.datetime.fromtimestamp(record.created).strftime(DATE_TIME_FORMAT),
            'level': record.levelname,
            'pathname': record.pathname,
            'lineno': record.lineno
        }
        if record.args:
            extra['msg'] = "'" + record.msg + "'," + str(record.args).strip('()')
        else:
            extra['msg'] = record.msg
        if record.exc_info:
            extra['exc_info'] = self.formatException(record.exc_info)
        if self._fmt == 'pretty':
            return json.dumps(extra, indent=2, ensure_ascii=False)

        return json.dumps(extra, ensure_ascii=False)


logger = create_logger()

if __name__ == '__main__':
    logger.info({"a": 1})
    logger.error("Do something")
    logger.warning("Something maybe fail.")
    logger.exception("Something maybe fail.")

    # # pylint test
    # logger.info("股票 4 {}_{}".format("code", "date_str"), "函数:{} ".format("res"))
    # logger.info("股票 4 %s_%s" % ("code", "date_str"), "函数:%s " % "res")
    # logger.info("this is "  "a test %s", 123)
    # logger.info("this is a test %s", 123)
