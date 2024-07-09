library(tidyverse)
library(usethis)

tab <- tibble(x = 1:5, y = x^2)

usethis::use_data(tab, name = "TABLE_LOL")
