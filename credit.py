def main():
  cardNumber = input("Insira o número do cartão de crédito: ")

  if validateCard(cardNumber):
    brand = getBrand(cardNumber)
    print(brand)
  else:
    print("INVÁLIDO")

def validateCard(card):
  total = 0

  for i in range(len(card) - 2, -1, -2):
    timesTwo = int(card[i]) * 2
    if timesTwo > 9:
      total += timesTwo - 9
    else:
      total += timesTwo

  for i in range(len(card) - 1, -1, -2):
    total += int(card[i])

  if total % 10 == 0:
    return True
  
  return False

def getBrand(card):
  if (len(card) == 13 or len(card) == 16) and card[0] == '4':
    return 'VISA'

  if len(card) == 16 and card[0:2] in ['51', '52', '53', '54', '55']:
      return 'MASTERCARD'

  if len(card) == 15 and card[0:2] in ['34', '37']:
      return 'AMEX'

  return 'OUTRA BANDEIRA'

main()
