from pbc.sg import Grid


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
    log = ssh_cl.execute('cat log.txt')
    assert not 'error' in str(log)


def test_sg_ui(browser, ssh_cl):
    grid = Grid(ssh_cl)
    grid.download()
    grid.start_hub()
    grid.add_node()
    browser.navigate("http://192.168.33.10:4444/grid/console")
    browser.execute_script('location.reload();')
    assert len(browser.xpath('//img[contains(@src, "firefox")]', wait=True, ttl=10)) == 5
