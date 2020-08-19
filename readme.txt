README
-----------------------------------------------------------------------------

Scipandas
Aim of the toolbox: To provide high performance tools and data structures and data analysis tools
Target OS : Windows 10.
Library Interfaced:Pandas
Source code link: https://github.com/pandas-dev/pandas 
Directory Structure:
src: this directory contains the required files to run the       gateway functions
sci_gateway: this folder contains the codes for gateway functions
python : contains the python files essential for running the tool box 
macros : contains lib macro of the toolbox 
locales: contains the localization of the tool box 
jar: contains the jar file for the help document
help: contains the help documents for the functions
etc: contains the start and the quit file for the library
examples: contains examples of implementing the gateway functions.
Requirements:
Scilab 6.1.0 – Desktop for Windows
Python 3.8.3 from windows store
Pandas library, this can installed using python –m pip install pandas

Steps to build the toolbox: The required builder files must be defined to build the toolbox. We have to start the build of the toolbox in two ways, either by running builder.sce or by using atomsInstall(‘path_to_zip_file’) in scilab. 

Steps to load the toolbox: We have to make sure that the PYTHONPATH environment variable is set, and add the Python folder located in path_to_installed(extracted)_scipandas_folder\sci_gateway\ to PYTHONPATH
Note: This can be done after building the toolbox.

















