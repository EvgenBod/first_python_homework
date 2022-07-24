per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму, которую хотите положить под проценты:"))
TKB_bank = int((per_cent['ТКБ']) * (money/100))
SKB_bank = int((per_cent['СКБ']) * (money/100))
VTB_bank = int((per_cent['ВТБ']) * (money/100))
SBER_bank = int((per_cent['СБЕР']) * (money/100))
deposit = [TKB_bank, SKB_bank, VTB_bank, SBER_bank]
print("Накопленные средства за год =",deposit)
print("Максимальная сумма, которую сможете заработать:", max(deposit))