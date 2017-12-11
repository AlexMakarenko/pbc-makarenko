class Grid:
    def __init__(self, ssh_client):
        self._client = ssh_client

    def is_file_downloaded(self):
        result = self._client.execute('test -f "selenium-server-standalone-3.8.0.jar" && echo yes')
        if 'yes' in str(result):
            return True

    def start_hub(self):
        print '...Start hub'
        self._client.execute('java -jar selenium-server-standalone-3.8.0.jar -role hub >> log.txt 2>&1 &')

    def download(self):
        if not self.is_file_downloaded():
            print '...Downloading selenium grid.'
            self._client.execute('wget -O selenium-server-standalone-3.8.0.jar https://goo.gl/SVuU9X')

    def add_node(self):
        print '...Add node'
        self._client.execute(
            'java -jar selenium-server-standalone-3.8.0.jar -role node  -hub http://localhost:4444/grid/register >> log.txt 2>&1 &')
