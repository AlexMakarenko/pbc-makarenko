import paramiko


class SshClient:
    def __init__(self, username, password):
        self._username = username
        self._password = password
        self._address = '192.168.33.10'
        self._client = self._connect()

    def _connect(self):
        print('...Connecting to {}@{}'.format(self._username, self._address))
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        client.connect(self._address, username=self._username, password=self._password, timeout=10)
        print('...Connected!')
        return client

    def execute(self, command):
        result = []
        if self._client:
            stdin, stdout, stderr = self._client.exec_command(command)
            for row in stdout:
                # print(row)
                result.append(str(row))
            return result
        else:
            print("...Connection not opened.")

    def close(self):
        self._client.close()
        print('...SSH connection closed!')
