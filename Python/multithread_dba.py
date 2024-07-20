import os
import time
from multiprocessing import Pool, freeze_support
from multiprocessing.connection import Connection

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


def run():

    cnxn: jdba.Connection = jdba.connect(
        "net.ucanaccess.jdbc.UcanaccessDriver",
        f"jdbc:ucanaccess://{db_path};newDatabaseVersion=V2010",
        ["", ""],
        classpath,
    )
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM DRFV2010")
    records = cursor.fetchall()
    return records


if __name__ == "__main__":

    freeze_support()
    print("Enter the number of times to run the above query")
    n = int(input())
    results = []

    with Pool(processes=os.cpu_count() - 1) as pool:

        for _ in range(n):
            res = pool.apply_async(run)
            results.append(res)
            res = [result.get() for result in results]

    print(res)
    pool.close()
    pool.join()
