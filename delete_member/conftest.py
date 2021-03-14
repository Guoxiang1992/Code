# -- coding: utf-8 --
# @File : conftest.py
import logging
logging.basicConfig(level=logging.INFO, #info级别日志
                    # 定义日志输出格式（时间、代码所在文件名、代码行号、日志级别名字、日志信息）
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    # 打印日志的时间并规定它的格式
                    datefmt='%a, %Y %m %d %H:%M:%S ',
                    filemode= 'a'
                    )
logger=logging.getLogger()