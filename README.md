# Jogo da Memória :video_game:

E aí, beleza?! Bem-vindo ao jogo da memória!! :grin:

Esse jogo foi um projeto de finalização do curso de Introdução a Programação, teve como objetivo consolidar a prática e experiência na implementação de software utilizando a
linguagem de programação Python, fazendo uso dos conhecimentos adquiridos na disciplina.

# Aspectos que foram avaliados no código:
- Uso de recursos (laços de repetição, estruturas de decisão, estruturas de dados); 
- Linguagem de forma apropriada; 
- Comentários no código; 
- Modularidade (uso de funções e bibliotecas); 
- Qualidade do código (uso de variáveis em vez de números mágicos, repetição desnecessária de instruções, etc); 
- Jogabilidade da interface; 
- Lógica da aplicação.

# Regras do jogo

- Considere um baralho em que cada carta tem uma figura especial do baralho (A, J, Q, K) e um
naipe (Copas, Ouro, Espada, Paus), conforme exemplos abaixo. O jogo completo é composto por
um total de 32 cartas, sendo 16 cartas únicas, e uma cópia de cada uma delas.

![image](https://github.com/Endril18/Jogo-Da-MemoriaTerminal/assets/105693005/a91a4f54-8bc8-4453-ae15-7fe4e1c1efd2)

- Para compor o tabuleiro, devem ser escolhidas aleatoriamente 20 cartas, dentre as 32 possíveis,
organizadas em 4 linhas e 5 colunas também de forma aleatória.

- É necessário que as cartas existam aos pares no tabuleiro para garantir as chances de sucesso do
jogador; portanto, na hora da escolha aleatória das cartas, é preciso cautela para não deixar cartas
sem correspondência.

- No início do jogo, o conteúdo de todas as cartas do tabuleiro deverá estar oculto.

- Cada partida terá participação de dois jogadores, e cada um poderá fazer cinco jogadas
alternadamente.

- Em cada jogada, o jogador escolherá duas cartas do tabuleiro para terem seus conteúdos
revelados (exibidos).

- Caso as cartas escolhidas sejam iguais, o jogador acumulará 50 pontos e o conteúdo delas
permanecerá visível até o final do jogo.

- Caso as cartas escolhidas não sejam iguais, mas tenham a mesma figura (A, J, Q, K), o jogador
acumulará 20 pontos e o conteúdo das cartas novamente será ocultado.

- Caso as cartas escolhidas não sejam iguais, mas tenham o mesmo naipe (Copas, Ouro, Espada
ou Paus), o jogador acumulará 30 pontos e o conteúdo das cartas novamente será ocultado.

- Caso as cartas não sejam iguais, nem tenham a mesma figura, nem tenham o mesmo naipe, o
jogador não acumulará pontos e o conteúdo das cartas novamente será ocultado.

- O jogo acaba quando todas as cartas tiverem sido reveladas (todos os pares encontrados), ou
quando acabarem as chances dos jogadores (dez rodadas).

- Vencerá o jogador que tiver acumulado maior quantidade de pontos ao final do jogo, não sendo
descartada a possibilidade de empate.
