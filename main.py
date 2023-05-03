def get_data_file_content(file_name):
    with open(file_name, "r") as data_file:
        data_file_content = data_file.read()

    return data_file_content


def main():
    print("Starting script for record comparison and validation")

    print(get_data_file_content("./Data/test.csv"))


if __name__ == "__main__":
    main()
