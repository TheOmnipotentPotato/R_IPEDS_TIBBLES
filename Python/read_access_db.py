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
cnxn: jbda.Connection = jdba.connect(
    "net.ucanaccess.jdbc.UcanaccessDriver",
    f"jdbc:ucanaccess://{db_path};newDatabaseVersion=V2010",
    ["", ""],
    classpath,
)
print("Connection made")
csrs: jdba.Cursor = cnxn.cursor()


def get_table(table_name: str, connection: jdba.Connection):
    table_data = [
        ("NULL",),
    ]
    table_names = [
        ("NULL",),
    ]
    with connection.cursor() as cursor:
        cursor.execute("SELECT *" + f"FROM {table_name}")
        table_data: list[tuple[str]] = cursor.fetchall()

        cursor.execute(
            "SELECT COLUMN_NAME "
            + "FROM INFORMATION_SCHEMA.COLUMNS "
            + f"WHERE table_name=N'{table_name}'"
        )
        table_names: list[tuple[str]] = cursor.fetchall()

        header_row: any = []
        for row in table_names:
            header_row.append(row[0])
        header_row = tuple(header_row)

        table_data.insert(0, header_row)

    return table_data


def database_to_csv(path: str) -> None:

    cnxn: jbda.Connection = jdba.connect(
        "net.ucanaccess.jdbc.UcanaccessDriver",
        f"jdbc:ucanaccess://{db_path};newDatabaseVersion=V2010",
        ["", ""],
        classpath,
    )
