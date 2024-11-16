import time


class HashTable:
    def __init__(self, size):
        """
        Inicializa a tabela hash com encadeamento direto.
        :param size: Tamanho da tabela.
        """
        self.size = size  # Tamanho da tabela
        self.table = [[] for _ in range(size)]  # Lista de listas para encadeamento

    def _hash(self, key):
        """
        Função hash simples.
        :param key: Chave a ser usada na tabela.
        :return: Índice calculado pela função hash.
        """
        return hash(key) % self.size

    def insert(self, key, address):
        """
        Insere uma chave e endereço na tabela.
        :param key: Chave a ser inserida.
        :param address: Endereço associado à chave.
        """
        index = self._hash(key)
        # Verificar se a chave já existe para evitar duplicatas
        for k, _ in self.table[index]:
            if k == key:
                raise ValueError(f"Chave {key} já existe na tabela.")
        self.table[index].append((key, address))

    def search(self, key):
        """
        Busca uma chave na tabela.
        :param key: Chave a ser buscada.
        :return: Endereço associado à chave ou None se não encontrado.
        """
        index = self._hash(key)
        for k, address in self.table[index]:
            if k == key:
                return address
        return None

    def remove(self, key):
        """
        Remove uma chave da tabela.
        :param key: Chave a ser removida.
        """
        index = self._hash(key)
        for i, (k, _) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False

    def rebuild(self, data):
        """
        Reconstrói o índice com novos dados.
        :param data: Lista de tuplas (key, address).
        """
        self.table = [[] for _ in range(self.size)]  # Reinicializa a tabela
        for key, address in data:
            self.insert(key, address)

    def measure_operation_time(self, operation, *args):
        """
        Mede o tempo de execução de uma operação na tabela hash.
        :param operation: Função a ser medida.
        :param args: Argumentos da função.
        :return: Tempo de execução em segundos e o resultado da operação.
        """
        start_time = time.time()
        result = operation(*args)
        end_time = time.time()
        return end_time - start_time, result

    def get_all(self):
        """
        Retorna todos os itens da tabela.
        :return: Lista de todos os pares (key, address).
        """
        return [(k, v) for bucket in self.table for k, v in bucket]
