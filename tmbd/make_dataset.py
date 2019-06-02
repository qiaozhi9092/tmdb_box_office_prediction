import os
from pathlib import Path

# CAUTION: this breaks when installed in site-packages.
ROOT_DIR = Path(__file__).parent.parent            # Project root
RAW_DATA_DIR       = ROOT_DIR.joinpath("data/raw") # Directory for raw data
PROCESSED_DATA_DIR = ROOT_DIR.joinpath("data/raw") # Directory for processed data
FIG_DIR            = ROOT_DIR.joinpath("figures")  # Directory for figures
