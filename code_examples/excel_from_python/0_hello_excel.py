import xlsxwriter

# Create an new Excel file
workbook = xlsxwriter.Workbook("hello_excel.xlsx")
# Add a worksheet
worksheet = workbook.add_worksheet()

# Text with formatting.
worksheet.write("A1", "Hello Excel")

workbook.close()
