import struct

from btree import BTree
from hash_table import HashTable
from product import ProductEntry

PRODUCT_ENTRY_SIZE = 45
HASH_TABLE_SIZE = 1000
BTREE_ORDER = 5
PRODUCT_ENTRY_SIZE = struct.calcsize("q16sf")


def load_products():
    products = []
    btree = BTree(BTREE_ORDER)
    hash_table = HashTable(HASH_TABLE_SIZE)

    with open("input/produtos_final_novo.bin", "rb") as f:
        address = 0
        while chunk := f.read(PRODUCT_ENTRY_SIZE):
            if len(chunk) == PRODUCT_ENTRY_SIZE:
                product = ProductEntry.from_binary(chunk)

                btree.insert(product.product_id, address)
                hash_table.insert(product.product_id, address)
    return btree, hash_table
