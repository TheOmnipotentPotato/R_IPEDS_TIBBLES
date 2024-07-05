library(usethis)
library(roxygen2)
library(tidyverse)
library(ipeds)
options("ipeds.download.dir" = "/Users/julianickodemus/Coding/R/ipedsData")



available_ipeds <- ipeds::available_ipeds()




get_valid_years <- function() {
    valid_years <- tibble(available_ipeds) |>
        filter(downloaded == TRUE) |>
        summarise(year)
    valid_years
}

get_missing_years <- function() {
    missing_years <- tibble(available_ipeds) |>
        filter(downloaded == FALSE & (provisional == TRUE | final == TRUE)) |>
        summarise(year)
    missing_years
}



download_missing_years <- function(missing_years) {
    missing_years |> map(\(missing_year) ipeds::download_ipeds(missing_year, force = TRUE))
}

generate_tibble <- function(table_name, table_year) {
    tibble(ipeds::ipeds_survey(table_name, year = table_year))
}



pull_data_year <- function(data_year) {
    print(data_year)
    table_names <- names(ipeds::load_ipeds(data_year))
    table_names |> map(\(table_name) generate_tibble(table_name, data_year))
}

pull_all_data <- function(year_list) {
    year_list |> map(pull_data_year)
}


# get_missing_years() |> download_missing_years()
valid_years <- get_valid_years()

pull_all_data(valid_years)
