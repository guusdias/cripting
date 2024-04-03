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

```bash
/usr/bin/python3.10

Digite o texto a ser criptografado: show demais
Texto inserido: show demais
Texto criptografado: b'\xa5mm\xdf\xf5C\xc2\xcbpe28\x95\xa9K\xf1\xf5-\x80\x18\x04XY)\xfbA\x90z\x90(\xce\xfb'
Texto descriptografado: show demais

Process finished with exit code 0
```

### SHA

```bash
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
