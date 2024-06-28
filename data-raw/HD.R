library(usethis)
library(roxygen2)
library(tidyverse)
library(ipeds)
options('ipeds.download.dir' = '/Users/julianickodemus/Coding/R/ipedsData')

HD <- tibble(ipeds_survey('HD', year=2021))
use_data(HD, overwrite = TRUE)
