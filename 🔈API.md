# API

O um dos termos mais usados no mundo da programacao hoje e dia de fato podemos dizer que e a famosa API, uma palavra que todos usam e nao e atoa. **Muitos sistemas usam API no seu dia a dia de funcionamento.**

## O que e uma API

 A sigla API, **Application Programming Interface (Interface de Programação de Aplicação)**, um nome bonito para dizermos que e uma forma de dois sistemas se comunicarem usando padroes e protocolos para esta comunicacao. 

 Imagine o sistema de clima tempo, onde mostra as informacoes do clima de uma certa regiao, um outro sistema precisa dessas informacoes, **a API e a responsavel pelo envio da informacao.**

 Pense em um restaurante a um cliente que quer um pedidos especifico do cardapio, para isso ele chama o garson, o garson anota o pedidos, e envio para o chef(cozinha), a cozinha realiza o pedidos e o garsom etrega o pedido para o cliente. Quem voce acha que e a API neste caso ? **A API  nesta situacao e o garsom**, ela realiza a requisicao dos dados e levam e traz eles.

 ## Tipos de API

**A quatro maneiras de uma APIs** se comportar cada uma criada para uma funcao especifica e suas acoes, algumas sao formas antigas outras sao para certas aoces especificas e aqui vamos falar um pouco de cada uma.

**APIs SOAP**
Essas APIs usam o Simple Object Access Protocol (Protocolo de Acesso a Objetos Simples). Cliente e servidor trocam mensagens usando XML. Esta é uma API menos flexível que era mais popular no passado.

**APIs RPC**
Essas APIs são conhecidas como Remote Procedure Calls (Chamadas de Procedimento Remoto). O cliente conclui uma função (ou um procedimento) no servidor e o servidor envia a saída de volta ao cliente.

**APIs WebSocket**
A API de WebSocket é outro desenvolvimento de API da Web moderno que usa objetos JSON para transmitir dados. Uma API WebSocket oferece suporte à comunicação bidirecional entre aplicativos cliente e o servidor. O servidor pode enviar mensagens de retorno de chamada a clientes conectados, tornando-o mais eficiente que a API REST.

**APIs REST**
Essas são as APIs mais populares e flexíveis encontradas na Web atualmente. O cliente envia solicitações ao servidor como dados. O servidor usa essa entrada do cliente para iniciar funções internas e retorna os dados de saída ao cliente. Vejamos as APIs REST em mais detalhes abaixo.


## API REST

Uma API reste e nada mais que uma Api que segue os protocolos HTTP. O nome REST(Transferencia Representacional de Estado) ele vai definir que o clinete e o servidor se comuniquem pelos protocolos

- Get: Pegar uma informacao
- PUT: Atualizar uma informacao
- POST: Enviar uma informacao
- DELETE: Deletar uma informacao

Sao essas as 4 acoes que uma API REST pode realizar e sao por via dessas que o cliente e o servidor conseguem se comunicar.

## O que é API Web?
Uma API Web ou API de serviço da Web é uma interface de processamento de aplicações entre um servidor da Web e um navegador da Web. Todos os serviços da Web são APIs, mas nem todas as APIs são serviços da Web. A API REST é um tipo especial de API Web que usa o estilo de arquitetura padrão explicado acima.

Os diferentes termos que abrangem as APIs, como API Java ou APIs de serviço, existem porque, historicamente, as APIs foram criadas antes da World Wide Web. As APIs Web modernas são APIs REST e os termos podem ser usados de forma intercambiável.

## Integracao de API

A integracao de API ocorre quando um sistema atuliza os dados automaicamente com o cliente e o servidor. Alguns dos exemplos mais solidos de atualizacao automatica dos dados sao o tempo do laptop quando voce troca de regiao e automaticamente e trocado a hora e a data.

## Vantagens da API REST

Por simula as APIs REST tem 4 vantagens

**INTEGRACAO**

As APIs sao usadas a integracao de um recurso novo na aplicacao com uma ja existente. Assim almentando a velocidade do sistema, sem ter que criar linhas de codigo do zero, podendo reutilizar varios padroes

