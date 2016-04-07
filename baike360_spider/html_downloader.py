import urllib.request


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return
        res = urllib.request.urlopen(url)
        if res.getcode() != 200:
            return
        return res.read()
