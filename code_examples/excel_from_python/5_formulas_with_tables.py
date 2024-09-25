import xlsxwriter
import pandas as pd

# Create an new Excel file
writer = pd.ExcelWriter("formula_with_tables.xlsx", engine="xlsxwriter") ## NEW

hsma_store_items_df = pd.DataFrame([
    {"Item": "HSMA T-Shirts", "Units": 500 , "Unit Cost": 11.99},
    {"Item": "I <3 HSMA Bumper Stickers", "Units": 3000, "Unit Cost": 0.30},
    {"Item": "HSMA Cat Bowls", "Units": 10, "Unit Cost": 15}

    ])

hsma_store_items_df.to_excel(writer, sheet_name="HSMA Store",
                             index=False, startrow=1, header=False)

# Get the xlsxwriter workbook and worksheet objects.
workbook = writer.book
worksheet = writer.sheets["HSMA Store"]

# Create a list of column headers, to use in add_table().
column_settings = [{"header": column} for column in hsma_store_items_df.columns]

# Add the Excel table structure. Pandas will add the data.
worksheet.add_table(0, 0,
                    len(hsma_store_items_df),
                    len(hsma_store_items_df.columns) - 1,
                    {"columns": column_settings, 'name': 'Stock'})

for row in range(len(hsma_store_items_df)):
    worksheet.write_formula(row+1, 3, '=Stock[@[Units]]*Stock[@[Unit Cost]]')

writer.close()
