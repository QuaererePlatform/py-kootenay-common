from willamette_common.schemas import (
    WebSiteFieldsMixinV1,
    WebPageFieldsMixinV1,
    WebPageSchemaV1,
    WebSiteSchemaV1)


def test_web_site():
    _ = WebSiteSchemaV1()
    _ = WebSiteFieldsMixinV1()


def test_web_page():
    _ = WebPageSchemaV1()
    _ = WebPageFieldsMixinV1()
