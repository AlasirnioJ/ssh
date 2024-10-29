
class SpreadSheet:

    def __init__(self):
        self._cells = {}

    def set(self, cell: str, value: str) -> None:
        self._cells[cell] = value

    def evaluate(self, cell: str):
        value = self._cells[cell]
        try:
            return int(value)
        except ValueError:
            try:
                float(value)
                return "#Error"
            except ValueError:
                return value

