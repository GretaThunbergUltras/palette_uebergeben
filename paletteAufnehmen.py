''' Code für das Fahrzeug ohne die Palette

    Der Code für das Fahrzeug dass anfangs keine Palette trägt und erst einmal auf
    eine Nachricht des ersten Fahrzeugs wartet. Nachdem es die Nachricht empfangen
    hat fährt es an die Palette heran, nimmt diese auf, dreht sich um und fährt weg.

'''

from botlib.bot import Bot
import time
from paletteAblegen import umdrehen, scanNachEntgegenkommendemFahrzeug, initialisiereRoboter

bot = None
    

def entgegenkommendesFahrzeugMitPaletteErkannt():
    '''
    Routine die ausgeführt werden sollte, wenn ein entgegenkommendes Fahrzeug mit Palette erkannt wurde:
    - Wartet auf Nachricht des ersten Fahrzeugs
    - Nimmt Palette auf
    - Dreht um
    '''
    #TODO testen der Funktion
    #TODO scanNachEntgegenkommendemFahrzeug abändern dass es Fahrzeuge mit Paletten erkennt.
    wartenAufNachrichtVonErstemFahrzeug()
    paletteAnfahren()
    paletteAufheben()
    umdrehen()
    pass


def wartenAufNachrichtVonErstemFahrzeug():
    '''
    Subsribes einen bestimmten Channel auf dem das erste Fahrzeug seine Nachricht sendet wenn es fertig ist.
    Wartet so lange, bis es die Nachricht erhält.
    Funktioniert mit MQTT
    '''
    #TODO realisieren der kompletten Funktion
    #Nachfrage möglich bei: Mercedes, Kris
    pass

def paletteAnfahren():
    '''
    Erkennt die Palette und fährt so an sie heran, dass man nur noch eine bestimmte Zeit geradeaus fahren muss,
    damit die Gabel unter die Palette fährt.
    '''
    #TODO realisieren der kompletten Funktion
    pass

def paletteAufheben():
    '''
    Hebt eine Palette, die auf dem Boden steht, autonom auf.
    Nimmt an, dass das Fahrzeug kurz vor der Palette steht.
    '''
    bot._forklift.to_pickup_mode()
    time.sleep(2)
    bot.drive_steer(0)
    bot.drive_power(30)
    time.sleep(1)
    bot.drive_power(0)
    bot._forklift.to_carry_mode()
    
def main():
    initialisiereRoboter()
    time.sleep(3)
    paletteAufheben()

if __name__ == "__main__":
    main()