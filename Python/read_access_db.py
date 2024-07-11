import jaydebeapi as jdba

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
for row in HD2010:
    print(row)

print("end of HD2010")

csrs.execute(
    """
    SELECT COLUMN_NAME
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE table_name=N'FLAGS2010'
    """
)

FLAGS = csrs.fetchall()
for row in FLAGS:
    print(row)
