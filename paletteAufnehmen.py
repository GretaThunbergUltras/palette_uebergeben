''' Code für das Fahrzeug ohne die Palette

    Der Code für das Fahrzeug dass anfangs keine Palette trägt und erst einmal auf
    eine Nachricht des ersten Fahrzeugs wartet. Nachdem es die Nachricht empfangen
    hat fährt es an die Palette heran, nimmt diese auf, dreht sich um und fährt weg.

'''

#TODO Methode zum scannen nach entgegenkommenden Fahrzeugen importieren (Botlib oder paletteAblegen.py)
#TODO testen ob Fahrzeuge mit Palette auch erkannt werden


def entgegenkommendesFahrzeugMitPaletteErkannt():
    #TODO testen der Funktion
    wartenAufNachrichtVonErstemFahrzeug()
    paletteAnfahren()
    paletteAufheben()
    #TODO Methode zum umdrehen importieren (Botlib oder paletteAblegen.py)
    pass

def wartenAufNachrichtVonErstemFahrzeug():
    #TODO realisieren der kompletten Funktion
    #Nachfrage möglich bei: Mercedes, Kris
    pass

def paletteAnfahren():
    #TODO realisieren der kompletten Funktion
    pass

def paletteAufheben():
    #TODO realisieren der kompletten Funktion, oder einbinden von der Botlib
    pass