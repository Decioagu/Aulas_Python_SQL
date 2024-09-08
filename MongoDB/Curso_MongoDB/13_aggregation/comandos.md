No MongoDB, o "framework aggregation" é um conjunto poderoso de ferramentas que permite realizar análises complexas e transformações de dados em seus documentos. Ele oferece diversas funcionalidades para agrupar, filtrar, calcular e processar informações de maneira eficiente, extraindo insights valiosos de suas coleções.

# 1 - bucket
### permite agrupar documentos com base em um campo específico, dividindo-os em categorias pré-definidas ou com base na distribuição dos dados.

db.books.aggregate([
  {
    $bucket: {
      groupBy: "$pageCount",
      boundaries: [100, 200, 300, 400, 500, 600, 700],
      default: "OTHERS",
      output: {
        "count": {$sum: 1}
      }
    }
  }
])

# 2 - bucketauto
### agrupa automaticamente documentos em um número especificado de buckets com base em uma expressão, é útil para analisar grandes conjuntos de dados e identificar padrões ou tendências sem precisar definir manualmente limites.

db.books.aggregate([
  {
    $bucketAuto: {
      groupBy: "$categories",
      buckets: 3
    }
  }
])

# 3 - collStats
### retorna estatísticas sobre uma coleção específica como: nome da coleção, número de documentos, tamanho da coleção, espaço em disco usado pela coleção, número de índices, tamanho total dos índices, estatísticas de latência de consulta e estatísticas de armazenamento.

db.books.aggregate( [ { $collStats: { queryExecStats: { }, count: { } } } ] ).pretty()

# 4 - sort
### é usado para ordenar os resultados de uma agregação. Ele pode ordenar os documentos por um ou mais campos, em ordem crescente = 1 ou decrescente = -1.

db.books.aggregate([
  { $sort: { pageCount: -1 } }
]).pretty()

# 5 - limit
### é útil para reduzir o conjunto de resultados a um número gerenciável.

db.books.aggregate([
  { $sort: { pageCount: -1 } },
  { $limit : 3 }
]).pretty();

# 6 - match
### é usado para filtrar documentos em um pipeline de agregação, permite que você especifique critérios para selecionar quais documentos devem passar para o próximo estágio do pipeline.

db.books.aggregate([
  { $sort: { pageCount: -1 } },
  { $match: { authors: "Gavin King"}},
  { $limit : 3 }
]).pretty();


# 7 - out
### serve para gravar os documentos resultantes do pipeline de agregação em uma nova coleção.

db.books.aggregate([
  { $match: { categories: "Java", pageCount: { $gt: 800 }}},
  { $limit : 5 },
  { $out: "bigjavabooks" }
]).pretty();

db.bigjavabooks.find().pretty()

# 8 - project
### é utilizado em pipelines de agregação para selecionar os campos de retorno dos documentos processados. 
db.books.aggregate([
  { $sort: { pageCount: -1 } },
  { $match: { authors: "Gavin King"}},
  { $limit : 3 },
  { $project: { title: 1 } }
]).pretty();

# 9 - sample
### é um operador que permite amostragem aleatória de documentos de uma coleção. Ele é útil para obter um subconjunto representativo de uma coleção grande sem precisar processar todos os documentos.
db.books.aggregate([
  { $sort: { pageCount: -1 } },
  { $match: { categories: "Java" }},
  { $project: { title: 1 } },
  { $sample: { size: 10 } }
]).pretty();

# 10 - skip
### é utilizado dentro do pipeline de agregação para ignorar um número especificado de documentos e passar os documentos restantes para o próximo estágio do pipeline. 

db.books.aggregate([
  { $sort: { pageCount: -1 } },
  { $match: { categories: "Java" }},
  { $project: { title: 1 } }
]).pretty();

db.books.aggregate([
  { $sort: { pageCount: -1 } },
  { $match: { categories: "Java" }},
  { $project: { title: 1 } },
  { $skip: 5 }
]).pretty();

# 10.5 - unwind
###  é usado para desconstruir um campo de array em um documento e criar documentos de saída separados para cada item no array, transforma documentos complexos em documentos mais simples, aumentando a legibilidade e a compreensão. Isso também permite a realização de operações adicionais, como agrupamento e classificação na saída resultante.
db.books.aggregate( [ 
  { $unwind : "$categories" },
  { $project: { categories: 1 } }
] )

# 11 - sortByCount
### é utilizado para ordenar os resultados de uma consulta com base na contagem de documentos em cada grupo, agrupa os documentos de acordo com um campo ou expressão específica.
db.books.aggregate( [ { $unwind: "$categories" },  { $sortByCount: "$categories" } ] )

# 12 - unset
### é usado para remover campos específicos de documentos dentro de uma pipeline de agregação. Ele pode ser utilizado para eliminar campos que não são mais necessários ou proteger informações confidenciais.
db.books.aggregate([
  { $sort: { pageCount: -1 } },
  { $match: { categories: "PowerBuilder" }},
  { $unset: "_id" }
]).pretty();

db.books.aggregate([
  { $sort: { pageCount: -1 } },
  { $match: { categories: "PowerBuilder" }},
  { $unset: ["_id", "status"] }
]).pretty();

# 13 - count
### é utilizado para contar o número de documentos em um estágio de agregação.
db.books.aggregate([
  { $sort: { pageCount: -1 } },
  { $match: { categories: "Java" }},
  { $project: { title: 1 } },
  { $count: "Contagem" }
]).pretty();

