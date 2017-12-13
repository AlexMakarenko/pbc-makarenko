from pbc.sg import Grid, SshClient
import pytest
from time import sleep




@pytest.fixture()
def grid(request):
    cl = SshClient('vagrant', 'vagrant')
    grid = Grid(cl)
    grid.download()
    grid.start_hub()
    grid.add_node()
    sleep(5)
    def fin():
        # cl.execute('rm log.txt')
        # cl.execute('killall java')
        cl.close()
    request.addfinalizer(fin)