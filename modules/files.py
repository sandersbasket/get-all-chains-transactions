def save_address_to_file(address: str, filename: str) -> None:
    with open(filename, 'a+') as file:
        file.write(address + '\n')
    print(f"{address} saved to {filename} successfully.")