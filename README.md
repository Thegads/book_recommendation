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
  
## Versão 0.1
 
  Adicionado um botão para receber uma informação na qual irá gerar uma nova página com essa informação. Funciona parcialmente. A informação é recebida, começa a extração das novas informações mas a página não é retornada. Precisa de algum trabalho para funcionar corretamente.
  [New APP](https://limitless-ridge-12360.herokuapp.com/)


# ENGLISH VERSION

# Book Recommendator

> **[Heroku](https://book-rec-nlp.herokuapp.com/)**<br />
> **[LinkedIn](https://www.linkedin.com/in/gustavo-röttgering-5058b554/)**

## About the Project

> Why a book recommendator?

 - Since I've started my journey into the data world, I haeve read several books related to Data Science. Based on this, I have decided to make a recommendator on books, returning its relevance on the theme, in this casa Natual Language Processing. It was my first start to end(hypothesis to deploy) project, based on the great course by [Mario Filho](https://www.linkedin.com/in/mariofilho/).
 
> Stages:

 1. With the idea on my mind, I chose a site with a great variety and a great number of titles. The site was amazon.com. Firstly was to scrape a list of all the titles in the query page then the book data from each book.
 2. With the scrapped data, a dataset was created in order to train the Machine Learning model.
 3. To set up our variable, this process was made with the help of **Active Learning** which help save time and resources.
 4. With the processed data and the variable set, was created three models: **Random Forest**, **LightGBM** e **Logistic Regression**.(For production, I had some problems with the models so it was only used **LightGBM**).
 5. For model improvement was used **Bayesian Optimization** method, with a given set of parameters, returns the best output from those values.
 6. Deploying was made with Docker and hosted by[Heroku](https://book-rec-nlp.herokuapp.com/).
 
 ## Repository
 
 - Análise de dados: Notebooks for scrapping, analisys and models.
 - Deploy: files to create the container and deploy.
 
 ## Tools and Libraries
 
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
 
 ## Work in Progress
 
 - Project based on a case study from Mario Filho's course, with several problems along the way, the project has many wasy of improvements:
  1. Some image links hasn't been extract correctly in production, what didn't happen locally.
  2. The model returns a score way similar to each result. This should be result of not being able to deploy the ensembled model.
  3. The models could improve greatly. It was a first try which I wanted to make a project from beginning to end.
  4. Add more features and data.
  
## Summarizing

  Thank again Mario Filho for the excelent course and all free material that he makes available for everybody and lastly to [Rodrigo Fragoso](https://www.linkedin.com/in/rodrigo-a-fragoso/) for his help on the last part of the project and improvements.
  
 ## Version 0.1
 
  Add a button to receive an input and return the page with the new results of that input. It works partially. On the background, it is received, and start the processing for the new data, but the page is not returned. Still need some work on that part.
  [New APP](https://limitless-ridge-12360.herokuapp.com/)
