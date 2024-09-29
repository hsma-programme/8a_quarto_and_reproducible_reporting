import xlsxwriter
import pandas as pd
from datetime import datetime

bed_state_df = pd.read_csv("bed_state_input_data.csv")
todays_date = datetime.today()
todays_date_ymd = todays_date.strftime('%Y-%m-%d')
todays_date_dmy = todays_date.strftime('%A %d %b %Y')

with pd.ExcelWriter(f"bed_state.xlsx", engine="xlsxwriter") as writer:
    # YOUR CODE HERE
