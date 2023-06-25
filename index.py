import threading
from typing import List
from modules import addresses as Address
from settings import settings 


addresses: List[str] = open(settings.config["file"], "r").read().splitlines()

def process_addresses(addresses: List[str]) -> None:
    for address in addresses:
        Address.get_transactions(address)

def split_array(array: List[str], num_parts: int) -> List[List[str]]:
    chunk_size = len(array) // num_parts
    remainder = len(array) % num_parts

    chunks = []
    start = 0
    for i in range(num_parts):
        end = start + chunk_size + (1 if i < remainder else 0)
        chunks.append(array[start:end])
        start = end

    return chunks

num_parts = settings.config['threads']
chunks = split_array(addresses, num_parts)

threads = []

for chunk in chunks:
    thread = threading.Thread(target=process_addresses, args=(chunk,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
