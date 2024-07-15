from csv import DictWriter

test_data = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [2, 3, 4, 5, 6, 7, 8, 9, 1],
    [3, 4, 5, 6, 7, 8, 9, 1, 2],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [5, 6, 7, 8, 9, 1, 2, 3, 4],
    [6, 7, 8, 9, 1, 2, 3, 4, 5],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [8, 9, 1, 2, 3, 4, 5, 6, 7],
    [9, 1, 2, 3, 4, 5, 6, 7, 8],
]

test_header = ["Var1", "Var2", "Var3", "Var4", "Var5", "Var6", "Var7", "Var8", "Var9"]


def two_list_to_dict(array1: list[str], array2: list[str]) -> dict[str, str]:
    zipped_lists = zip(array1, array2)
    return dict(zipped_lists)


def dict_csv_write(
    header_row: list[str], data: list[list[any]], table_name: str
) -> None:
    with open(f"{table_name}.csv", "a", newline="") as csv:
        writer = DictWriter(csv, fieldnames=header_row)
        writer.writeheader()

        for row in data:
            row_dict = two_list_to_dict(header_row, row)
            writer.writerow(row_dict)


if __name__ == "__main__":
    dict_csv_write(test_header, test_data, "test")
