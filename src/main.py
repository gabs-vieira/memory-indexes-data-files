import time
from object_management import (
    load_products,
    load_btree,
    load_hash,
)
from query import *


def measure_index_creation(load_function, *args):
    """Mede o tempo de criação do índice."""
    start_time = time.time()
    index = load_function(*args)
    end_time = time.time()
    return index, end_time - start_time


def measure_query_time(query_function, *args):
    """Mede o tempo de execução de uma consulta."""
    start_time = time.time()
    result = query_function(*args)
    end_time = time.time()
    return result, end_time - start_time


def main():

    print("\nLoading products...")
    products = load_products()
    print("Done.")

    print("\nCreating indexes in memory...")
    btree, index_btree_time = measure_index_creation(load_btree, products)
    hash_table, index_hash_time = measure_index_creation(load_hash, products)
    print("Done.")


if __name__ == "__main__":
    main()
