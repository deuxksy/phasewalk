from selenium import webdriver
from commons import log
from setting import redis_pool_common
from setting import config
import os
import logging
import redis
import json
import traceback

logger = log.get_logger(logger=logging.getLogger(os.path.basename(__file__).split('.')[0]), config=config)


class FreeProxyList(object):
    def __init__(self, url, *args, **kwargs):
        self.url = url
        self.redis_common = redis.Redis(connection_pool=redis_pool_common)
        self.init(*args, **kwargs)

    def __del__(self):
        if self.webdriver:
            self.webdriver.close()

    def init(self):
        # browser = config.get('default', 'browser')
        browser = 'phantomjs'
        executable_path = config.get('default', '{}.executable.path'.format(browser))
        if 'phantomjs' == browser:
            self.webdriver = webdriver.PhantomJS(executable_path=executable_path)
        elif 'chrome' == browser:
            self.webdriver = webdriver.Chrome(executable_path=executable_path)
        elif 'firefox' == browser:
            self.webdriver = webdriver.Firefox(executable_path=executable_path)

    def get_proxy_list(self):
        proxy_list = []
        self.webdriver.get(self.url)
        proxies = self.webdriver.find_elements_by_xpath('//table[@class="DataGrid"]/tbody/tr[@class!="Caption"][td[1]/a]')
        for proxy in proxies:
            try:
                proxy_list.append({
                    'ip': proxy.find_element_by_xpath('./td[1]').text,
                    'port': int(proxy.find_element_by_xpath('./td[2]').text),
                    'protocol': proxy.find_element_by_xpath('./td[3]').text.lower(),
                    'country': proxy.find_element_by_xpath('./td[5]').text,
                })
            except Exception:
                logger.error(traceback.format_exc())
        return proxy_list

    def save(self, proxy_list):
        if proxy_list:
            self.redis_common.delete('proxy:http')
            self.redis_common.delete('proxy:https')

        for proxy in proxy_list:
            self.redis_common.lpush('proxy:{}'.format(proxy.get('protocol')), json.dumps(proxy,sort_keys=True,separators=(',', ':')))

    def main(self):
        proxy_list = self.get_proxy_list()
        self.save(proxy_list)

