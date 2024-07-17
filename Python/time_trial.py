import logging
from re import search
from time import process_time

import jaydebeapi as jdba
import pandas as pd

logger = logging.getLogger(__name__)
logging.basicConfig(
    format="[%(levelname)s] %(asctime)s: %(message)s",
    filename="time_trial.log",
    encoding="utf-8",
    level=logging.DEBUG,
)
# test speed of base fetchall vs custom fetch_fast with larger array size


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


def get_table_slow(table_name: str, connection: jdba.Connection):
    with connection.cursor() as cursor:
        cursor.execute("SELECT *" + f"FROM {table_name}")
        logging.debug(f"SQL query complete for {table_name}")
        table_data: list[tuple[str]] = cursor.fetchall()
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


def get_table(table_name: str, connection: jdba.Connection):
    with connection.cursor() as cursor:
        cursor.execute("SELECT *" + f"FROM {table_name}")
        logging.debug(f"SQL query complete for {table_name}")
        table_data: list[tuple[str]] = cursor.fetchall()
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


if __name__ == "__main__":
    start_time = process_time()
    slow = get_table_slow("HD2010", cnxn)
    stop_time = process_time()
    slow_time = stop_time - start_time
    start_time = process_time()
    fast = get_table("HD2010", cnxn)
    stop_time = process_time()
    fast_time = stop_time - start_time
    print(slow_time, fast_time)
