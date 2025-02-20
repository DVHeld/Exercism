"""React exercise"""

class InputCell:
    """A simple input cell. Notifies the compute cells dependent on it if its value changes."""

    def __init__(self, initial_value):

        if not isinstance(initial_value, int):
            raise TypeError("The input must be a number.")

        self._value = initial_value
        self._dependent_cells = set()

    @property
    def value(self):
        """The cell's value.
 
        :return int: The value.
        """

        return self._value

    @value.setter
    def value(self, new_value):

        if not isinstance(new_value, int):
            raise TypeError("The input must be a number.")

        if new_value != self._value:
            self._value = new_value
            for cell in self._dependent_cells:
                cell.update()
            for cell in self._dependent_cells:
                cell.trigger_callback()

    def add_dependent_cell(self, cell):
        """Adds a dependent compute cell to this cell´s list.
 
        :param ComputeCell cell: The dependent compute cell.
        """

        self._dependent_cells.add(cell)

class ComputeCell:
    """A compute cell. Stores its current value and the compute function. Notifies the compute
    cells dependent on it if its value changes."""

    def __init__(self, inputs, compute_function):
        if not isinstance(inputs, list):
            raise TypeError("The input must be a list.")
        if not callable(compute_function):
            raise TypeError("The compute function must be a callable type.")

        self.inputs = inputs
        self.compute_function = compute_function
        self._value = compute_function([cell.value for cell in inputs])
        self._dependent_cells = set()
        self._was_updated = False
        self._old_value = self._value
        self._callbacks = set()
        for cell in inputs:
            cell.add_dependent_cell(self)

    @property
    def value(self):
        """This cell's value."""

        return self._value

    def add_dependent_cell(self, cell):
        """Adds a dependent compute cell to this cell´s list.
 
        :param ComputeCell cell: The dependent compute cell.
        """

        self._dependent_cells.add(cell)

    def update(self):
        """Recomputes this cell's value. Called by a parent cell when its value changes."""

        new_value = self.compute_function([cell.value for cell in self.inputs])
        if self._value != new_value:
            self._value = new_value
            for cell in self._dependent_cells:
                cell.update()
            self._was_updated = True
            if new_value == self._old_value:

                self._was_updated = False
    def trigger_callback(self):
        """Triggers a callback to this cell's registered callbacks."""

        if self._was_updated:
            for callback in self._callbacks:
                callback(self._value)
            self._old_value = self._value
            for cell in self._dependent_cells:
                cell.trigger_callback()
            self._was_updated = False

    def add_callback(self, callback):
        """Add a callbacl to the corresponding list.
 
        :param function callback: The callback function to be added.
        :raises TypeError: Raised when the provided input is not a callable.
        """

        if not callable(callback):
            raise TypeError("The callback function must be a callable")

        self._callbacks.add(callback)

    def remove_callback(self, callback):
        """Removes a callback function from this cell's list.
 
        :param function callback: The callb ack to be removed.
        """

        if callback in self._callbacks:
            self._callbacks.remove(callback)
