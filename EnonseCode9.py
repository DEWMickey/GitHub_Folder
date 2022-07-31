# Enonse #1
IP = "227.0.0.1"
s = 0
for i in IP:
    print(i)
    if i in ["0","1","2","3","4","5","6","7","8","9"]:
        s += int(i)
print(s*int(IP[0]))


# Enonse #2
n = int(input("Antre antye ou a : "))
if n // 4 == 0:
    print("OK")
else:
    print("NOK")

# Enonse #3
new_text = []
text = input("entrer le texte ").lower()
for i in text.split():
    new_text.append(i[0].upper() + i[1:])
print(" ".join(new_text))


# Enonse #4
def choice(numero):
    global lite_possible, Num_1, Num_2

    for i in range(1, 21):
        if numero == 1:
            if i % Num_1 == 0 and i % Num_2 != 0:
                lite_possible.append(i)
        if numero == 2:
            if i % Num_1 != 0 and i % Num_2 == 0:
                lite_possible.append(i)
        if numero == 3:
            if i % Num_1 == 0 and i % Num_2 == 0:
                lite_possible.append(i)
        if numero == 4:
            if i % Num_1 != 0 and i % Num_2 != 0:
                lite_possible.append(i)


lite_possible = []
Num_1 = 2
Num_2 = 3
numero = int(input("""liste [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
1- Multiple 2 not 3
2- Multiple 3 not 2
3- Multiple 2 and 3
4- Not Multiple 2 and 3
choose 1,2,3 or 4\n"""))
choice(numero)
print(lite_possible, f"--> Total {len(lite_possible)}")


# Enonse #5
a = "5 45 1283 12"

t = a.split()
s = 0
r = 1
k = 0
o = []
while k < len(t):
    for i in t[k]:
        s += int(i)
    k += 1
    s *= 1
    r = r*s
    s=0

print(r)


# Enonse #6
ReverseString = ""
Chaine = "   Ayibobo Ayiti   u"
print(Chaine.strip(" "))
for i in Chaine.replace(" ",""):
    ReverseString = i+ReverseString
print(ReverseString)


# Enonse #7
a = []
Chenn = "consequence miry lan di"
for i in Chenn:
    if i in ["a", "e", "i", "o", "u", "y"]:
        print(Chenn.index(i)-1)
        Chenn = Chenn.replace(Chenn[Chenn.index(i)-1],"*")
print(Chenn)


# Enonse #9
start, end = int(input("Antre komansmanse enteval nonb ou yo: ")), int(input("Antre nonb pou enteval la fini an: "))
Lp = []
for i in range(start, end+1):
    if i % 2 == 0:
        Lp.append(i)


# Enonse #11
Nonb = [12,3,5,799,87]
i = 0
for big in Nonb:
    if big > i:
        i = big
print(i)


# Enonse #12
a, b = int(input("Antre vale a : ")), int(input("Antre vale b: "))
somme = 0
if a > b:
    somme = (a + b) - a
    print(somme)
else:
    somme = (a + b) - b
    print(somme)


# Enonse #13
i = 1
c = 0
liste = [0, 1, 2, 3, 4]
while i < 5:
    c += -1
    if i == 1:
        liste = liste[c::-1]
        print(liste)
    else:
        d = -i+1
        liste = liste[c::-1] + liste[d:]
        print(liste)
    i += 1


# Enonse #14
a, b = int(input("Antre vale a : ")), int(input("Antre vale b: "))
print((b/a)/2)


# Enonse 16
import string


def decrypt(word):
    global a
    for i in word.split():
        if i[0] == ">":
            if i[2] in string.ascii_uppercase:
                a.append(string.ascii_uppercase.index(i[2]) + int(i[1]) + 1)

        elif i[0] == "<":
            if i[2] in string.ascii_uppercase:
                a.append(string.ascii_uppercase.index(i[2]) - int(i[1]) + 1)


def renvoiWord(a):
    global c
    for p in a:
        c = c + string.ascii_uppercase[p - 1]
    return c


word = ">7E >0A <1Q <6Z >2M >4L"
# appel fonction yo
decrypt(word)  # appel fonksyon an poul ka dekripte mo an
NewWord = renvoiWord(a)  # Varyab ki la pou resevwa nom dekripte a

# Blok code ki pou afiche nom kode a, alfabè yo epi nouveau nom an
print(f"\nLis alfabè yo se: {string.ascii_uppercase}")
print(f"\nKod la se: {word} \nPozisyon chak 3 karakte se {a}\nEpi mo ki kache a ladann nan se: {NewWord}")

