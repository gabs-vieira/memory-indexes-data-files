# Memory-Indexes-Data-Files

Perguntas:
- Como determino a ordem da árvore? --> calculo baseado no tamanho da página
- Como devemos fazer a recriação /ou modificacao dos indices ? (atualmente eu removo/crio um produto e recrio o arquivo de produtos )
- A disposição dos dados está boa? Disponiveis no terminal --> AJustar o log pro "erro" == n achou 


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



### **Cálculo da Ordem da Btree**
Numero de registros = (Tamanho do ProductEntry /Tamanho do arquivo) = (5.299.952 /45 ) = 117776 


Tamanho do nó interno=(tamanho da chave+tamanho do ponteiro para filho)×(ordem−1)+metadados

4096 = (8bytes+8bytes)×(ordem−1)+16bytes

ordem = 256