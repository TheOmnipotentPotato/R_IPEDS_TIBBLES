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
[mdbtools](https://github.com/mdbtools/mdbtools)\
This package is not yet polished enough to put on CRAN and install normally. 

## usage

After cloning the repo navigate to it in your IDE of choice. You will need to change the `database_path` variable to wherever the ipeds access database files are installed on your machine.
```
database_path <- #where the .accdb files are stored
```
