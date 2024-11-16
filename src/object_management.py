import time

from btree import BTree
from hash_table import HashTable
from product import ProductEntry
from constants import *


def load_products():
    products = []

    with open(INPUT_PATH, "rb") as f:
        address = 0
        while chunk := f.read(PRODUCT_ENTRY_SIZE):
            if len(chunk) == PRODUCT_ENTRY_SIZE:
                product = ProductEntry.from_binary(chunk)
                products.append(product)
                address += PRODUCT_ENTRY_SIZE  # Avança para o próximo registro

    return products


def load_btree(products: list[ProductEntry]):
    btree = BTree(BTREE_ORDER)

    address = 0
    for product in products:
        btree.insert(product.product_id, address)
        address += PRODUCT_ENTRY_SIZE

    return btree


def load_hash(products: list[ProductEntry]):
    hash_table = HashTable(HASH_TABLE_SIZE)

    address = 0
    for product in products:
        hash_table.insert(product.product_id, address)
        address += PRODUCT_ENTRY_SIZE

    return hash_table
