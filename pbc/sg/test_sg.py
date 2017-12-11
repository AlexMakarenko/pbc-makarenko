def test_selenium_grid(sq_fixture):
    cl = sq_fixture
    assert len(cl.execute('pgrep java')) == 2
    log = cl.execute('cat log.txt')
    errors = []
    for row in log:
        if 'error' in row:
            print(row)
            errors.append(row)
    if errors:
        raise Exception('Errors in the log file!!!')
