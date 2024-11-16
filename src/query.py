from btree import BTree
from hash_table import HashTable
from product import ProductEntry

from constants import PRODUCT_ENTRY_SIZE, INPUT_PATH


# Queries in File


# Queries in Memory
def query_btree(btree: BTree, product_id: int):
    adress = btree.search(product_id)
    if adress is not None:
        with open(INPUT_PATH, "rb") as f:
            f.seek(adress)
            chunk = f.read(PRODUCT_ENTRY_SIZE)
            return ProductEntry.from_binary(chunk)

    return None


def query_hash_table(hash_table: HashTable, product_id: int):
    address = hash_table.search(product_id)
    with open(INPUT_PATH, "rb") as f:
        f.seek(address)
        chunk = f.read(PRODUCT_ENTRY_SIZE)
        return ProductEntry.from_binary(chunk)

    return None
