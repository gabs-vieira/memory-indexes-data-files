import csv
import struct


# Definição do formato binário
FORMAT = "q16sf"  # long long (q), string de 16 bytes (16s), float (f)
RECORD_SIZE = struct.calcsize(FORMAT)


def process_product_data(input_csv, output_bin):
    with open(input_csv, "r", encoding="utf-8") as csv_file, open(
        output_bin, "wb"
    ) as bin_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            try:
                # Extração e validação dos campos
                product_id = int(row["product_id"])
                brand = (
                    row["brand"] or "Unknown"
                )  # Substituir valores nulos por "Unknown"
                price = float(row["price"])

                # Validar os dados
                if product_id > 0 and price > 0.0 and len(brand) > 0:
                    # Garantir que a marca tenha no máximo 16 caracteres
                    brand = brand[:16].ljust(16, "\x00")
                    # Empacotar os dados e escrever no arquivo binário
                    bin_file.write(
                        struct.pack(FORMAT, product_id, brand.encode("utf-8"), price)
                    )
            except (ValueError, KeyError) as e:
                # Ignorar registros inválidos
                print(f"Registro ignorado: {row}, erro: {e}")


if __name__ == "__main__":
    input_csv_path = "input/dataset.csv"
    output_bin_path = "input/products.bin"

    process_product_data(input_csv_path, output_bin_path)
    print(f"Produtos válidos processados e salvos em {output_bin_path}")
