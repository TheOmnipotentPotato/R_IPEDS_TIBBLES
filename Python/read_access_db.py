import jaydebeapi as jdba

from csv_writter import dict_csv_write

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
print("Connection made")
csrs: jdba.Cursor = cnxn.cursor()


def get_table(table_name: str, connection: jdba.Connection) -> dict[str | list[str], str | list[tuple[str]]]:
    with connection.cursor() as cursor:
        cursor.execute("SELECT *" + f"FROM {table_name}")
        table_data: list[tuple[str]] = cursor.fetchall()
        table_data: list[list[str]] = 
        cursor.execute(
            "SELECT COLUMN_NAME "
            + "FROM INFORMATION_SCHEMA.COLUMNS "
            + f"WHERE table_name=N'{table_name}'"
        )
        column_names: list[tuple[str]] = cursor.fetchall()
        column_names: list[str] = [row[0] for row in column_names]


    return {'head' : column_names, 'data': table_data}


def get_table_names(connection: jdba.Connection) -> list[str]:
    with connection.cursor() as cursor:
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
        table_names = get_table_names(conn)
        for name in table_names:
            table: dict[str | list[str], str | list[tuple[str]]] = get_table(name, conn)
            dict_csv_write(table['head'], table['data'], name)






if __name__ == "__main__":
    out = database_to_csv(db_path)
    print(out)
