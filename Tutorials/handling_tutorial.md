# Introdução 

A garra manipuladora de latas é um sistema que consiste em coletar latas transportadas por uma esteira de alimentação e posicioná-las em uma caixa numa segunda esteira. É composta por uma garra, um motor que se movimenta no eixo x e outro motor que se movimenta no eixo y. Cabe a essa máquina preencher 3 fileiras com 3 latas na caixa, sem deixar que as latas batam umas nas outras ou batam em obstáculos, sem realizar a captura das latas quando qualquer uma das esteiras esteja em movimento. A cada fileira preenchida pela garra, esse agente deve enviar um sinal de conclusão à esteira da caixa de latas para que ela se mova para outra posição alvo. 

É permitido a garra realizar 11 tipos diferentes de ações discretas:

•	Abrir a garra;<br>
•	Fechar a garra;<br>
•	Sinalizar preenchimento de fileira à esteira da caixa de latas;<br> 
•	Movimentar para as 8 posições descritas na figura imagem abaixo, podendo se deslocar de qualquer posição para a outra.<br>

<p align="center"><img src="Images/handling_positions.PNG" style="width:70%"></p>

Por sua vez, o sistema recebe informações de estado de 6 variáveis:<br> 

•	Sensor de fim de curso da esteira da caixa de lata (variável discreta);<br>
•	Sensor de presença de lata na garra (variável discreta);<br>
•	Posição da garra no eixo Y (variável contínua);<br>
•	Posição da garra no eixo X (variável contínua);<br>
•	Sensor de fim de curso da garra, indicando se está fechada ou aberta (variável discreta);<br>
•	Sinal enviado pela esteira da caixa de lata, indicando que se ela está em movimento ou não está sobre o sensor de fim de curso da posição da garra (variável discreta).<br>

# Para treinamento da garra manipualdora de latas:

## Abra o Jupyter Notebook:

Se você instalou o Anaconda, abra o Anaconda Navigator e clique no botão "Launch" para o Jupyter Notebook.<br>
Se você instalou o Python e o Jupyter Notebook usando o pip, abra o terminal ou prompt de comando e digite o comando "python -m notebook".<br>
No Linux ou macOS, abra o terminal e digite o comando "python -m notebook".<br>

Independentemente do método escolhido, após o Jupyter Notebook ser iniciado, ele abrirá uma página da web no seu navegador padrão com o endereço "http://localhost:8888/tree". A partir daí, você pode criar um novo notebook ou abrir um já existente.

## Ative o servidor websocket via notebook (opção 1):

Todos os processos de treino e teste requerem ativação do servidor websocket para gestão de comunicação entre agente (cliente) e ambiente (servidor). Para isto siga os passos seguintes:

### 1- Abra o notebook Socket Communication:

Executar o ficheiro no diretório DigitalTwinRL/Socket/Socket Communication.ipynb 

### 2- Execute o servidor websocket:

Basta correr a primeira célula do notebook e o ficheiro python irá ativar conexão TCP/IP local, porta 12000. Caso já esteja ativo e a célula for executada novamente, a conexão será desativada. Em todo treinamento ou teste, deve-se certificar que a conexão esteja ativa.

## Ative o servidor websocket por arquivo executável (opção 2):

O diretório DigitalTwinRL\Socket\dist\socket_communication contém o ficheiro executável socket_communication.exe que também pode ser utilizado para iniciar a comunicação socket. Basta abri-lo.

## Gerar o ambiente de treinamento da garra manipualdora de latas:

### 1- Abra o notebook de ambiente:

Executar o ficheiro no diretório DigitalTwinRL/Enviroment/Handling_enviroment.ipynb

### 2- Prepare o ambiente de treinamento:

Execute as células abaixo de criação do ambiente:

1 - Importa bibliotecas;<br>
2 - Cria funções de encoding/decoding em json;<br>
3 - Define função do ambiente de treino.<br>

### 3- Verifique a conexão websocket:

Execute a célula 4 "Verifica se o servidor socket está ativo" para checar se o servidor está ativo. Caso não esteja, verifique o notebook Socket Communication.ipynb nos passos anteriores.

### 4- Ative o ambiente de treinamento:

Execute a célula 5 "Ativa o ambiente para treino". A célula ficará permanentemente a correr, aguardando comandos do agente. Um log ações é exebido abaixo da célula durante o treinamento do agente.

