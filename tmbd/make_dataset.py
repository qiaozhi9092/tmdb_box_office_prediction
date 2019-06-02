import os
from pathlib import Path

# CAUTION: this breaks when installed in site-packages.
ROOT_DIR = Path(__file__).parent.parent
RAW_DATA_DIR = ROOT_DIR.joinpath("data/raw")
PROCESSED_DATA_DIR = ROOT_DIR.joinpath("data/raw")
