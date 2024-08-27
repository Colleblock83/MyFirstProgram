print("Willkommen zum Gehaltsrechner!")
print("Notiz: Der Rechner rechnet mit 31 Tagen im Monat")
arbeitsstunden = int(input("Bitte gebe deine Arbeitszeit in vollen Stunden an"))
stundenlohn = int(input("Bitte gebe nun deinen Stundenlohn ein"))

tageslohn = stundenlohn * arbeitsstunden
wochenlohn = tageslohn * 7
monatslohn = wochenlohn * 4 + 3 * tageslohn


print("Dein Monatslohn beträgt rund " + str(monatslohn) + "€.")
print("")
print("")
print("")

feed_back = int(input("Kannst du mir ein kleines Feedback geben? 1 = Sehr gut/Gut, 3 = Verbesserungsfährig 6 = Ganz schlecht"))

if feed_back == 1:
    print("Danke schön für das liebe Feedback, habe noch einen schönen Tag.")
elif feed_back == 3:
    print("Danke sehr für das Feedback, habe einen schönen Tag.")
elif feed_back == 6:
    print("Oh das tut mir leid, schreibe mir gerne Verbesserungsvorschläge in mein GitHub. Schönen Tag dir!")
else:
    print("Tut mir leid, ich verstehe nur die Zahlen 1, 3 und 6")


print("Danke für das nutzen meines ersten eigenen Programms!")
input("Drücke nun eine Taste um das Programm zu beenden...")











