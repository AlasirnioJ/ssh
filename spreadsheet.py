
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
            if value.startswith("'") and value.endswith("'"):
                return value[1:-1]
            try:
                float(value)
                return "#Error"
            except ValueError:
                return "#Error"  # This line is modified to return "#Error" for improperly quoted strings or other invalid inputs.

