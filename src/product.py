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

    def to_binary(self):
        """
        Serializa o objeto ProductEntry para uma string binária fixa.
        """
        brand_encoded = self.brand.encode("utf-8")[:16]  # Limita a 16 bytes
        brand_padded = brand_encoded + b"\x00" * (
            16 - len(brand_encoded)
        )  # Preenche com '\x00'
        return struct.pack("q16sf", self.product_id, brand_padded, self.price)

    def __repr__(self):
        return (
            f"ProductEntry(product_id={self.product_id}, "
            f"brand='{self.brand}', price={self.price})"
        )
