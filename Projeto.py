Padrão =1024

def converterStringParaFloat(value):
    print('Valor convertido de str para float')
    return float(value)

def bitParaByte(valorASerConvertido):
    print('Valor convertido de bit para byte')
    bytesCalculado = valorASerConvertido / 8
    return bytesCalculado

def byteParaBit(valorASerConvertido):
    print('Valor convertido de byte para bit')
    bitsCalculado = valorASerConvertido * 8
    return bitsCalculado

def ByteParaKilobyte(valorASerConvertido):
    print('Valor convertido de byte para kilobyte')
    KilobyteCalculado = valorASerConvertido / Padrão
    return KilobyteCalculado

def KilobyteparaByte(valorASerConvertido):
    print('Valor convertido de kilobyte para bytes')
    ByteCalculado = valorASerConvertido * Padrão
    return ByteCalculado

def KilobyteparaMegabyte(valorASerConvertido):
    print('Valor convertido de Kilobyte para Megabyte')
    MegabyteCalculado = valorASerConvertido / Padrão
    return MegabyteCalculado

def MegabytesparaKilobyte(valorASerConvertido):
    print('Valor convertido de Megabyte para Kilobytes')
    bitsCalculado = valorASerConvertido * Padrão
    return bitsCalculado

def MegabyteparaGigabyte(valorASerConvertido):
    print('Valor convertido de Megabyte para Gigabyte')
    GigabyteCalculado = valorASerConvertido / Padrão
    return GigabyteCalculado

def GigabyteparaMegabyte(valorASerConvertido):
    print('Valor convertido de Gigabyte para Megabytes')
    MegabyteCalculado = valorASerConvertido * Padrão
    return MegabyteCalculado

def GigabyteparaTerabyte(valorASerConvertido):
    print('Valor convertido de Gigabyte para Terabyte')
    TerabyteCalculado = valorASerConvertido / Padrão
    return TerabyteCalculado

def TerabyteparaGigabyte(valorASerConvertido):
    print('Valor convertido de Teragabyte para Gigabytes')
    GigabyteCalculado = valorASerConvertido * Padrão
    return GigabyteCalculado

def TerabyteparaPetabyte(valorASerConvertido):
    print('Valor convertido de Terabyte para Petabyte')
    PetaCalculado = valorASerConvertido / Padrão
    return PetaCalculado

def PetabyteparaTerabyte(valorASerConvertido):
    print('Valor convertido de Petabyte para Terabytes')
    TerabyteCalculado = valorASerConvertido * Padrão
    return TerabyteCalculado

print('Insira o valor a ser convertido')
ValorInicial = converterStringParaFloat(input())
valorConvertido = PetabyteparaTerabyte(ValorInicial)
print(valorConvertido)