from typing import Callable, List
class Message():
    """
    Stores the notes and their new colors.
    All functions return themselves (except for xy), so you can chain calls.
    To get the actual sysex data (not including the 0xF0 to start and 0xF7 to end the message),
    call the object like a function.

    Example:
    msg = Message().row(0, 1, 0.5, 0.25)
    msg.note(1, 1, 1, 0.5, 0.25).note(8, 1, 1, 0.5, 0.25)
    data = msg()
    """
    rgb_header = [0x00, 0x20, 0x29, 0x02, 0x18, 0x0B]

    def __init__(self):
        self.data = {}

    def __call__(self) -> List:
        """
        Returns the data formatted correctly as a sysex message.
        The returned list is ready to be put into any MIDI message library, such as mido.
        """
        sysex_data = Message.rgb_header[:]
        for k, v in self.data.items():
            sysex_data += [k] + v
        return sysex_data

    def xy(self, x: int, y: int):
        """
        Convinence function to convert an x and y coordinate into the ID of the cooresponding LED.
        LEDs are numbered from 11 to 89. The first row is 11 thru 19, second row is 21 thru 19, etc.
        Only works in session mode, so don't switch to user mode. (That can only be done with another sysex message, so you won't mess it up unless you try.)
        """
        return (y + 1) * 10 + (x + 1)

    def range(self, x1: int, y1: int, x2: int, y2: int, red: float, green: float, blue: float):
        """
        Sets a range of LEDs to the provided color.
        """
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                self.data[self.xy(x, y)] = [red*63, green*63, blue*63]
        return self

    def range_func(self, x1: int, y1: int, x2: int, y2: int, function: Callable[[int, int], List[float]]):
        """
        Sets a range of LEDs to a color provided by a function.
        The function should take an x and y coordinate and return a list with 3 float values from 0 to 1.
        """
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                generated_data = function(x, y)
                cleaned_data = [0, 0, 0]
                for i in range(3):
                    if i < len(generated_data):
                        cleaned_data[i] = generated_data * 63
                self.data[self.xy(x, y)] = cleaned_data
        return self

    def row(self, row: int, red: float, green: float, blue: float):
        """
        Sets an entire row of LEDs to the provided color.
        """
        self.range(0, row, 7, row, red, green, blue)
        return self

    def col(self, col: int, red: float, green: float, blue: float):
        """
        Sets an entire column of LEDs to the provided color.
        """
        self.range(row, 0, row, 7, red, green, blue)
        return self

    def note(self, x: int, y: int, red: float, green: float, blue: float):
        """
        Sets a single LED to the provided color.
        """
        self.data[self.xy(x, y)] = [red*63, green*63, blue*63]
        return self
