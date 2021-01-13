import xlrd


class ReadExcelFile:
    def read_excel(self, work, sheet):
        wb = xlrd.open_workbook(work)
        ws = wb.sheet_by_name(sheet)
        rows = ws.get_rows()
        next(rows)
        d = {row[0].value: (row[1].value, row[2].value) for row in rows}
        return d, d.keys()

    def read_test_data(self, workbook, worksheet, testcase):
        wb = xlrd.open_workbook(workbook)
        ws = wb.sheet_by_name(worksheet)
        rows = ws.get_rows()
        next(rows)
        tc = {row[0].value: (row[1].value, row[2].value, row[3].value, row[4].value, row[5].value) for row in rows}
        return tc[testcase]
