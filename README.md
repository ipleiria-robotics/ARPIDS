

# DigitalTwinRL
 Este é um projeto desenvolvido no âmbito da tese de mestrado ["Comparação de Métodos de Aprendizagem por Reforço em Processos Industriais Discretos Sequenciais"](Thesis/dissertation.pdf), realizada sob a orientação do Doutor Luís Miguel Perdigoto e do Doutor Luís Manuel Conde Bento, na Escola Superior de Tecnologia e Gestão ESTG, no Politécnico de Leiria. 

 Este repositório contém os documentos, códigos, vídeos, resultados e tutoriais para que o usuário replique os algoritmos de Aprendizagem por Reforço, permitindo experimentar diferentes métodos e configurações, comparando a performance de cada ao processo industrial simulado.

 <p align="left">
  <img src="Tutorials/Videos/Reference.gif" alt="gif" width="65%" />
 </p> 

# Introdução
 O processo de comissionamento de equipamentos durante a implementação de um novo sistema, ou na reconfiguração de um já existente, é uma etapa em que as empresas gastam dinheiro e tempo antes da entrada em operação. 
 
 Baseando-se nesse problema, este trabalho utiliza gémeos digitais, que simule um processo de empacotamento de latas, em conjunto com a utilização de técnicas de Aprendizagem por Reforço para permitir que o sistema se reconfigure e se programe de forma automática. 

  Dessa forma, este trabalho permite aplicar alguns dos diferentes algoritmos de Deep Reinforcement Learning a um sistema de empacotamente de latas, no qual o principal objetivo é avaliar a viabilidade e o desempenho de utilizá-los na aprendizagem e otimização automática das sequências de controlo em processos industriais de natureza sequencial e discreta. Dada essa natureza, com necessidade inerente de efeito de memória, podem ser  experimentadas diferentes arquiteturas de redes neuronais, comparando o uso de redes MLP's (Multilayers Perceptron) com o uso de LSTM (Long Short-Term Memory) e com o uso de buffers de memória de estados anteriores de diferentes tamanhos. 
  
 # [Documentação](Tutorials/documentation_tutorial.md)
Descreve a arquitetura e um conjunto de links das bibliotecas e frameworks utilizados.

# [Instruções de instalação](Tutorials/quick_setup.md)
Passos de instalações de pacotes Python. 

# [Tutorial da esteira da caixa de latas](Tutorials/boxconveyor_tutorial.md)
Tutorial completo de como treinar e utilizar a esteira da caixa de latas no processo de empacotamento.

# [Tutorial da garra manipuladora de latas](Tutorials/handling_tutorial.md)
Tutorial completo de como treinar e utilizar a garra manipuladora de latas no processo de empacotamento.  

# [Vídeos](Tutorials/videos.md)
Vídeos mostrando a performance de algoritmos aplicados à esteira da caixa de latas e à garra manipuladora de latas.

# [Resultados](Tutorials/videos.md)
Resultados de algoritmos aplicados à esteira da caixa de latas e à garra manipuladora de latas.






