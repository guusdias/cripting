# Algoritmos de Criptografia

## Objetivo

O objetivo desta atividade é a implementação de 3 algoritmos mais conhecidos de criptografia, que são:

- [x] AES (Advanced Encryption Standard)
- [x] RSA (Rivest-Shamir-Adleman)
- [x] SHA (Secure Hash Algorithm)

## Contexto

Cada arquivo contido no projeto contém o código de um dos algoritmos. Todos eles necessitam do _input_ do usuário, de algum valor específico, para que então retornem aquele conteúdo encriptado e então traduzido novamente.

Sendo assim, basta rodar cada um deles, inserir o texto que deseja e então verá a mágica ocorrer 🪄.

## Funcionamento

### AES

```shell
/usr/bin/python3.10

Digite o texto a ser criptografado: show demais
Texto inserido: show demais
Texto criptografado: b'\xa5mm\xdf\xf5C\xc2\xcbpe28\x95\xa9K\xf1\xf5-\x80\x18\x04XY)\xfbA\x90z\x90(\xce\xfb'
Texto descriptografado: show demais

Process finished with exit code 0
```

### SHA

```shell
/usr/bin/python3.10

A resposta da charada a seguir é a senha!


É feito de água, mas se for colocado dentro da água morrerá.


Senha: gelo
Senha Inserida Inicial: gelo
Senha Correta Inicial: gelo
Senha Inserida com SHA: 99cff4ccf498719e369db1a7350e7473ff9fd9d541e0f378451c055c46de4f45
Senha Correta com SHA: 99cff4ccf498719e369db1a7350e7473ff9fd9d541e0f378451c055c46de4f45


Senhas Batem: Sim!

Process finished with exit code 0
```

### RSA

```shell
/usr/bin/python3.10

Insira um texto para criptografar: show demais
Texto inserido: show demais


Chave pública usada para criptografar:
PublicKey(24436431406880159318235148681942486821312954056592023550704315625423282956756214539541956972146779798918198499844432171864118898703276994159959625957168767441601754047343724525542074547868276156757325391669675832798215654388251174540080799544851777047331784448709739327092096213520904221897799746825227597990603550471845878541314640991994700095043881081280911705681851036330471609428257564911279785517978568288369153505691603228496261550744904148397041394667746412123228659054044499531308602949180697034715448418653229075082617807022338165403669517091791772784980806692207814465753122330472436328320000605681796262477, 65537)


Texto criptografado:
b'\xb2\xdd\xa6z\x9d \x88`\xa1\xa9k3\xb8\x06\x10\x9a\x02\x06\x19\xda\xd0u\xcc\xb5O,>\xf3\xb4\xbb@\x08\x13\xee\xf2\xa5\x8f8\x03*\xa1\x99K\xb8\xbag\x0b\xa66\xc3*\xa7k\xday\xfcnI\xfb\xb53\x92\xab\xb2\xfe&Y\xcd\xc3L7\xe4V\x8f \x82$\xee\xfc\x1fEFa\x9f?LI\xf2j\xce\xf4\x07\xda~\xe4\x97\xd3\x82\xb5,\xf8\xb4\xb6\xcd\xe4\xd5\xe2t\x8e-\x10\x19\xde\r~\x08\xf6apn\x85\x05T\xf7c\xd7\xbd\x81\xb7(5\xd4a2\x99\xa93J~F#wB\xbcs\xf9\xcf\xdc\x04+\xaca\xfe\x14n\tj\xf1\x80\xeb\xacX\xfe\x9e\xa7\xa9\xf2\xceY\xdb\xb1\xe5_\xeef\xd1nz\x96Yir\xa3\xfd\xe6!\xacS\xf0\x89\xbc\x95d\x0b2\x1c/:\x1a\\O,}!\x08\xf4e\xc0\xb0Z\xc9g\xadF\x97\xe7\x07i\x81\xd2"\xc9z\x9a\xac\xfdo\xdd\xcc\n\x9d2\xfd\x86S\xc6\xb5\xbffa\xf2\x8d\xbab\xf6}gT\xd8^\xab\x02\x8bW\xd6<'


Chave privada usada para descriptografar:
PrivateKey(24436431406880159318235148681942486821312954056592023550704315625423282956756214539541956972146779798918198499844432171864118898703276994159959625957168767441601754047343724525542074547868276156757325391669675832798215654388251174540080799544851777047331784448709739327092096213520904221897799746825227597990603550471845878541314640991994700095043881081280911705681851036330471609428257564911279785517978568288369153505691603228496261550744904148397041394667746412123228659054044499531308602949180697034715448418653229075082617807022338165403669517091791772784980806692207814465753122330472436328320000605681796262477, 65537, 8465519304542581094056957377890691072082782380958318243056453331089464214873935256507935839230060706999691452774279994964721538614205729212623759826228843187727943358574422412193223072993901793841926174412443659426746543437002833006667904738793578376834777822047178260864838983044365922363035680736015255143792979876914918663550972115405822884031046203117580999472397703465458320730765035813628981876446003754126769410252154834584745483300610102682855772814542843186973646005778506746430120117886209596037773909904274738380852147275321842085658678666935280133819758045985984082493272323198238757225343491989467252225, 2703314108691667037522132122948194236639460809948301185998248731724241072357430515022670205531740206485357146636777301485837765142020980792472636673735353778817546248789929968288162729223539557387546267014132982476222701994455048167481233124248915337545618925527723138090039789477836335067965852348856357396056216824776862254373, 9039434717672061320884507162515155768812333674972740853346632909810826635048969937036053319638933244948023012180794013892113240356908484270905788961904431368533707404132082145899036561028851559060779187002511641953900978112917407856932495233232321592362605242123347544302308427023956413449)


Texto descriptografado: show demais

Process finished with exit code 0
```

## Rodar o projeto

Para rodar, basta instalar alguns pacotes necessários e após isso só rodar o arquivo que quiser.

```shell
$ pip install pycryptodome
$ pip install rsa
```
