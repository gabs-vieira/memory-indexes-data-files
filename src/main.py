import csv
import time
from object_management import (
    load_products,
    load_btree,
    load_hash,
)
from query import *


def measure_execution_time(func, *args):
    start_time = time.time()
    index = func(*args)
    end_time = time.time()
    return index, end_time - start_time


def display_results_table(results):
    """Exibe uma tabela comparativa no terminal."""
    print("\nResultados Comparativos:")
    headers = ["Funcionalidade", "Método", "ID Produto", "Tempo (s)"]
    print(f"{headers[0]:<20} {headers[1]:<15} {headers[2]:<15} {headers[3]:<15}")
    for row in results:
        print(f"{row[0]:<20} {row[1]:<15} {row[2]:<15} {row[3]:<15.6f}")


def save_to_csv(filename, headers, data):
    """Salva os resultados em um arquivo CSV."""
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)


def main():

    print("\nLoading products...")
    products = load_products()
    print("Done.")

    # print("\nCreating indexes in memory...")
    # btree, index_btree_time = measure_index_creation(load_btree, products)
    # hash_table, index_hash_time = measure_index_creation(load_hash, products)
    # print("Done.")

    # product_ids = [26022534, 17300016, 1005115, 5100503, 4804194]

    btree, hash_table = None, None
    results = []

    while True:
        print("\nEscolha uma ação:")
        print("1. Criar índice em memória (HashTable e BTree)")
        print("2. Consultar produto (Arquivo, HashTable, BTree)")
        print("3. Adicionar produto (HashTable, BTree)")
        print("4. Remover produto (HashTable, BTree)")
        print("5. Gerar tabela de resultados e sair")
        choice = input("Digite o número da ação: ").strip()

        if choice == "1":
            print("\nCreating indexes in memory...")
            btree, btree_time = measure_execution_time(load_btree, products)
            hash_table, hash_time = measure_execution_time(load_hash, products)
            results.append(["Create Index", "BTree", "-", btree_time])
            results.append(["Create Index", "HashTable", "-", hash_time])
            print(f"BTree created in {btree_time:.6f} seconds.")
            print(f"HashTable created in  {hash_time:.6f} seconds.")

        elif choice == "2":
            product_id = int(input("Digite o ID do produto para consultar: "))
            _, file_time = measure_execution_time(query_in_file, product_id)
            _, btree_time = (
                measure_execution_time(query_btree, btree, product_id)
                if btree
                else (None, None)
            )
            _, hash_time = (
                measure_execution_time(query_hash_table, hash_table, product_id)
                if hash_table
                else (None, None)
            )

            results.append(["Query", "File", product_id, file_time])
            if btree_time is not None:
                results.append(["Query", "BTree", product_id, btree_time])
            if hash_time is not None:
                results.append(["Query", "HashTable", product_id, hash_time])

            print(f"Query time in File: {file_time:.6f} seconds.")
            if btree_time is not None:
                print(f"Query time in BTree: {btree_time:.6f} seconds.")
            if hash_time is not None:
                print(f"Query time in HashTable: {hash_time:.6f} seconds.")

        elif choice == "3":
            # TODO: Insert products in btree and hash table
            print("TODO: Insert products in btree and hash table")
            # new_product = {
            #     "id": int(input("Digite o ID do novo produto: ")),
            #     "name": "Novo Produto",
            #     "price": 10.0,
            # }
            # _, btree_time = (
            #     measure_execution_time(insert_in_btree, btree, new_product)
            #     if btree
            #     else (None, None)
            # )
            # _, hash_time = (
            #     measure_execution_time(insert_in_hash, hash_table, new_product)
            #     if hash_table
            #     else (None, None)
            # )

            # if btree_time is not None:
            #     results.append(
            #         ["Adicionar Produto", "BTree", new_product["id"], btree_time]
            #     )
            #     print(f"Produto adicionado à BTree em {btree_time:.6f} seconds.")
            # if hash_time is not None:
            #     results.append(
            #         ["Adicionar Produto", "HashTable", new_product["id"], hash_time]
            #     )
            #     print(f"Produto adicionado à HashTable em {hash_time:.6f} seconds.")

        elif choice == "4":
            # TODO: Remove products in btree and hash table
            print("TODO: Remove products in btree and hash table")
            # product_id = int(input("Digite o ID do produto a remover: "))
            # _, btree_time = (
            #     measure_execution_time(remove_from_btree, btree, product_id)
            #     if btree
            #     else (None, None)
            # )
            # _, hash_time = (
            #     measure_execution_time(remove_from_hash, hash_table, product_id)
            #     if hash_table
            #     else (None, None)
            # )

            # if btree_time is not None:
            #     results.append(["Remover Produto", "BTree", product_id, btree_time])
            #     print(f"Produto removido da BTree em {btree_time:.6f} seconds.")
            # if hash_time is not None:
            #     results.append(["Remover Produto", "HashTable", product_id, hash_time])
            #     print(f"Produto removido da HashTable em {hash_time:.6f} seconds.")

        elif choice == "5":
            display_results_table(results)
            save_to_csv(
                "../output/results.csv",
                ["Funcionalidade", "Método", "ID Produto", "Tempo (s)"],
                results,
            )
            print("\nResultados salvos em 'results.csv'.")
            print("Encerrando programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
