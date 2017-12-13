from abc import ABCMeta, abstractmethod


class BaseGrid():
    __metaclass__ = ABCMeta

    @abstractmethod
    def download(self):
        pass

    @abstractmethod
    def start_hub(self):
        pass

    @abstractmethod
    def add_node(self):
        pass


class Grid(BaseGrid):
    def __init__(self, ssh_client):
        self._client = ssh_client

    def download(self):
        if not self.is_file_downloaded():
            print '...Downloading selenium grid.'
            self._client.execute('wget -O selenium-server-standalone-3.8.0.jar https://goo.gl/SVuU9X')

    def start_hub(self):
        print '...Start hub'
        self._client.execute(
            'wget -O sg-node.json https://gist.github.com/extsoft/aed4cb6e0b1ae3cd1d38cafffdd79310/raw/')
        self._client.execute('java -jar selenium-server-standalone-3.8.0.jar -role hub >> log.txt 2>&1 &')

    def add_node(self):
        print '...Add node'
        self._client.execute(
            'java -jar selenium-server-standalone-3.8.0.jar -role node  -nodeConfig sg-node.json >> log.txt 2>&1 &')

    def is_file_downloaded(self):
        result = self._client.execute('test -f "selenium-server-standalone-3.8.0.jar" && echo yes')
        return True if 'yes' in str(result) else False



