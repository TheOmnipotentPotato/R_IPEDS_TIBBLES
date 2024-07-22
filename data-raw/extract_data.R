library(Hmisc)

setwd("/Users/julianickodemus/Coding/R/ipedsData")

databases <- list.files(pattern = ".*\\.accdb")

exract_database <- function(path) {
    year_str <- gsub(pattern = "^[A-Z]*", "-", path) |>
        gsub(pattern = "\\.accdb", replacement = "-") |>
        substr(4, 5)
    db_out <- Hmisc::mdb.get(path, stringsAsFactors = FALSE)
    list(year = year_str, data = db_out)
}


exract_database(databases[1])
