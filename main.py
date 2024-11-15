import time
from file_operations import load_products
from query import query_btree


def measure_index_creation(load_function):
    start_time = time.time()
    index = load_function()
    end_time = time.time()
    return index, end_time - start_time


def main():
    # products = load_products()
    btree, hash_table = load_products()

    a = query_btree(btree, 16700260)
    b = query_btree(btree, 4100297)
    print(b.product_id)
    print(b.brand)
    print(b.price)
    breakpoint()


if __name__ == "__main__":
    main()
