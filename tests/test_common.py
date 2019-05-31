from willamette_common import (
    WebSiteBase, WebPageBase, WebPageSchema, WebSiteSchema)


def test_web_site():
    _ = WebSiteSchema()
    _ = WebSiteBase()


def test_web_page():
    _ = WebPageSchema()
    _ = WebPageBase()
