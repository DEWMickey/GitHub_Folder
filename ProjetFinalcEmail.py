import smtplib, ssl
from email.mime.text import MIMEText
import keyboard



def info():
    print("""Atansyon!  Atansyon!
    Aplikasyon jere 2 kont pou kounya: Gmail epi Yahoo
    Pou itilize aplikasyon sa ak kont nou site la yo, gen 2 kondisyon ki dwe reyini:
    1- Ou dwe gen verifikasyon 2 fason an ki aktive sou kont lan
    2- Ou dwe gen yon modpas ke google jenere pou ou a pati de kont ou an (sa depann de nimewo 1 an)
    
    Pou verifye si 1 aktive oubyen pou aktivel, kopye lyen sa nan google ou: https://myaccount.google.com/signinoptions/two-step-verification
    Pou ka jenere modpas la li menm lew fin aktive verifye oubyen aktive 1 an, al sou lien sa nan google ou: https://myaccount.google.com/apppasswords
    Pou sekiritew nou pa save modpas yo ba ou a nan app la, toujou sonjel lew ap vin voye mail
    Si kondisyon sa yo ok pou deja peze bouton Esc sou klavye a pou ka komanse itilize app la ou k pou kitel\n""")
    while True:
        if keyboard.is_pressed("Esc"):
            break
        elif keyboard.is_pressed("k"):
            quit()


# Fonksyon kap jere Email pou Gmail
def gmail():
    global sender
    global password
    global recipient
    global body
    msg = MIMEText("")
    msg['Subject'] = input("Ekri sije ki dwe nan mail lan\n")
    print("""\nEkri ko mail la, lew fini ekril wap peze enter epi peze bouton F8 sou klavye a pou mail yo ka ale.\n
    Pa bliye:
    Siw bezwen 1 liy apre yon fraz wap peze bouton ki gen siy / yon fwa
    siw bezwen 2 liy apre yon fraz oubyen paragraf wap peze bouton ki gen siy / 2 fwa\n""")
    body = input("").replace("//", "\n\n").replace("/", "\n")
    while True:
        if keyboard.is_pressed("F8"):
            break
    msg['From'] = sender
    e = 0
    try:
        with open("EmailList.txt", "r") as fichye:
            done = fichye.read().split(",")
            while e < len(done) - 1:
                msg['To'] = done[e]
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL('smtp.googlemail.com', 465, context=context) as server:
                    server.login(sender, password)
                    server.sendmail(sender, done[e], f"{msg.as_string()}\n{body}")
                    print("Successfully sent email to: ", done[e])
                e += 1
    except smtplib.SMTPException:
        print("Error: unable to send email")


# Fonksyon kap jere Email pou yahoo
def yahoo():
    global sender
    global password
    global recipient
    global body
    msg = MIMEText("")
    msg['Subject'] = input("\nEkri sije ki dwe nan mail lan\n")
    print("""\nEkri sa ki ap nan ko mail la, lew fini ekril wap peze enter epi peze bouton F8 sou klavye a pou mail yo ka ale.
        Pa bliye:
        Siw bezwen 1 liy apre yon fraz wap peze bouton ki gen siy / yon fwa, epi wap kontinye ekri apre siy lan.
        siw bezwen 2 liy apre yon fraz oubyen paragraf wap peze bouton ki gen siy / 2 fwa epi wap kontinye ekri apre siy lan.\n""")
    body = input("").replace("//", "\n\n").replace("/", "\n")
    while True:
        if keyboard.is_pressed("F8"):
            break
    msg['From'] = sender
    e = 0
    try:
        with open("EmailList.txt", "r") as fichye:
            done = fichye.read().split(",")
            while e < len(done) - 1:
                msg['To'] = done[e]
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465, context=context) as mail:
                    mail.login(sender, password)
                    mail.sendmail(sender, done[e], f"{msg.as_string()}\n\n{body}")
                    print("Successfully sent email to: ", done[e])
                e += 1
    except smtplib.SMTPException:
        print("Error: unable to send email")


# Varyab ke nou kreye pou ko mail lan
body = ""


# Ko program nan
info()
sender = input("\nByenvini! Svp antre email ki ap voye mail bay lot moun nan ou moun yo !\n")
password = input("\nSvp antre modpas ke google jenere pou ou sou site li a\n")
recipient = input("\nAntre lis adres email moun ki dwe resevwa mail la, mete vigil apre ckak email, ou pa bezwen mete espas apre vigil la\n").split(",")
with open("EmailList.txt", "w") as F:
    for i in recipient:
        F.write(f"{i},")
    F.close()

confirm = input("\nSi email ki pral voye msg yo se gmail Tape g epi tape enter sou klavye a, si se yahoo tape y epi tape enter.\n")
while confirm not in ["g","y"]:
    confirm = input("\nRechwazi, chwa ou a dwe g oubyen y.\n")
else:
    if confirm == "g":
        gmail()
        print("g")
    elif confirm == "y":
        yahoo()
        print("y")


