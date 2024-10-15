#Coleta e amostragem de dados:

nome = input('Digite seu nome:');
print(f'Óla, {nome}!');

#nome = input('Digite seu nome:');
idade = input('Digite sua idade: ');
print(f'Seu nome é {nome} e sua idade é {idade} anos.');

#nome = input('Digite seu nome:');
#idade = input('Digite sua idade:');
altura = input('Digite sua altura em metros:');
print(f'Seu nome é {nome}, sua idade é {idade} anos e sua altura é {altura} em metros!');

#Calculos:

valor1 = input('Digite o primeiro valor: ');
valor2 = input('Digite o segundo valor: ');
print(f'O primeiro número é {valor1}, e o segundo é {valor2}!');

valor1 = float(input('Digite o primeiro valor: '));
valor2 = float(input('Digite o segundo valor: '));
valor3 = float(input('Digite o terceiro valor: '));
soma = float(valor1)+float(valor2)+float(valor3);
print(f'A soma dos valores é {soma}!');

valor1 = float(input('Digite o primeiro valor: '));
valor2 = float(input('Digite o segundo valor: '));
subt=float(valor1)-float(valor2);
print(f'A subtração dos valores é {subt}!');

valor1 = float(input('Digite o primeiro valor: '));
valor2 = float(input('Digite o segundo valor: '));
mult=float(valor1)*float(valor2);
print(f'A multiplicação dos valores é {mult}!');

numerador = int(input('Digite o numerador: '));
denominador = int(input('Digite o denominador:'));
div=numerador/denominador;
print(f'A divisão dos valores é {div}');

numerador = int(input('Digite o numerador: '));
denominador = int(input('Digite o denominador:'));
div=numerador%denominador;
print(f'O resto divisão dos valores é {div}');

operador = int(input('Digite o operador valor: '));
potencia = int(input('Digite a potência valor: '));
print(f'resultado é {operador**potencia}');

#calculo de média
nota1=float(input('Digite a primeira nota: '));
nota2=float(input('Digite a segunda nota: '));
nota3=float(input('Digite a terceira nota: '));
media=nota1+nota2+nota3/3;
print(f'A media ficou {media}!');

#calculo média mais elaborado
quant=int(input('Quantas notas serão calculadas?'))
soma = 0;
for i in range(quant):
    nota=float(input(f'Digite a nota {i+1}:'))
    soma += nota

media = soma / quant
print(f'A média das notas é: {media}.');

#Editando textos

frase = input('Digite uma frase: ')
print(frase)

frase = input('Digite uma frase: ')
print(frase.strip().lower())

frase = input('Digite uma frase: ')
print(frase.lower().replace('a',chr(162)))
