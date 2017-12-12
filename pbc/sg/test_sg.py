from time import sleep
from pbc.sg import StartGrid



def test_processes(ssh_cl):
    StartGrid(ssh_cl)
    try:
        assert len(ssh_cl.execute('pgrep java')) == 2
        print('Two java processes are running.')
    except AssertionError:
        raise


def test_errors_in_logs(ssh_cl):
    StartGrid(ssh_cl)
    log = ssh_cl.execute('cat log.txt')
    errors = []
    for row in log:
        if 'error' in row.lower():
            print(row)
            errors.append(row)
    if errors:
        raise Exception('Errors in the log file!!!')
    print("No errors in log file.")


def test_sg_ui(browser, ssh_cl):
    StartGrid(ssh_cl)
    browser.navigate("http://192.168.33.10:4444/grid/console")
    counter = 15
    while counter > 0:
        try:
            assert len(browser.xpath('//img[contains(@src, "firefox")]')) == 5
            print("Selenium grid works!")
            break
        except AssertionError:
            browser.execute_script('location.reload();')
            counter -= 1
            sleep(1)
    else:
        raise Exception('Selenium grid doesn\'t work!')
