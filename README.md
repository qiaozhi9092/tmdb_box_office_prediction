# TMDB Box Office Prediction

## Prerequisites
1. Kaggle command line tool (`pip install kaggle`)
2. Kaggle API Key
    - To get this, go to Kaggle.com > "My Account", then Ctrl-F for
      "API". Download an API key and store it at `~/.kaggle/kaggle.json`
3. Python 3.7
    - This is somewhat arbitrary and may change.

## Installation
It's probably best to use a Python virtual environment with this project. Replace `pip` with whatever the proper `pip` executable is called on your system.

This may or may not work, but gives the general idea.
```shell
git clone https://github.com/eldrtimo/tmdb_box_office_prediction
cd tmdb_box_office_prediction
pip install -r requirements.txt
```

## Project Intent
The goals of this project are to:
1. develop methods for effective collaboration on a data science project
2. submit competitive predictions of box office revenue in satisfaction of the
   Kaggle TMBD Box Office Prediction Challenge.

## Organization
The directory tree shall be structured as follows:
- `notebooks` - directory for Jupyter notebooks for prototyping analysis
- `figures` - containing figures
- `tmdb` - Python module for project-related functionality
- `data` - Data directory. This directory shall be excluded from repository. It
  will be created and populated by the Makefile.
    - `data/raw` - directory for raw data downloaded from Kaggle
    - `data/processed` - directory for processed data ready for analysis
- `docs` - Project documentation.

## Creating New Notebooks
Create new notebooks in the `notebooks` directory.

In order to access the project modules using `import tmbd`, each notebook must begin with the following code at the beginning:
```python
import os
import sys
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)
import tmbd
```

## Makefile
The Makefile shall contain targets allowing the user to:
- download data from Kaggle
- process and clean data
- refresh notebooks and figures after change in data processing methods
- submit predictions to Kaggle

## Collaboration
Team members will add their contributions to the project by creating notebooks. When an idea is sufficiently demonstrated out in a notebook, it will be incorporated into the `tmbd` Python module so that it can be shared across the entire project.
