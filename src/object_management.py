import time

import os
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


def add_product(btree: BTree, hash_table: HashTable, product, file_path):
    times = {}

    file_time = time.time()
    with open(file_path, "ab") as f:
        address = f.tell()
        f.write(product.to_binary())
    times["file"] = time.time() - file_time

    # Medir tempo de inserção na BTree
    btree_time = time.time()
    btree.insert(product.product_id, address)
    times["btree"] = time.time() - btree_time

    # Medir tempo de inserção na HashTable
    hash_time = time.time()
    hash_table.insert(product.product_id, address)
    times["hash_table"] = time.time() - hash_time

    print(f"Product {product.product_id} added successfully.")
    return times


def remove_product(btree, hash_table, product_id):
    times = {}

    # Medir tempo de remoção no arquivo
    start_time = time.time()
    success = remove_from_file(product_id)
    times["file"] = time.time() - start_time

    if not success:
        print(f"Product {product_id} not found in file.")
        return times, False

    start_time = time.time()
    btree.remove(product_id)
    times["btree"] = time.time() - start_time

    start_time = time.time()
    hash_table.remove(product_id)
    times["hash_table"] = time.time() - start_time

    print(f"Product {product_id} removed successfully.")
    return times, True


def remove_from_file(product_id):
    temp_file_path = INPUT_PATH + ".tmp"

    try:
        with open(INPUT_PATH, "rb") as original_file, open(
            temp_file_path, "wb"
        ) as temp_file:
            found = False
            while True:
                data = original_file.read(PRODUCT_ENTRY_SIZE)
                if not data:
                    break
                product = ProductEntry.from_binary(data)
                if product.product_id == product_id:
                    found = True  # Skip writing this record
                    continue
                temp_file.write(data)

        if not found:
            print(f"Product {product_id} not found in file.")
            os.remove(temp_file_path)  # Clean up the temporary file
            return False

        # Replace original file with the updated file
        os.replace(temp_file_path, INPUT_PATH)
        print(f"Product {product_id} removed successfully.")
        return True

    except Exception as e:
        print(f"Error while removing product from file: {e}")
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)  # Clean up the temporary file
        return False
