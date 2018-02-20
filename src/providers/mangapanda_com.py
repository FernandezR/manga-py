from src.provider import Provider
from .helpers.std import Std


class MangaPandaCom(Provider, Std):

    def get_archive_name(self) -> str:
        idx = self.get_chapter_index().split('-')
        return 'vol_{:0>3}-{}'.format(*idx)

    def get_chapter_index(self) -> str:
        idx = self.re.search(r'\.com/[^/]+/([^/]+)', self.get_current_chapter()).group(1)
        return '{}-0'.format(idx)

    def get_main_content(self):
        return self.http_get('{}/{}'.format(self.get_domain(), self.get_manga_name()))

    def get_manga_name(self) -> str:
        return self.re.search(r'\.com/([^/]+)', self.get_url()).group(1)

    def get_chapters(self):
        return self._elements('#listing a')

    def get_files(self):
        img_selector = '#imgholder img'
        url = self.http().normalize_uri(self.get_current_chapter())

        parser = self.html_fromstring(url, '#container', 0)
        count_pages = parser.cssselect('#selectpage option + option')

        count_pages = len(count_pages)
        images = self._images_helper(parser, img_selector)

        n = 1
        while n < count_pages:
            parser = self.html_fromstring('{}/{}'.format(url, 1 + n))
            images += self._images_helper(parser, img_selector)
            n += 1

        return images

    def get_cover(self):
        pass  # TODO


main = MangaPandaCom
