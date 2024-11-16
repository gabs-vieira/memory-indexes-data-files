import struct
import os
import tempfile

# Definições do formato dos registros
FORMAT = "q16sf"  # long, char[16], float
RECORD_SIZE = struct.calcsize(FORMAT)


def read_product_chunk(file, chunk_size=10000):

    products = []
    for _ in range(chunk_size):
        chunk = file.read(RECORD_SIZE)
        if len(chunk) != RECORD_SIZE:  # Fim do arquivo
            break
        product_id, brand, price = struct.unpack(FORMAT, chunk)

        # Ignorar registros inválidos
        if product_id == 0:
            continue

        brand = brand.decode("utf-8", errors="replace").strip("\x00")
        products.append({"product_id": product_id, "brand": brand, "price": price})

    return products


def process_products(input_file, output_file):
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Arquivo de entrada não encontrado: {input_file}")

    unique_products = {}

    # Arquivo temporário para escrita
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file_path = temp_file.name

        with open(input_file, "rb") as f:
            while products := read_product_chunk(f):
                for product in products:
                    product_id = product["product_id"]

                    if product_id not in unique_products:
                        unique_products[product_id] = product

        # Ordena os produtos e grava no arquivo temporário
        with open(temp_file_path, "wb") as temp_file:
            for product_id in sorted(unique_products.keys()):
                product = unique_products[product_id]
                brand = product["brand"].ljust(16, "\x00").encode("utf-8")
                data = struct.pack(FORMAT, product_id, brand, product["price"] or 0.0)
                temp_file.write(data)

        # Substitui o arquivo de saída pelo temporário
        os.replace(temp_file_path, output_file)

    print(
        f"Arquivo processado com sucesso (removido duplicatas e ordenado): {output_file}"
    )


def main():
    input_file = "input/products.bin"
    output_file = "input/produtos_final_novo.bin"

    try:
        process_products(input_file, output_file)
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")


if __name__ == "__main__":
    main()
