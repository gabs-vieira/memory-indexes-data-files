import struct


class ProductEntry:
    def __init__(self, product_id, brand, price):
        self.product_id = product_id
        self.brand = brand.strip()  # Remove espaços ou '\x00'
        self.price = price

    @staticmethod
    def from_binary(data):
        # Formato: long, string[16], float
        unpacked_data = struct.unpack("q16sf", data)
        return ProductEntry(
            product_id=unpacked_data[0],
            brand=unpacked_data[1].decode("utf-8", errors="replace").strip(),
            price=unpacked_data[2],
        )

    def __repr__(self):
        return (
            f"ProductEntry(product_id={self.product_id}, "
            f"brand='{self.brand}', price={self.price})"
        )
