
### **Checklist**

- [ ] Implementação Btree +
  - [x] Query + Search
  - [ ] Add
  - [ ] Remove


- [ ] Implementação Tabela Hash +
  - [x] Query + Search
  - [ ] Add
  - [ ] Remove

- [x] Search no arquivo
- [x] Implementação de count time
  - criação de indices (memoria e file)

- [x] Consultas (5) no arquivo e na memoria
  - [x] Montar tabela de comparacao para os 3 metodos 
    - Hash
    - Btree
    - File

- [ ] Inserção e remocao de novos registros com recriação ou modificacao dos indices 
  - [ ] Montar tabela de comparacao para os 3 metodos 
    - Hash
    - Btree
    - File

- [x] Tratamento de erros nas queries caso nao encontre o resultado


Perguntas:
- Como determino a ordem da árvore?
- Como devemos fazer a recriação /ou modificacao dos indices ? (atualmente eu removo/crio um produto e recrio o arquivo de produtos )
- A disposição dos dados está boa? Disponiveis no terminal


Perguntas a se responder
Arvore: BTree +
Quantidade de elementos por nodo: 256 
Estratégia Colisões: Encadeamento Direto

---


### **Estratégia de Resolução de Colisões: Encadeamento Direto**
**Descrição:**

- Cada posição da tabela é um "balde" que contém uma lista.
- Se ocorrer uma colisão (duas ou mais chaves resultam no mesmo índice), as chaves conflitantes são armazenadas nessa lista associada ao índice.
- A busca, inserção e remoção ocorrem iterando sobre essa lista para encontrar a chave correspondente.

**Vantagens:**

- Fácil implementação e manipulação de colisões.
- Não há limite fixo para a quantidade de elementos por índice (exceto pela memória disponível).
- Preserva todas as entradas sem necessidade de realocar dados.

**Desvantagens:**
- Se houver muitas colisões em um único índice, o desempenho degrada para 𝑂(𝑛) na lista associada ao índice.