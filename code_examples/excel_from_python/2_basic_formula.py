import xlsxwriter

# Create an new Excel file
workbook = xlsxwriter.Workbook("basic_formula.xlsx")
# Add a worksheet
worksheet = workbook.add_worksheet("HSMA Store")

# Add a bold format
bold = workbook.add_format({"bold": True})

# Add a currency format
currency_format = workbook.add_format({'num_format': '£#,##0.00'})

# Text with formatting
worksheet.write("A1", "Item", bold)
worksheet.write("B1", "Units", bold)
worksheet.write("C1", "Unit Cost", bold)
worksheet.write("D1", "Total Cost", bold) ## NEW

# Write some entries with row/column notation
# in the format worksheet.write(row, column, value)
worksheet.write(1, 0, "HSMA T-Shirts")
worksheet.write(1, 1, 500)
worksheet.write(1, 2, 11.99, currency_format)
worksheet.write_formula(1, 3, '=B2*C2', currency_format)

worksheet.write(2, 0, "I <3 HSMA Bumper Stickers")
worksheet.write(2, 1, 3000)
worksheet.write(2, 2, 0.30, currency_format)
worksheet.write_formula(2, 3, '=B3*C3', currency_format)

worksheet.write(3, 0, "HSMA Cat Bowls")
worksheet.write(3, 1, 10)
worksheet.write(3, 2, 15, currency_format)
worksheet.write_formula(3, 3, '=B4*C4', currency_format)

worksheet.write_formula(4, 3, '=SUM(D2:D4)', currency_format)

workbook.close()
