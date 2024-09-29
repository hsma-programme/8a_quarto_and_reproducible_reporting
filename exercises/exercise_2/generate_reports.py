from quarto_render_func import render_quarto
import pandas as pd
import os

# Change the directory to the location of the current file
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Read in the csv
## YOUR CODE HERE

# Get a list of unique team names
## YOUR CODE HERE

# Iterate through team names

    # Print a message indicating the team you are about to work on

    # Run the render function for each team
    render_quarto(
        input=## YOUR CODE HERE,
        output_file=## YOUR CODE HERE,
        params=## YOUR CODE HERE,
        print_command=True,
        verbose=True
        )
