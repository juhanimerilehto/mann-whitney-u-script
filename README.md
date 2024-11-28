# Mann-Whitney U Script

**Version 1.0**
### Creator: Juhani Merilehto - @juhanimerilehto - Jyväskylä University of Applied Sciences (JAMK), Likes institute

![JAMK Likes Logo](./assets/likes_str_logo.png)

## Overview

Mann-Whitney U Test script. This Python-based tool enables automated non-parametric analysis for comparing distributions between two independent groups. Developed for the Strategic Exercise Information and Research unit in Likes Institute, at JAMK University of Applied Sciences, this module provides comprehensive statistical output including effect sizes, visualizations, and detailed distribution analysis.

## Features

- **Complete Non-parametric Analysis**: Mann-Whitney U test with effect sizes
- **Distribution Analysis**: Comprehensive comparison of group distributions
- **Effect Size Calculations**: Standardized test statistics and interpretations
- **Advanced Visualizations**: Box plots, violin plots, and distribution overlays
- **Excel Integration**: Detailed statistical reports with descriptive measures
- **Terminal Feedback**: Clear presentation of test statistics and effect sizes
- **Tested**: Tested with simulated data

## Hardware Requirements

- **Python:** 3.8 or higher
- **RAM:** 8GB recommended
- **Storage:** 1GB free space for analysis outputs
- **OS:** Windows 10/11, MacOS, or Linux

## Installation

### 1. Clone the repository:
```bash
git clone https://github.com/juhanimerilehto/mann-whitney-u-script.git
cd mann-whitney-u-script
```

### 2. Create a virtual environment:
```bash
python -m venv stats-env
source stats-env/bin/activate  # For Windows: stats-env\Scripts\activate
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Basic usage:
```bash
python mann-whitney-u.py
```

With custom parameters:
```bash
python mann-whitney-u.py --excel_path "your_data.xlsx" --group_column "Group" --value_column "Value"
```

## Configuration Parameters

- `excel_path`: Path to Excel file (default: 'data.xlsx')
- `group_column`: Column containing group labels (default: 'Group')
- `value_column`: Column containing measurements (default: 'Value')
- `group1_name`: Name of first group (default: 'Control')
- `group2_name`: Name of second group (default: 'Treatment')
- `output_prefix`: Prefix for output files (default: 'mannwhitney')

## File Structure

```plaintext
├── mann-whitney-u-script/
│   ├── assets/
│   │   └── likes_str_logo.png
│   ├── mann-whitney-u.py
│   ├── requirements.txt
│   └── README.md
```

## Credits

- **Juhani Merilehto (@juhanimerilehto)** – Specialist, Data and Statistics
- **JAMK Likes** – Organization sponsor

## License

This project is licensed for free use under the condition that proper credit is given to Juhani Merilehto (@juhanimerilehto) and JAMK Likes institute. You are free to use, modify, and distribute this project, provided that you mention the original author and institution and do not hold them liable for any consequences arising from the use of the software.