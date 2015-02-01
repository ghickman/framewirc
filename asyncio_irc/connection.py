import asyncio

from .message import Message


class Connection:
    """
    Communicates with an IRC network.

    Incoming data is transformed into Message objects, and dispatched to
    methods defined in `listeners`.
    """

    def __init__(self, listeners, host, port):
        self.listeners = listeners
        self.host = host
        self.port = port
        self.ssl = True

    @asyncio.coroutine
    def connect(self):
        """Connect to the server, and dispatch incoming messages."""
        connection = asyncio.open_connection(self.host, self.port, ssl=self.ssl)
        self.reader, self.writer = yield from connection

        self.on_connect()

        self._connected = True
        while self._connected:
            message = yield from self.reader.readline()
            if not message:
                self.disconnect()
                return
            self.handle(message)

    def disconnect(self):
        """Close the connection to the server."""
        self._connected = False
        self.writer.close()
        self.on_disconnect()

    def handle(self, raw_message):
        message = Message(raw_message)
        for listener in self.listeners:
            listener.handle(self, message)

    def on_connect(self):
        self.send(b'USER meshybot 0 * :MeshyBot7')
        self.send(b'NICK meshybot')

    def on_disconnect(self):
        print('Connection closed')

    def send(self, message):
        message = message + b'\r\n'
        print('write', message)
        self.writer.write(message)