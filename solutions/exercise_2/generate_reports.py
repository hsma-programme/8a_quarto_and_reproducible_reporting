from quarto_render_func import render_quarto
import pandas as pd
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

team_df = pd.read_csv("kpis_fantasy_land_mhs.csv")
teams = team_df['team'].unique()

for team in teams:
    print(f"""
###########################################
# Generating report for {team}
###########################################
          """)

    render_quarto(
        input="community_mental_health_team_dash.qmd",
        output_file=f"{team.replace(' ', '_').replace('-', '_')}_dashboard.html",
        params=[{'team':team}],
        print_command=True,
        verbose=True,
        shell=True
        )
