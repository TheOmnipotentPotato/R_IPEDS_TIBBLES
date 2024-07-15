import jaydebeapi as jdba

from csv import

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
cnxn = jdba.connect(
    "net.ucanaccess.jdbc.UcanaccessDriver",
    f"jdbc:ucanaccess://{db_path};newDatabaseVersion=V2010",
    ["", ""],
    classpath,
)
print("Execution Step 1 complete")
csrs = cnxn.cursor()

# Select * from HD2010
csrs.execute(
    """
    SELECT COLUMN_NAME 
    FROM INFORMATION_SCHEMA.COLUMNS 
    WHERE table_name=N'HD2010'
    """
)
HD2010 = csrs.fetchall()
table_names = HD2010.pop()[0]
for row in HD2010:
    table_names = f"{table_names},{row[0]}"
print(table_names)


def get_table(table_name: str, connection: jdba.Connection):
    table_data = [
        ("NULL",),
    ]
    table_names = [
        ("NULL",),
    ]
    with connection.cursor() as cursor:
        cursor.execute("SELECT *" + f"FROM {table_name}")
        table_data = cursor.fetchall()

        cursor.execute(
            "SELECT COLUMN_NAME "
            + "FROM INFORMATION_SCHEMA.COLUMNS "
            + f"WHERE table_name=N'{table_name}'"
        )
        table_names = cursor.fetchall()
        header_row = []
        for row in table_names:
            header_row.append(row[0])
        header_row = tuple(header_row)

        table_data.insert(0, header_row)

    return table_data


def array_to_csv(table_name: str, array):
    with open(f"{table_name}.csv", a) as file:






if __name__ == "__main__":
    table = get_table("HD2010", cnxn)
    print(table)