## Treinar o agente da garra manipualdora de latas:

### 1- Abra o notebook de treinamento do agente:

Executar o ficheiro no diretório DigitalTwinRL/Agent/Handling_Agent.ipynb

### 2- Prepare o agente para o treinamento:

Execute as células abaixo de criação do agente:

1 - Importa bibliotecas;<br>
2 - Cria funções de encoding/decoding em json;<br>
3 - Define função de criação do agente.<br>

### 3- Crie o modelo de Apendizagem por Reforço:

Defina valores, parâmetros e execute a célula 4 "Cria o modelo em Aprendizagem por Reforço". Abaixo segue a descrição de cada variável a definir:

- algoritmo: Especifica o algoritmo de aprendizagem por reforço a ser utilizado para treinar o modelo de rede neuronal;<br>
- nome_do_ficheiro: Nome do arquivo a ser salvo após o treinamento do modelo;<br>
- tamanho_buffer: Define o tamanho do buffer utilizado pelo algoritmo de aprendizado por reforço. O buffer é uma estrutura de dados que armazena amostras de experiência que serão usadas para treinar o modelo em lotes;<br>
- funcao_ativacao:  Especifica a função de ativação a ser usada nas camadas da rede neuronal. As funções de ativação são usadas para adicionar não-linearidade aos modelos de rede neuronal e podem afetar significativamente o desempenho do modelo;<br>
- rede_neuronal:  Define a arquitetura da rede neural que será utilizada no modelo, especificando o número de neurónios nas camadas de política e valor da rede neuronal. ver: https://stable-baselines3.readthedocs.io/en/master/guide/custom_policy.html;
- tipo_camadas:   Define o tipo de camadas do modelo;<br>
- fator_desconto:  Especifica o fator de desconto utilizado na aprendizagem por reforço. Este fator é utilizado para controlar a importância que as recompensas futuras têm sobre as recompensas atuais. Quanto maior o fator de desconto, maior será a importância das recompensas futuras;<br>
- save_path:  Define o caminho onde o modelo será salvo após o treinamento. Esta variável é construída concatenando-se vários elementos, como o diretório onde os modelos são salvos, o nome do arquivo e o tamanho do buffer utilizado durante o treinamento.<br>

### 4- Define funções de callback:

A execução da célula 5 "Define funções de callback" cria diretórios dentro de DigitalTwinRL\Agent\Training_Handling que permitem gerar logs e salvar modelos durante o treinamento. Os logs descrevem a performance do agente durante o treinamento e podem ser visualizados por meio do Tensorboard. Ver link: https://stable-baselines3.readthedocs.io/en/master/guide/tensorboard.html

### 5- Inicie o treinamento do agente:

A execução da célula 6 "Inicia treino" realiza o treinamento do agente. Importante definir a quantidade de passos de treino em n_steps.

### 6- Salve o modelo (se desejar):

A execução da célula 7 "Salva o modelo (caso necessário)" salva o modelo no diretório definido em save_path.

# Para teste do agente treinado:

### 1- Carregue um modelo do diretório (se desejar):

A execução da célula 8 "Carrega o modelo (caso necessário)" carrega um modelo salvo previamente em diretório. os parâmetros seguintes devem ser definidos na célula:

- nome_do_ficheiro_carregar: Nome do arquivo a ser carregado, referente ao modelo treinado com o algoritmo;<br>
- algoritmo_carregar: O algoritmo que será carregado;<br>
- tamanho_buffer_carregar: O tamanho do buffer que foi utilizado para treinar o modelo que será carregado.<br>

### 2- Certifique que a conexão websocket esteja ativa:

Reabra a conexão ou certifique que esteja ativa. Descrição no início deste tutorial.

### 3- Carregue a realidade virtual:

Execute o ficheiro DigitalTwinRL\Virtual_Reality\DigitalTwinRL.exe que irá iniciar a realidade virtual. 

### 4- Inicie o teste do agente:

A execução da célula 9 "Utiliza modelo treinado no ambiente" executa o modelo treinado em Aprendizagem por Reforço para acionamento da garra manipuladora de latas na realidade virtual.  

As linhas de código "mensagem = encode_json('BoxConveyor_automatico', [])" podem ser alteradas para manter o comando da esteira de latas e esteira de caixa de latas no modo manual ou modo automático, conforme necessidade do usuário. 












