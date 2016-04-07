import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup


class HtmlParser(object):
    def __init__(self):
        self.new_urls = set()
        # self.res_data = dict()

    def _get_new_urls(self, page_url, soup):
        # new_urls = set()
        # /doc/5912108-6125016.html或/doc/3745498.html
        links = soup.find_all('a', href=re.compile(r'/doc/[\d-]+\.html'))
        for link in links:
            new_url = link['href']
            new_full_url = urljoin(page_url, new_url)
            # print(new_full_url)
            self.new_urls.add(new_full_url)
        return self.new_urls

    def _get_new_data(self, page_url, soup):
        res_data = dict()
        # url
        res_data['url'] = page_url
        # <span class="title">Python</span>
        title_node = soup.find('span', class_='title')
        res_data['title'] = title_node.get_text()
        # <div class="card_content" id="js-card-content">
        summary_node = soup.find('div', class_='card_content').find('p')
        res_data['summary'] = summary_node.get_text()
        # print("dd: ", self.res_data)
        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data
