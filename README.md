# IPEDS Tables
This package will generate Rda files for each table in the access databases produced by the National center for educational statistics as part of the IPEDS report. 

The package will be on CRAN soon. 

This package is very much still a work in progress. All the functional aspects are done but using the script will take some editing for your local environment. 

The script should be pointed at the directory where all the .accdb files are stored. The script will then find the accdb files in that directory, and pipe them into the extraction pipeline.
This workflow could very easily be refactored into a parallel process and that is on the todo list.
