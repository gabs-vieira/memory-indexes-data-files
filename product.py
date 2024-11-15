import struct


class ProductEntry:
    def __init__(self, product_id, brand, price):
        self.product_id = product_id
        self.brand = brand.strip()  # Remove espaços extras ou '\x00'
        self.price = price

    @staticmethod
    def from_binary(data):
        # Formato para leitura: 8 bytes (long), 16 bytes (string), 4 bytes (float)
        unpacked_data = struct.unpack("q16sf", data)
        return ProductEntry(
            product_id=unpacked_data[0],
            brand=unpacked_data[1].decode("utf-8", errors="replace").strip(),
            price=unpacked_data[2],
        )

    def __repr__(self):
        return f"ProductEntry(product_id={self.product_id}, brand='{self.brand}', price={self.price})"