**INOVACAO**

Diversos setores de uma empresa podem receber uma alteracao rapida e atualizacao de alguma implementacao. As inovacoes podem chegar rapido se usar uma API apenas trocando o nivel da mesma, apenas atualizando a API muitas coisas ja podem mudar, sem precisar reescrever o codigo inteiro.

**EXPANSAO**

As APIs sao um vasto campo para a empresa para satisfazer as necessidades do cliente, nelas voce pode encontrar varias informacos. Uma API de maps sao umas das mais formas que temos e podemos usar podendo ser gratuitas ou pagas.

**FACILIDADE DE MANUTENCAO**

A API atua como um gateway entre dois sistemas. Cada sistema é obrigado a fazer alterações internas para que a API não seja afetada. Dessa forma, qualquer alteração futura de código feita por uma parte não afetará a outra parte.


## Os tipos de API

APIs sao classificadas pelos seus escopos e arquiteturas, anteriormente vimos os principais arquiteturas de APIs agora iremos olhar os principais escopos.

**API publicas**

Sao abertas ao publico geral, podendo ter algum tipo de autorizacao dependendo das informacoes, podendo tambem ser pagas ou gratuitas.

**API privada**

Sao internas de uma empresa, somente membros podem usa-las e sao usadas apenas para conectar sistemas e dados dentro da empresa

**APIs de parceiros**

Estas são acessíveis apenas por desenvolvedores externos autorizados para auxiliar as parcerias entre empresas.

**APIs compostas**

Estas combinam duas ou mais APIs distintas para atender a requisitos ou comportamentos complexos do sistema. 


## JSON

As APIs REST enviam as informacaoes atravez de um arquivo que nomeamos de JSON este formato e um padrao para os envios de informacoes das APIs modernas sendo utilizado em todas hoje em dia, as APIs que nao utilizam por muitas vezes sao APIs no formato antigo
O formato JSON por se so e mais rapido para os envios de informacoes e muitas das vezes vem assim 

```
[
  {
    "id": 1,
    "product": "Laptop",
    "price": 999.99
  },
  {
    "id": 2,
    "product": "Mouse",
    "price": 25.50
  }
]
```

Muitas das vezes o JSON e sua maior parte e um Arry, muito sendo um dicionario dentro de um dicionario, assim podendo realizar sua manipulacao de uma maneira rapida e pratica do que os outros formatos.

## O que sao EndPoints e como elas funcionam

As endpoints sao o caminho especifico que e pego para obter a informacao desejavel, muita das suas vezes elas sao em formato de URLs, sendo muito usadas para saber o caminho especifico que cada um pode ter.
Pensando no exemplo do restaurante as endponits sao o cardapito e voce pede algo especifico do cardapio.

**SEGURANCA**

Os endpoints da API tornam o sistema vulnerável a ataques. O monitoramento da API é crucial para impedir o uso indevido.

**PERFORMACE**

Os endpoints da API, especialmente os de alto tráfego, podem causar gargalos e afetar a performance do sistema.

## Como proteger uma API REST?

Todas as APIs devem ser protegidas por meio de autenticação e monitoramento adequados. As duas principais maneiras de proteger APIs REST incluem:

1. **Tokens de autenticação**
Eles são usados para autorizar os usuários a fazer a chamada de API. Os tokens de autenticação verificam se os usuários são quem afirmam ser e se têm direitos de acesso para aquela chamada de API específica. Por exemplo, quando você faz login em seu servidor de e-mail, seu cliente de e-mail usa tokens de autenticação para acesso seguro.

2. **Chaves de API**
As chaves de API verificam o programa ou a aplicação que faz a chamada de API. Elas identificam a aplicação e garantem que ela tenha os direitos de acesso necessários para fazer a chamada de API específica. As chaves de API não são tão seguras quanto os tokens, mas permitem o monitoramento da API para coletar dados sobre o uso. Você pode ter notado uma longa sequência de caracteres e números no URL do seu navegador ao visitar diferentes sites. Essa string é uma chave de API que o site usa para fazer chamadas de API internas.


# Criando API 

