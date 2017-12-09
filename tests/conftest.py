import paramiko
import pytest
from time import sleep


@pytest.fixture(scope='session')
def setup_fixture():
    print('\nConnecting to virtual machine.')
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect('192.168.33.10', username='vagrant', password='vagrant')
    print('Connected!')
    stdin, stdout, stderr = client.exec_command('hostname')
    for line in stdout:
        print('... ' + line.strip('\n'))
    # download
    client.exec_command('wget -O selenium-server-standalone-3.8.0.jar https://goo.gl/SVuU9X')
    sleep(30)
    # run hub
    client.exec_command('java -jar selenium-server-standalone-3.8.0.jar -role hub >> log.txt 2>&1 &')
    # run node
    client.exec_command(
        'java -jar selenium-server-standalone-3.8.0.jar -role node -hub http://localhost:4444/grid/register >> log.txt 2>&1 &')
    # find processes; returns 2 PIDs
    stdin, stdout, stderr = client.exec_command('pgrep java')
    sleep(2)
    processes = []
    for line in stdout:
        print('... ' + line.strip('\n'))
        processes.append(line)
    print('processes: {}'.format(processes))
    yield processes
    # clean up
    client.exec_command('killall java')  # kill processes
    client.close()
    print('Connection closed!')
