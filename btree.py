class BTreeNode:
    def __init__(self, order):
        self.order = order  # Ordem da árvore (quantidade máxima de chaves é order - 1)
        self.keys = []  # Lista de chaves (product_id)
        self.addresses = (
            []
        )  # Lista de endereços para registros (ou referências no caso da árvore B+)
        self.children = []  # Lista de nós filhos (somente para nós internos)
        self.is_leaf = True  # Indica se o nó é uma folha


class BTree:
    def __init__(self, order):
        self.root = BTreeNode(order)  # Nó raiz
        self.order = order

    def insert(self, key, address):
        """Insere uma chave e seu endereço na árvore."""
        root = self.root
        if len(root.keys) == self.order - 1:  # Nó está cheio
            new_root = BTreeNode(self.order)
            new_root.children.append(self.root)
            new_root.is_leaf = False
            self.split_child(new_root, 0)
            self.root = new_root
        self._insert_non_full(self.root, key, address)

    def _insert_non_full(self, node, key, address):
        """Insere em um nó não cheio."""
        if node.is_leaf:
            # Insere a chave e endereço na posição correta
            i = len(node.keys) - 1
            while i >= 0 and key < node.keys[i]:
                i -= 1
            node.keys.insert(i + 1, key)
            node.addresses.insert(i + 1, address)
        else:
            # Encontra o filho correto para descer
            i = len(node.keys) - 1
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == self.order - 1:  # Filho está cheio
                self.split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], key, address)

    def split_child(self, parent, index):
        """Divide um filho cheio."""
        node = parent.children[index]
        mid = self.order // 2
        new_node = BTreeNode(self.order)
        new_node.is_leaf = node.is_leaf
        parent.keys.insert(index, node.keys[mid])
        parent.children.insert(index + 1, new_node)
        new_node.keys = node.keys[mid + 1 :]
        new_node.addresses = node.addresses[mid + 1 :]
        node.keys = node.keys[:mid]
        node.addresses = node.addresses[:mid]
        if not node.is_leaf:
            new_node.children = node.children[mid + 1 :]
            node.children = node.children[: mid + 1]

    def search(self, key):
        """Busca uma chave na árvore."""
        return self._search(self.root, key)

    def _search(self, node, key):
        i = 0
        print(f"Searching for key: {key} in node with keys: {node.keys}")
        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        # Verifica se a chave foi encontrada
        if i < len(node.keys) and key == node.keys[i]:
            return node.addresses[i]  # Retorna o endereço associado

        # Se o nó for folha e não encontramos a chave, retornamos None
        if node.is_leaf:
            return None

        # Antes de tentar acessar node.children[i], verificamos se i está dentro do intervalo
        if i < len(node.children):  # Verifica se há filhos para descer
            return self._search(node.children[i], key)
        else:
            return None  # Caso não haja filho para descer
