# contoh penggunaan openpyxl

from openpyxl import Workbook, load_workbook

# membuka file excel
wb = load_workbook("Book1.xlsx")

# membaca worksheet
ws = wb["Sheet1"]

# membaca Cell
print(ws["A2"].value)

# membaca cell
# perhitungan row dan column dimulai dari 1 (bukan 0)
print(ws.cell(row=1, column=2).value)