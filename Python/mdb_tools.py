import logging
from subprocess import check_output, run

logger = logging.getLogger(__name__)
logging.basicConfig(
    format="[%(levelname)s] %(asctime)s: %(message)s",
    filename="mbd-test.log",
    encoding="utf-8",
    level=logging.DEBUG,
)


db_path = "/Users/julianickodemus/Coding/R/ipedsData/IPEDS201011.accdb"


def table_to_csv(path: str, table_name: str) -> None:
    logging.debug(f"Accessing {table_name} via mdb-tools")
    run(f"echo '$(mdb-export {path} {table_name})' > {table_name}.csv", shell=True)
    logging.debug(f"{table_name} written to csv")
    return None


def table_to_csv_2(path: str, table_name: str) -> str:
    logging.debug(f"Accessing {table_name} via mdb-tools")
    data = check_output(f"mdb-export {path} {table_name}", shell=True).decode("utf-8")
    logging.debug(f"{table_name} written to csv")
    return data


if __name__ == "__main__":
    out = table_to_csv_2(db_path, "C2010_A")
    print(out)
