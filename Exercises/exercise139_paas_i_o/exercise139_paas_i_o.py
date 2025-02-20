"""PAAS I/O exercise"""

from io import BufferedRandom

class MeteredFile(BufferedRandom):
    """A wrapper that counts the total bytes read and written and the amount of read and write
    operations. Implemented as a subclass.
 
    :param file BufferedRandom: The file stream to be monitored.
    """

    def __init__(self, *args, **kwargs):

        super().__init__(self, *args, **kwargs)
        self._read_bytes = 0
        self._read_ops = 0
        self._write_bytes = 0
        self._write_ops = 0

    def __enter__(self):

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):

        return super().__exit__(exc_type, exc_val, exc_tb)

    def __iter__(self):

        return self

    def __next__(self):

        line = super().readline()
        if not line:
            raise StopIteration
        self._read_bytes += len(line)
        self._read_ops += 1
        return line

    def read(self, size=-1):

        data = super().read(size)
        self._read_bytes += len(data)
        self._read_ops += 1
        return data

    @property
    def read_bytes(self) -> int:
        """The total amount of bytes read."""

        return self._read_bytes

    @property
    def read_ops(self) -> int:
        """The total amount of read operations performed."""

        return self._read_ops

    def write(self, b):

        written = super().write(b)
        self._write_bytes += written
        self._write_ops += 1
        return written

    @property
    def write_bytes(self) -> int:
        """The total amount of bytes written."""

        return self._write_bytes

    @property
    def write_ops(self) -> int:
        """The total amount of write operations performed."""

        return self._write_ops

class MeteredSocket:
    """A wrapper that counts the total bytes read and written and the amount of read and write
    operations. Implemented with delegation."""

    def __init__(self, socket):

        self._socket = socket
        self._recv_bytes = 0
        self._recv_ops = 0
        self._send_bytes = 0
        self._send_ops = 0

    def __enter__(self):

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):

        return self._socket.__exit__(exc_type, exc_val, exc_tb)

    def recv(self, bufsize, flags=0):
        """Receive data and register its length."""

        received = self._socket.recv(bufsize, flags)
        self._recv_bytes += len(received)
        self._recv_ops += 1
        return received

    @property
    def recv_bytes(self) -> int:
        """The total amount of bytes received."""

        return self._recv_bytes

    @property
    def recv_ops(self) -> int:
        """The total amount of receipt operations."""

        return self._recv_ops

    def send(self, data, flags=0):
        """Send data and register its amount."""

        sent = self._socket.send(data, flags)
        self._send_bytes += sent
        self._send_ops += 1
        return sent

    @property
    def send_bytes(self) -> int:
        """The total amount of bytes sent."""

        return self._send_bytes

    @property
    def send_ops(self) -> int:
        """The total amount of send operations performed."""

        return self._send_ops
