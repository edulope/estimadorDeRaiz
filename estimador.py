print("insira o numero desejado")
numero = float(input())
print("insira a raiz desejada")
raiz = int(input())
imaginario = False
negativo = False
expoencial = False
menorQueUm = False
if(raiz%2 == 0 and numero < 0):
    imaginario = True
    numero = -numero
if(numero<1):
    menorQueUm = False
if(raiz<0):
    negativo = True
    raiz = abs(raiz)
if(not raiz%1 == 0):
    exponencial = True
if(numero < 0):
    if(numero>-1): min = -1
    else: min = numero
    max = 0
else:
    min = 0
    if(numero<1):max = 1
    else: max = numero
print("estimando...")
meio = (min+max)/2
meioAnterior = 0
if(numero == 0):
    meio = 0
resposta = meio
for i in range(raiz):
    if(i == 0): resposta = meio
    else: resposta = resposta*meio
while((float('%.10f'%(resposta)))!= numero and meio != meioAnterior):
    if(raiz == 0):
        meio = 1
        break
    if(raiz == 1):
        meio = numero
        break
    if(resposta>numero):
        max = meio
    elif(resposta<numero):
        min = meio
    meioAnterior = meio
    meio = (min+max)/2
    for i in range(raiz):
        if(i == 0): resposta = meio
        else: resposta = resposta*meio
    print(meio)

output = "a raiz " + str(raiz) + " de " + str(numero) + " é: "
    
if(imaginario):
    output = output + "i"
if(negativo):
    output = output+"1/"
output = output + str(float('%.10f'%(meio)))
print(output)
input()