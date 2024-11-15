from btree import BTree
from hash_table import HashTable
from product import ProductEntry
import struct

PRODUCT_ENTRY_SIZE = struct.calcsize("q16sf")


def query_btree(btree: BTree, product_id: int):
    adress = btree.search(product_id)
    if adress is not None:
        with open("input/produtos_final_novo.bin", "rb") as f:
            f.seek(adress)
            chunk = f.read(PRODUCT_ENTRY_SIZE)
            return ProductEntry.from_binary(chunk)

    return None
