import xlsxwriter
import pandas as pd
from datetime import datetime

bed_state_df = pd.read_csv("bed_state_input_data.csv")
todays_date = datetime.today()
todays_date_ymd = todays_date.strftime('%Y-%m-%d')
todays_date_dmy = todays_date.strftime('%A %d %b %Y')

with pd.ExcelWriter(f"{todays_date_ymd}_bed_state.xlsx", engine="xlsxwriter") as writer:

    start_row = 5

    bed_state_df.to_excel(writer,
                          sheet_name="Bed State",
                          index=False,
                          startrow=start_row,
                          header=False)

    # Get the xlsxwriter workbook and worksheet objects.
    workbook = writer.book
    worksheet = writer.sheets["Bed State"]

    max_row, max_col = bed_state_df.shape
    max_row += start_row - 1
    col_names = bed_state_df.columns.tolist()

    #######################
    # Add in the title bits
    ########################
    bold = workbook.add_format({"bold": True})
    italic = workbook.add_format({"italic": True})

    worksheet.write("A1", "HSMA Hospitals Trust: Mental Health Bedstock Report", bold)
    worksheet.write("A2", todays_date_dmy, italic)

    worksheet.write("A4", "By Ward", bold)

    ####################
    # Add in a formula #
    ####################

    # Add the Total column header
    # worksheet.write(3, max_col, "Available Beds")

    # Add the formula for each row in the Total column
    for row in range(start_row, max_row+1):
        formula = f'=C{row+1}-D{row+1}-E{row+1}'
        worksheet.write_formula(row, max_col, formula)

    max_col += 1

    col_names.append("Available Beds")

    for row in range(start_row, max_row+1):
        formula = f'=(E{row+1}+D{row+1})/C{row+1}'
        worksheet.write_formula(row, max_col, formula)

    max_col += 1

    col_names.append("Occupancy")

    percent_format = workbook.add_format({"num_format": ".1%"})

    # Apply the number format to Grade column.
    worksheet.set_column(6, 6, None, percent_format)

    # Create a list of column headers, to use in add_table().
    column_settings = [
        {"header": column}
        for column
        in col_names]

    # Add the Excel table structure. Pandas will add the data.
    worksheet.add_table(start_row,
                        0,
                        max_row,
                        max_col - 1,
                        {"columns": column_settings,
                        'name': 'Stock',
                        'style': 'Table Style Light 9',
                        'banded_rows': False,
                        'first_column': True
                        })

    start_position_summary_table = len(bed_state_df) + 10

    worksheet.write(start_position_summary_table-2, 0, "By Ward", bold)

    worksheet.write(start_position_summary_table, 0, "Specialty", bold)

    worksheet.write(start_position_summary_table, 1, "Available Beds", bold)

    for i, specialty in enumerate(bed_state_df["Specialty"].sort_values().unique()):
        worksheet.write(
            start_position_summary_table+1+i,
            0,
            specialty
            )

        formula_sumif = f'=SUMIF(B{start_row+1}:B{max_row+1}, "{specialty}", F{start_row+1}:F{max_row+1})'

        worksheet.write_formula(
            start_position_summary_table+1+i,
            1,
            formula_sumif
            )

    # Autofit
    worksheet.autofit()
