import pandas as pd

# Create an new Excel file
writer = pd.ExcelWriter("3_working_with_dataframes.xlsx", engine="xlsxwriter") ## NEW

# # Add a bold format
# bold = workbook.add_format({"bold": True})

# # Add a currency format
# currency_format = workbook.add_format({'num_format': '£#,##0.00'})

hsma_store_items_df = pd.DataFrame([
    {"Item": "HSMA T-Shirts", "Units": 500 , "Unit Cost": 11.99},
    {"Item": "I <3 HSMA Bumper Stickers", "Units": 3000, "Unit Cost": 0.30},
    {"Item": "HSMA Cat Bowls", "Units": 10, "Unit Cost": 15}

    ])

hsma_store_items_df.to_excel(writer, sheet_name="HSMA Store", index=False)

writer.close()
