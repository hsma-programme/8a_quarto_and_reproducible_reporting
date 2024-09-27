from quarto_render_func import render_quarto
import pandas as pd
from palmerpenguins import load_penguins

penguins_df = load_penguins()
penguin_species = penguins_df['species'].unique()

for species in penguin_species:
    render_quarto(
        input="parameterised_report.qmd",
        output_file=f"{species}_report_automated.html",
        params=[{'species':species}],
        print_command=True,
        verbose=True
        )
