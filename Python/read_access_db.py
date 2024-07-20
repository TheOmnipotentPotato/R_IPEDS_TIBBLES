import logging
from re import search
from time import process_time

import jaydebeapi as jdba
import pandas as pd
from yaspin import yaspin
from yaspin.spinners import Spinners

from csv_writter import dict_csv_write

logger = logging.getlogger(__name__)
logging.basicconfig(
    format="[%(levelname)s] %(asctime)s: %(message)s",
    filename="db_write.log",
    encoding="utf-8",
    level=logging.debug,
)

db_path = "/Users/julianickodemus/Coding/R/ipedsData/IPEDS201011.accdb"

# UCanAccess jar files
ucanaccess_jars = [
    "/Users/julianickodemus/Coding/JDBC/UCanAccess/UCanAccess501/ucanaccess-5.0.1.jar",
    "/Users/julianickodemus/Coding/JDBC/UCanAccess/UCanAccess501/lib/commons-lang3-3.8.1.jar",
    "/Users/julianickodemus/Coding/JDBC/UCanAccess/UCanAccess501/lib/commons-logging-1.2.jar",
    "/Users/julianickodemus/Coding/JDBC/UCanAccess/UCanAccess501/lib/hsqldb-2.5.0.jar",
    "/Users/julianickodemus/Coding/JDBC/UCanAccess/UCanAccess501/lib/jackcess-3.0.1.jar",
]
classpath = ":".join(ucanaccess_jars)
cnxn: jdba.Connection = jdba.connect(
    "net.ucanaccess.jdbc.UcanaccessDriver",
    f"jdbc:ucanaccess://{db_path};newDatabaseVersion=V2010",
    ["", ""],
    classpath,
)
logging.info("Connected to database")
csrs: jdba.Cursor = cnxn.cursor()


def fetch_fast(cursor: jdba.Cursor) -> list[tuple[str]]:
    cursor.arraysize = 50
    rows = []
    while True:
        row = cursor.fetchmany()
        if row is None:
            break
        else:
            rows.append(row)
    return rows


def get_table(table_name: str, connection: jdba.Connection):
    with connection.cursor() as cursor:
        cursor.execute("SELECT *" + f"FROM {table_name}")
        logging.debug(f"SQL query complete for {table_name}")
        table_data: list[tuple[str]] = fetch_fast(cursor)
        logging.debug(f"Data extracted from {table_name} table")
        cursor.execute(
            "SELECT COLUMN_NAME "
            + "FROM INFORMATION_SCHEMA.COLUMNS "
            + f"WHERE table_name=N'{table_name}'"
        )
        column_names: list[tuple[str]] = cursor.fetchall()
        column_names: list[str] = [row[0] for row in column_names]
        logging.debug(f"Header created for {table_name}")

    return {"head": column_names, "data": table_data}


def find_tables_table(table_names: list[str]) -> str:
    regex = lambda name: search("TABLES", name)
    name = [regex(table).string for table in table_names if not regex(table)]


def get_table_names(connection: jdba.Connection) -> list[str]:
    with connection.cursor() as cursor:
        # get the tables in database
        cursor.execute(
            "SELECT table_name "
            + "FROM INFORMATION_SCHEMA.TABLES "
            + "WHERE table_type = 'BASE TABLE'"
        )
        table_names: list[tuple[str]] = cursor.fetchall()
        table_names: list[str] = [row[0] for row in table_names]

    return table_names


def database_to_csv(path: str) -> None:

    with jdba.connect(
        "net.ucanaccess.jdbc.UcanaccessDriver",
        f"jdbc:ucanaccess://{path};newDatabaseVersion=V2010",
        ["", ""],
        classpath,
    ) as conn:
        table_names = get_table_names(conn)[4:]
        print(table_names)
        for name in table_names:
            start_time = process_time()
            logging.debug(f"Processing {name} table")
            table: dict[str | list[str], str | list[tuple[str]]] = get_table(name, conn)
            dict_csv_write(table["head"], table["data"], name)
            stop_time = process_time()
            p_time = stop_time - start_time
            logging.debug(
                f"Processed {name} table in {p_time//60} mins and {p_time % 60} seconds"
            )


if __name__ == "__main__":
    # out = database_to_csv(db_path)
    # print(out)
    table = get_table("C2010_A", cnxn)
    df: pd.DataFrame = pd.DataFrame(table["data"], columns=table["head"])
    df.to_csv("test3.csv", encoding="utf-8", index=False, header=True)
