from Projeto import converterStringParaFloat, bitParaByte, byteParaBit, ByteParaKilobyte, KilobyteparaByte, KilobyteparaMegabyte, MegabytesparaKilobyte, MegabyteparaGigabyte, GigabyteparaMegabyte, GigabyteparaTerabyte, TerabyteparaGigabyte, TerabyteparaPetabyte, PetabyteparaTerabyte

print('Escreva 1 para bitParaByte \n -Escreva 2 para byteParaBit \n -Escreva 3 para ByteParaKilobyte \n -Escreva 4 para KilobyteparaByte \n -Escreva 5 para KilobyteparaMegabyte \n -Escreva 6 para  MegabytesparaKilobyte \n -Escreva 7 para MegabyteparaGigabyte \n -Escreva 8 para GigabyteparaMegabyte \n -Escreva 9 para GigabyteparaTerabyte \n -Escreva 10 para TerabyteparaGigabyte \n -Escreva 11 para TerabyteparaPetabyte \n -Escreva 12 para PetabyteparaTerabyte   ')
funcEscolha = input()
if(funcEscolha == 1):
   entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
   valorConvertido = bitParaByte (entradaDoTecladoValorASerConvertido)
   print(valorConvertido)

if(funcEscolha == 2):
   entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
   valorConvertido = byteParaBit (entradaDoTecladoValorASerConvertido)
   print(valorConvertido)

if(funcEscolha == 3):
   entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
   valorConvertido = ByteParaKilobyte (entradaDoTecladoValorASerConvertido)
   print(valorConvertido)

if(funcEscolha == 4):
   entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
   valorConvertido = KilobyteparaByte (entradaDoTecladoValorASerConvertido)
   print(valorConvertido)

if(funcEscolha == 5):
   entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
   valorConvertido = KilobyteparaMegabyte (entradaDoTecladoValorASerConvertido)
   print(valorConvertido)

if(funcEscolha == 6):
   entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
   valorConvertido = MegabytesparaKilobyte (entradaDoTecladoValorASerConvertido)
   print(valorConvertido)

if(funcEscolha == 7):
   entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
   valorConvertido = MegabyteparaGigabyte (entradaDoTecladoValorASerConvertido)
   print(valorConvertido)

if(funcEscolha == 8):
   entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
   valorConvertido = GigabyteparaMegabyte (entradaDoTecladoValorASerConvertido)
   print(valorConvertido)

if(funcEscolha == 9):
   entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
   valorConvertido = GigabyteparaTerabyte (entradaDoTecladoValorASerConvertido)
   print(valorConvertido)

if(funcEscolha == 10):
   entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
   valorConvertido = TerabyteparaGigabyte (entradaDoTecladoValorASerConvertido)
   print(valorConvertido)

if(funcEscolha == 11):
   entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
   valorConvertido = TerabyteparaPetabyte (entradaDoTecladoValorASerConvertido)
   print(valorConvertido)

if(funcEscolha == 12):
   entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
   valorConvertido = PetabyteparaTerabyte (entradaDoTecladoValorASerConvertido)
   print(valorConvertido)