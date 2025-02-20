"""Circular Buffer exercise"""

class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.
 
    :param str message: explanation of the error.
    """
    def __init__(self, message):
        self.message = message
class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.
 
    :param str message: explanation of the error.
    """
    def __init__(self, message):
        self.message = message
class CircularBuffer:
    """A circular buffer.
 
    Stores items in a circular buffer of the given capacity.
    """

    def __init__(self, capacity,/):

        self.capacity = capacity
        self.buffer = []
        self.buffer_next, self.buffer_oldest = 0, 0
        self.buffer = list(None for _ in range(capacity))

    def read(self):
        """Reads and deletes the oldest element in the buffer.
 
        :raises BufferEmptyException: Raised when the buffer is empty.
        :return any: The read data.
        """

        if self.buffer[self.buffer_oldest] is None:
            raise BufferEmptyException("Circular buffer is empty")
        read_data = self.buffer[self.buffer_oldest]
        self.buffer[self.buffer_oldest] = None
        self.buffer_oldest = (self.buffer_oldest+1) % self.capacity
        return read_data

    def write(self, data,/):
        """Writes data to the next empty slot in the buffer.
 
        :param any data: The data to be stored.
        :raises BufferFullException: Raised when the buffer is full.
        """

        if self.buffer[self.buffer_next] is not None:
            raise BufferFullException("Circular buffer is full")
        self.buffer[self.buffer_next] = data
        self.buffer_next = (self.buffer_next+1) % self.capacity

    def overwrite(self, data,/):
        """Forces a write to the buffer. If the buffer is full, the oldest element is overwritten.
 
        :param any data: The data to be stored.
        """

        if self.buffer[self.buffer_next] is None:
            self.buffer[self.buffer_next] = data
            self.buffer_next = (self.buffer_next+1) % self.capacity
        else:
            self.buffer[self.buffer_oldest] = data
            self.buffer_oldest = (self.buffer_oldest+1) % self.capacity

    def clear(self):
        """Clears the buffer."""

        self.__init__(self.capacity)
