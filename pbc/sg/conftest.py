from pbc.sg import SshClient, Grid
import pytest


@pytest.fixture(scope='session')
def sq_fixture():
    cl = SshClient('vagrant', 'vagrant')
    grid = Grid(cl)
    grid.download()
    grid.start_hub()
    grid.add_node()
    yield cl
    cl.execute('killall java')
    cl.close()
