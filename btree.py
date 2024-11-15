class BTreeNode:
    def __init__(self, is_leaf=False):
        self.is_leaf = is_leaf
        self.keys = []  # Chaves no nó
        self.children = []  # Referências para os filhos
        self.addresses = []  # Endereços no arquivo, usado apenas em folhas


class BTree:
    def __init__(self, order):
        self.root = BTreeNode(is_leaf=True)  # Nó raiz
        self.order = order

    def insert(self, key, address):
        """Insere uma chave e seu endereço na árvore."""
        root = self.root
        if len(root.keys) == self.order - 1:  # Nó está cheio
            new_root = BTreeNode(self.order)
            new_root.children.append(self.root)
            new_root.is_leaf = False
            self._split_child(new_root, 0)
            self.root = new_root
        self._insert_non_full(self.root, key, address)

    def _insert_non_full(self, node, key, address):
        i = len(node.keys) - 1

        if node.is_leaf:
            # Insere a chave e o endereço na posição correta
            while i >= 0 and key < node.keys[i]:
                i -= 1
            node.keys.insert(i + 1, key)
            node.addresses.insert(i + 1, address)
        else:
            # Encontra o filho onde a chave deve ser inserida
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1

            # Se o filho está cheio, divida-o antes de continuar
            if len(node.children[i].keys) == self.order - 1:
                self._split_child(node, i)
                if key > node.keys[i]:
                    i += 1

            self._insert_non_full(node.children[i], key, address)

    def _split_child(self, parent, index):
        order = self.order
        child = parent.children[index]
        mid = order // 2

        # Cria um novo nó
        new_node = BTreeNode(is_leaf=child.is_leaf)
        parent.keys.insert(index, child.keys[mid])  # Promove a chave do meio
        parent.children.insert(index + 1, new_node)

        # Divide as chaves e os filhos
        new_node.keys = child.keys[mid + 1 :]
        child.keys = child.keys[:mid]

        if not child.is_leaf:
            new_node.children = child.children[mid + 1 :]
            child.children = child.children[: mid + 1]

        if child.is_leaf:
            new_node.addresses = child.addresses[mid + 1 :]
            child.addresses = child.addresses[:mid]

    def search(self, key):
        """Busca uma chave na árvore."""
        return self._search(self.root, key)

    def _search(self, node, key):
        i = 0
        # Encontra a primeira chave maior ou igual a `key`
        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        if i < len(node.keys) and node.keys[i] == key:  # Chave encontrada
            if node.is_leaf:
                return node.addresses[i]  # Retorna o endereço na folha
            else:
                return node.children[i]  # Retorna o nó correspondente

        if node.is_leaf:  # Não encontrou e chegou em uma folha
            return None

        # Continua buscando no filho apropriado
        return self._search(node.children[i], key)
