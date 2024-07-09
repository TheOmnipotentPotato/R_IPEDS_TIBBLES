library(tidyverse)
library(odbc)

con1 <- dbConnect(odbc::odbc(), driver="ODBC Driver 17 for SQL Server")
