from JDI.web.selenium.elements.complex.table.row_column import RowColumn


class Column(RowColumn):

    def __init__(self, val):
        RowColumn.__init__(self, val)

    @staticmethod
    def column(val):
        return Column(val)