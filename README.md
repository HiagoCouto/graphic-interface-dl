# SNG-Classifier
## Dependências
Para ter o software funcionando é necessário ter os seguintes programas e bibliotecas Python instaladas:
#### Linguagem:
- Python 3.x

#### Bibliotecas da Linguagem:
  - *PyQt5*
  - *Keras*
  - *Tensorflow*
  - *numpy*
  - *scikit-learn*
  
## Submissão de *Datasets*
Quaquer *dataset* que for submetido para treino deverá seguir algumas regras:
  1. Precisa ser um .zip
  2. Deve conter uma pasta com o nome do *dataset* no interior
  3. O nome do zip deve ser igual ao da pasta compactada
  4. Dentro da pasta as imagens devem estar contidas, separadas por pasta conforme o tipo. O nome das pastas corresponde aos *labels*
  
## Possíveis Problemas
A depender de como foram configuradas as bibliotecas *Python*: *Tensorflow* e *Keras*, alguns problemas podem ocorrer na execução da aplicação. Esse problema pode, também, ocorrer a depender das versões usadas.

O aplicativo usa o Inceptio-V3 no *backend*, deste modo, se o Inceptio-V3 nunca tiver sido usado ná máquina, o download  do mesmo irá iniciar. Isso pode demorar a depender da sua internet.
