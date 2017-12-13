from pbc.sg import Grid
from time import sleep
import requests
from bs4 import BeautifulSoup


def test_processes(ssh_cl):
    grid = Grid(ssh_cl)
    grid.download()
    grid.start_hub()
    grid.add_node()
    assert len(ssh_cl.execute('pgrep java')) == 2


def test_errors_in_logs(ssh_cl):
    grid = Grid(ssh_cl)
    grid.download()
    grid.start_hub()
    grid.add_node()
    assert not 'error' in str(ssh_cl.execute('cat log.txt'))


def test_sg_ui(browser, ssh_cl):
    grid = Grid(ssh_cl)
    grid.download()
    grid.start_hub()
    grid.add_node()
    browser.navigate("http://192.168.33.10:4444/grid/console")
    sleep(2)
    browser.execute_script('location.reload();')
    assert len(browser.xpath('//img[contains(@src, "firefox")]', wait=True, ttl=10)) == 5


def test_sg_rest(ssh_cl):
    grid = Grid(ssh_cl)
    grid.download()
    grid.start_hub()
    grid.add_node()
    sleep(5)
    r = requests.get('http://192.168.33.10:4444/grid/console')
    soup = BeautifulSoup(r.text, 'html.parser')
    firefox_browsers = [x for x in soup.find_all('img') if str(x['src']).endswith('firefox.png')]
    assert len(firefox_browsers) == 5
