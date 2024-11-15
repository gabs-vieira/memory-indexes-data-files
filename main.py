from file_operations import load_products


def main():
    # products = load_products()
    btree, hash_table = load_products()

    breakpoint()
    product_address = btree.search(16700260)


if __name__ == "__main__":
    main()
