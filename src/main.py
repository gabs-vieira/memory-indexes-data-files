import csv
import time
from object_management import *
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
        if isinstance(row[3], (int, float)):
            tempo = f"{row[3]:<15.6f}"
        else:
            tempo = f"{row[3]:<15}"
        print(f"{row[0]:<20} {row[1]:<15} {row[2]:<15} {tempo}")


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

            if not (btree and hash_table):
                print("Os índices precisam ser criados antes de remover produtos.")
                continue

            product_id = int(input("Digite o ID do produto para consultar: "))

            # File Query
            result_file, file_time = measure_execution_time(query_in_file, product_id)
            if result_file is None:
                print("Produto não encontrado no arquivo.")
                results.append(["Query-error", "File", product_id, "Erro"])
            else:
                results.append(["Query", "File", product_id, file_time])
                print(f"Query time in File: {file_time:.6f} seconds.")

            # BTree Query
            if btree is not None:
                result_btree, btree_time = measure_execution_time(
                    query_btree, btree, product_id
                )
                if result_btree is None:
                    print("Produto não encontrado na BTree.")
                    results.append(["Query-error", "BTree", product_id, "Erro"])
                else:
                    results.append(["Query", "BTree", product_id, btree_time])
                    print(f"Query time in BTree: {btree_time:.6f} seconds.")

            # Hash Table Query
            if hash_table is not None:
                result_hash, hash_time = measure_execution_time(
                    query_hash_table, hash_table, product_id
                )
                if result_hash is None:
                    print("Produto não encontrado na HashTable.")
                    results.append(["Query-error", "HashTable", product_id, "Erro"])
                else:
                    results.append(["Query", "HashTable", product_id, hash_time])
                    print(f"Query time in HashTable: {hash_time:.6f} seconds.")

        elif choice == "3":

            # if not (btree and hash_table):
            #     print("Os índices precisam ser criados antes de remover produtos.")
            #     continue

            new_product = ProductEntry(
                product_id=int(input("Digite o ID do novo produto: ")),
                brand=input("Digite a brand do produto: "),
                price=float(input("Digite o preço do produto: ")),
            )
            times = add_product(btree, hash_table, new_product, INPUT_PATH)

            results.append(
                ["Add Product", "File", new_product.product_id, times["file"]]
            )
            results.append(
                ["Add Product", "BTree", new_product.product_id, times["btree"]]
            )
            results.append(
                [
                    "Add Product",
                    "HashTable",
                    new_product.product_id,
                    times["hash_table"],
                ]
            )

            print(
                f"Tempo para adicionar produto (ID {new_product.product_id}):\n"
                f"Arquivo: {times['file']:.6f}s\n"
                f"BTree: {times['btree']:.6f}s\n"
                f"HashTable: {times['hash_table']:.6f}s"
            )

        elif choice == "4":

            # if not (btree and hash_table):
            #     print("Os índices precisam ser criados antes de remover produtos.")
            #     continue

            product_id = int(input("Digite o ID do produto a remover: "))

            # Medindo o tempo para cada operação
            times, success = remove_product(btree, hash_table, product_id)
            if not success:
                results.append(["Remove-error", "File", product_id, "Erro"])
                continue

            # Adicionando os tempos aos resultados
            results.append(["Remove Product", "File", product_id, times["file"]])
            results.append(["Remove Product", "BTree", product_id, times["btree"]])
            results.append(
                ["Remove Product", "HashTable", product_id, times["hash_table"]]
            )

            print(
                f"Tempo para remover produto (ID {product_id}):\n"
                f"Arquivo: {times['file']:.6f}s\n"
                f"BTree: {times['btree']:.6f}s\n"
                f"HashTable: {times['hash_table']:.6f}s"
            )

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
