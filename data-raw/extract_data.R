library(Hmisc)
library(purrr)
library(tidyverse)
library(logger)
setwd("/Users/julianickodemus/Coding/R/ipedsData")

log_path <- "/Users/julianickodemus/Coding/R/ipedsData/ipedsTablesRPKG/ipedstables/data-raw/db_log.log"
databases <- list.files(pattern = ".*\\.accdb")
log_appender(appender_file(log_path))






extract_database <- function(path) {
    year_str <- gsub(pattern = "^[A-Z]*", "-", path) |>
        gsub(pattern = "\\.accdb", replacement = "-") |>
        substr(4, 5)
    db_out <- Hmisc::mdb.get(path, stringsAsFactors = FALSE)
    log_info("Extracted {path}")
    list(year = year_str, data = db_out)
}

get_table <- function(table_name, database) {
    tb <- database[[table_name]] |> tibble()
    list(data = tb, name = table_name)
}



get_table_names <- function(database, year) {
    database[[paste0("Tables", year)]][["TableName"]]
}


write_table_to_Rda <- function(table, name) {
    assign(paste0(name), table)
    save(list = name, file = paste0(name, ".Rda"))
    log_info("Created Rda for {name}")
}

database_to_Rda <- function(database) {
    names <- get_table_names(database$data, database$year)
    tables <- names |> purrr::map(\(name) get_table(name, database$data))
    setwd("/Users/julianickodemus/Coding/R/ipedsData/ipedsTablesRPKG/ipedstables/data/")
    tables |> purrr::map(\(table) write_table_to_Rda(table$data, table$name))
}

# databases |> purrr::map(\(database) print(database))
databases |>
    purrr::map(\(database) extract_database(database)) |>
    purrr::map(\(database) database_to_Rda(database))
