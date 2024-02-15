# Scipandas

## Aim
The aim of this toolbox is to provide high-performance tools, data structures, and data analysis tools.

## Target OS
Windows 10

## Library
Interfaced with Pandas

## Source Code
[GitHub Repository](https://github.com/pandas-dev/pandas)

## Directory Structure
- **src**: Contains the required files to run the gateway functions
- **sci_gateway**: Codes for gateway functions
- **python**: Python files essential for running the toolbox
- **macros**: Library macros
- **locales**: Localization of the toolbox
- **jar**: Jar file for the help document
- **help**: Help documents for the functions
- **etc**: Start and quit files for the library
- **examples**: Examples of implementing the gateway functions

## Requirements
- Scilab 6.1.0 – Desktop for Windows
- Python 3.8.3 from Windows Store
- Pandas library (install using `python -m pip install pandas`)

## Steps to Build
1. Define the required builder files.
2. Start the build of the toolbox by running `builder.sce` or using `atomsInstall('path_to_zip_file')` in Scilab.

## Steps to Load
1. Make sure the PYTHONPATH environment variable is set.
2. Add the Python folder located in `path_to_installed_scipandas_folder\sci_gateway\` to PYTHONPATH.
   Note: This can be done after building the toolbox.
