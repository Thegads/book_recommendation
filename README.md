# Um recomendador de Livros

> **[Heroku](https://book-rec-nlp.herokuapp.com/)**<br />
> **[LinkedIn](https://www.linkedin.com/in/gustavo-röttgering-5058b554/)**

## Sobre o Projeto

> Por que um recomendador de livros?

 - Desde que iniciei minha caminhada no mundo de dados, consumi uma grande variedades de livros sobre diversos temas relacionados à Data Science. Resolvi então nesse projeto realizar um recomendador de livros, baseado em sua relevância a um tema, no caso de Natural Language Processing. Foi meu primeiro projeto do ínicio ao fim, ou seja, da criação da ideia até o deploy, beseado no curso do grande [Mario Filho](https://www.linkedin.com/in/mariofilho/).
 
> O que foi feito:

 1. Com a ideia em mãos, escolhi um site onde poderia procurar por livros e tivesse uma grande quantidade de títulos. O escolhido foi o site da Amazon. Nessa etapa, através de um webscrapping, foi extraído a lista de todos os livros retornados na pesquisa da query, e depois os dados de cada livro.
 2. Com os dados extraídos, foi criado um data set para treinar os modelos de Machine Learning.
 3. Para poder fazer as anotações dos exemplos do Data Set, ou seja, classificar a nossa variável, foi utilizado o Active Learning para auxiliar, pois esse recurso nos ajuda a poupar tempo e recursos.
 4. Tendo os dados já tratados e classificados, criei 3 modelos: **Random Forest**, **LightGBM** e **Logistic Regression**.(No final, por problemas na hora de criar o container, foi somente utilizado o **LightGBM**).
 5. Para tunar o modelo, foi utilizado o método **Bayesian Optimization**, em que dado uma série de parâmatros, retorna o melhor resultado dentro do spectro de valores.
 6. Finalizando o processo, com a ajuda do Docker, é criado um container e hospedado no [Heroku](https://book-rec-nlp.herokuapp.com/) para que todos possam acessar.
 
 ## Repositório
 
 - Análise de dados: Os notebooks com os códigos utilizados para a extração e análise dos dados e modelagem.
 - Deploy: os arquivos utilizados para criar o container e subir para o Heroku.
 
 ## Ferramentas utilizadas
 
 - Scikit-Learn
 - Scikit-Optimize
 - Pandas
 - Numpy
 - Flask
 - Requests
 - BeautifulSoup4
 - Selenium
 - Docker
 - Heroku
 
 ## Projeto em Andamento
 
 - Esse projeto foi o estudo de caso do curso do Mario Filho, encontrei diversas dificuldades no caminho, existem muitas melhorias a serem feitas:
  1. Alguns links das imagens não foram extraídos corretamente quando rodados em produção, individualmente não há esse problema.
  2. O modelo está trazendo um score muito parecido entre os resultados, isso se deve ao fato de não ter conseguido realizar o **Ensemble** dos modelos na hora de criar o container.
  3. O modelo pode melhorar muito. Foi uma primeira tentativa, em que eu gostaria de realizar o processo do início ao fim.
  4. Adicionar mais features e mais dados para o treinamento.
  
## Considerações Finais

  Agradecer novamente ao Mario Filho pelo execelente curso e materiais gerados gratuitamente para que todos possam ter acesso. E pelo apoio na parte final do [Rodrigo Fragoso](https://www.linkedin.com/in/rodrigo-a-fragoso/).
