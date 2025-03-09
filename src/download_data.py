"""
This script downloads NFL play-by-play data for user-specified seasons
and saves that data locally in Excel format for inspection.

Author: Ed Murphy
"""

import nfl_data_py as nfl
import os

# manually set NFL season of interest
season_to_download = 2024

# manually set location for local output of data to .xlsx
output_path = os.path.join(os.getcwd(), 'data')

# Check if directory exists, create it if it doesn't
if not os.path.exists(output_path):
    os.makedirs(output_path)

plays = nfl.import_pbp_data(years=range(season_to_download, season_to_download + 1))

output_file = os.path.join(output_path, f"every_nfl_play_{season_to_download}_season.xlsx")

plays.to_excel(output_file, index=False)

print(f"Data for every play of the {season_to_download} season has been written to {output_path}")
