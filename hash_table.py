class HashTable:
    def __init__(self, size):
        self.size = size  # Tamanho da tabela
        self.table = [[] for _ in range(size)]  # Lista de listas para encadeamento

    def _hash(self, key):
        """Função hash simples."""
        return hash(key) % self.size

    def insert(self, key, address):
        """Insere uma chave e endereço na tabela."""
        index = self._hash(key)
        self.table[index].append((key, address))

    def search(self, key):
        """Busca uma chave na tabela."""
        index = self._hash(key)
        for k, address in self.table[index]:
            if k == key:
                return address  # Retorna o endereço associado
        return None
