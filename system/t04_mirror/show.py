from lib import BaseTest


class ShowMirror1Test(BaseTest):
    """
    show mirror: regular mirror
    """
    fixtureCmds = ["aptly mirror create mirror1 http://mirror.yandex.ru/debian/ wheezy"]
    runCmd = "aptly mirror show mirror1"


class ShowMirror2Test(BaseTest):
    """
    show mirror: missing mirror
    """
    runCmd = "aptly mirror show mirror-xx"
    expectedCode = 1


class ShowMirror3Test(BaseTest):
    """
    show mirror: regular mirror with packages
    """
    fixtureDB = True
    runCmd = "aptly mirror show --with-packages wheezy-contrib"