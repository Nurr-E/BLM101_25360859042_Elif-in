from config import KONU_ADI, TAM_AD, ÖĞRENCİ_NO, EMAIL

# Mantık kapıları

def AND(a, b):
    return a & b

def OR(a, b):
    return a | b

def NOT(a):
    return 1 - a

def XOR(a, b):
    return a ^ b


print(f"\nKONU ADI: {KONU_ADI}\nÖĞRENCİ: {TAM_AD}\nÖĞRENCİ NO: {ÖĞRENCİ_NO}\n")
print("Sanal Mantık Devresi Simülatörüne Hoş Geldiniz\n")

# A ve B için while ile kontrol
while True:
    try:
        a = int(input("A değerini giriniz (0 veya 1): "))
        b = int(input("B değerini giriniz (0 veya 1): "))
        if a in [0, 1] and b in [0, 1]:
            break
        else:
            print("Geçerli bir ifade girin!")
    except ValueError:
        print("Geçerli bir ifade girin!")

print("\nKullanılacak mantık kapısını seçiniz:")
print("1 - AND")
print("2 - OR")
print("3 - XOR")

# Seçim için while ile kontrol
while True:
    try:
        secim = int(input("Seçiminiz: "))
        if secim in [1, 2, 3]:
            break
        else:
            print("Geçerli bir ifade girin!")
    except ValueError:
        print("Geçerli bir ifade girin!")

if secim == 1:
    print("Sonuç (A AND B):", AND(a, b))

elif secim == 2:
    print("Sonuç (A OR B):", OR(a, b))

elif secim == 3:
    print("Sonuç (A XOR B):", XOR(a, b))


# Doğruluk tablosu
print("\nA AND (B OR C) ifadesinin doğruluk tablosu")
print("A B C | Sonuç")
print("----------------")

for A in [0, 1]:
    for B in [0, 1]:
        for C in [0, 1]:
            print(A, B, C, "|", A & (B | C))

