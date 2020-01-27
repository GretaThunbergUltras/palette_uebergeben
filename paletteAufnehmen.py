''' Code für das Fahrzeug ohne die Palette

    Der Code für das Fahrzeug dass anfangs keine Palette trägt und erst einmal auf
    eine Nachricht des ersten Fahrzeugs wartet. Nachdem es die Nachricht empfangen
    hat fährt es an die Palette heran, nimmt diese auf, dreht sich um und fährt weg.

'''

#TODO Methode zum scannen nach entgegenkommenden Fahrzeugen importieren (Botlib oder paletteAblegen.py)
#TODO testen ob Fahrzeuge mit Palette auch erkannt werden
from botlib.bot import Bot
import time

bot = None
    
def initialisiereRoboter():
    global bot
    bot = Bot()
    bot.calibrate()

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
    bot._forklift.to_pickup_mode()
    time.sleep(2)
    bot.drive_steer(0)
    bot.drive_power(30)
    time.sleep(1)
    bot.drive_power(0)
    bot._forklift.to_carry_mode()
    
def test():
    initialisiereRoboter()
    time.sleep(3)
    paletteAufheben()
test()