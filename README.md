# IPEDS Tables
This package will generate Rda files for each table in the access databases produced by the National center for educational statistics as part of the IPEDS report. 

The package will be on CRAN soon. 

This package is very much still a work in progress. All the functional aspects are done but using the script will take some editing for your local environment. 

The script should be pointed at the directory where all the .accdb files are stored. The script will then find the accdb files in that directory, and pipe them into the extraction pipeline.
This workflow could very easily be refactored into a parallel process and that is on the todo list.


## install

Clone the repo(and create the directory to store the repo)

```
mkdir -p ~/Documents/ipeds && git clonehttps://github.com/TheOmnipotentPotato/ipeds-tables.git ~/Documents/ipeds
```
install `mdbtools` which allows unix machines to extract data from an access database

On MacOS
```
brew instal mdbtools
```
On Debian (Ubuntu, Linux Mint)
```
apt install mdbtools
```
If you wish to build from source the `mdbtools` repo has good instructions on that 
[m=1tools](https://github.com/mdbtools/mdbtools)\
This package is not yet polished enough to put on CRAN and install normally. 

## usage

After cloning the repo navigate to it in your IDE of choice. You will need to change the `database_path` variable in `extract_data.R` to wherever the ipeds access database files are installed on your machine.
```
database_path <- #where the .accdb files are stored
```

After saving the change run the script with whatever method you prefer. The example for this README will be with the terminal.

```
cd ~/Documents/ipeds && Rscript extract_data.R
```

To use the data in a project load it with the R builtin `load`
```
#for example loading the C2022_A table
load(file="C2022_A.Rda")
```
## future plans

This project is actively being worked on and will become easier to use as time goes on. I plan on working on a Windows fork

### TODO
- [ ] build package through roxygen2
- [ ] automate download process
- [ ] windows compatible fork
- [ ] document functions for `?function` in R console
- [ ] build vignette for package
