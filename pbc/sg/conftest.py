from pbc.sg import SshClient
from selenium.webdriver import Firefox
from elementium.drivers.se import SeElements
import pytest


@pytest.fixture(scope='module')
def ssh_cl(request):
    cl = SshClient('vagrant', 'vagrant')
    def fin():
        cl.execute('rm log.txt')
        cl.execute('killall java')
        cl.close()
    request.addfinalizer(fin)
    return cl


@pytest.fixture()
def browser(request):
    driver = Firefox()
    se = SeElements(driver)
    request.addfinalizer(driver.quit)
    return se
