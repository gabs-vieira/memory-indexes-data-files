import struct

from btree import BTree
from hash_table import HashTable
from product import ProductEntry

PRODUCT_ENTRY_SIZE = 45
HASH_TABLE_SIZE = 1000
BTREE_ORDER = 5


def load_products():
    products = []
    product_size = 28  # Tamanho do registro
    with open("input/final_products.bin", "rb") as f:
        while chunk := f.read(product_size):
            if len(chunk) == product_size:
                product = ProductEntry.from_binary(chunk)
                products.append(product)
    return products
