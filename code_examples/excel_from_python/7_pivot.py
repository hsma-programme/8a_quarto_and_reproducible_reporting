import xlsxwriter
import pandas as pd

hsma_store_items_df = pd.DataFrame([
    {"Item": "HSMA T-Shirts", "Category": "Clothing", "Units": 500 , "Unit Cost": 11.99},
    {"Item": "I <3 HSMA Bumper Stickers", "Category": "Stickers", "Units": 3000, "Unit Cost": 0.30},
    {"Item": "HSMA Cat Bowls", "Category": "Pets", "Units": 10, "Unit Cost": 15},
    {"Item": "HSMA Wooly Hats", "Category": "Clothing", "Units": 300 , "Unit Cost": 13.99},
    {"Item": "I <3 HSMA Socks", "Category": "Clothing", "Units": 1000 , "Unit Cost": 4.99},
    {"Item": "Find the Future in You Logo Sticker", "Category": "Stickers", "Units": 1000, "Unit Cost": 0.10},
    ])

with pd.ExcelWriter("7_pivot.xlsx", engine="xlsxwriter") as writer:

    hsma_store_items_df.to_excel(writer, sheet_name="HSMA Store",
                                index=False, startrow=1, header=False)

    # Get the xlsxwriter workbook and worksheet objects.
    workbook = writer.book
    worksheet = writer.sheets["HSMA Store"]

    max_row, max_col = hsma_store_items_df.shape
    col_names = hsma_store_items_df.columns.tolist()

    ####################
    # Add in a formula #
    ####################

    # Add the Total column header
    worksheet.write(0, max_col, "Total")

    # Add the formula for each row in the Total column
    for row in range(1, max_row+1):
        formula = f'=C{row+1}*D{row+1}'
        worksheet.write_formula(row, max_col, formula)

    max_col += 1

    col_names.append("Total")

    # Create a list of column headers, to use in add_table().
    column_settings = [
        {"header": column}
        for column
        in col_names]

    # Add the Excel table structure. Pandas will add the data.
    worksheet.add_table(0, 0,
                        max_row,
                        max_col - 1,
                        {"columns": column_settings,
                        'name': 'Stock',
                        'style': 'Table Style Medium 9',
                        'banded_rows': False,
                        'first_column': True
                        })

    ####################
    # Add in a chart
    ####################

    chart = workbook.add_chart({'type': 'column'})
    chart.add_series(
        # [sheetname, first_row, first_col, last_row, last_col]
        {'values': ['HSMA Store', 1, 3, max_row, 3],
         'categories': ['HSMA Store', 1, 0, max_row, 0],
         'name': 'Stock Value'}
        )
    chart.set_x_axis({
    'name': 'Product',
    'name_font': {'size': 18, 'bold': True},
    })
    chart.set_y_axis({
    'name': 'Total Value',
    'name_font': {'size': 18, 'bold': True},
    })
    chart.set_title({'name': 'HSMA Merchandise Stock'})
    # Insert the chart into the worksheet.
    worksheet.insert_chart(1, 6, chart)

    ####################
    # Add in a 'pivot table'
    ####################
    # Unfortunately xlsxwriter doesn't have a dedicated method
    # for creating a true Excel pivot table, so we have to think how to do
    # this ourselves.

    # First let's think of what we want
    # We want a row per category of merchandise

    start_position = len(hsma_store_items_df) + 5

    bold = workbook.add_format({"bold": True})

    worksheet.write(start_position, 0, "Category", bold)

    worksheet.write(start_position, 1, "Stock Value Summary", bold)

    worksheet.write(start_position, 2, "Products in Category", bold)


    for i, category in enumerate(hsma_store_items_df["Category"].unique()):
        worksheet.write(
            start_position+1+i,
            0,
            category
            )

        formula_sumif = f'=SUMIF(B2:B{len(hsma_store_items_df)+1}, "{category}", E2:E{len(hsma_store_items_df)+1})'

        worksheet.write_formula(
            start_position+1+i,
            1,
            formula_sumif
            )

        formula_countif = f'=COUNTIF(B2:B{len(hsma_store_items_df)+1}, "{category}")'

        worksheet.write_formula(
            start_position+1+i,
            2,
            formula_countif
            )


    # Autofit
    worksheet.autofit()
