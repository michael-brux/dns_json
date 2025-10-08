from http.client import HTTPSConnection
from urllib.parse import urlencode
import json

ENDPOINTS = [
    ["/resolve", ["8.8.8.8", "8.8.4.4"]],
    ["/dns-query",["1.1.1.1", "1.0.0.1"]]
]
DEFAULT_ENDPOINT:list = ENDPOINTS[0]
DEFAULT_PATH:str = DEFAULT_ENDPOINT[0]
DEFAULT_HOST:str = DEFAULT_ENDPOINT[1][0]
#print(DEFAULT_PATH, DEFAULT_HOST)

class Resolver:
    def __init__(self, host:str=DEFAULT_HOST, path:str=DEFAULT_PATH):
        self.host = host
        self.path = path
        self._connection = None
        #self._response = None

    @property
    def connection(self):
        if self._connection is None:
            self._connection = HTTPSConnection(self.host)
        return self._connection

    def resolve(self, name:str="example.com", qtype:str="A"):
        query = urlencode({"name": name, "type": qtype})
        url = f"{self.path}?{query}"
        self.connection.request("GET",url)
        response = self.connection.getresponse()
        if response.status == 200:
            return json.loads(response.read().decode())
        return {"error": f"HTTP {response.status}", "message": response.reason}

    def close(self):
        if self._connection is None:
            return
        self.connection.close()
        self._connection = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

if __name__ == "__main__":
    from pprint import pprint
    with Resolver() as resolver:
        pprint(resolver.resolve())