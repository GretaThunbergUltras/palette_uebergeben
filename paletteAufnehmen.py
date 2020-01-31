''' Code für das Fahrzeug ohne die Palette

    Der Code für das Fahrzeug dass anfangs keine Palette trägt und erst einmal auf
    eine Nachricht des ersten Fahrzeugs wartet. Nachdem es die Nachricht empfangen
    hat fährt es an die Palette heran, nimmt diese auf, dreht sich um und fährt weg.

'''

from botlib.bot import Bot
import time
from paletteAblegen import scanNachEntgegenkommendemFahrzeug

bot = None
    

def initialisiereRoboter():
    '''
    Kreiert und Konfiguriert eine Bot() Instanz, so dass die angeschlossenen Geräte einfach
    angesprochen werden können.
    '''
    global bot
    bot = Bot()
    bot.calibrate()

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
    #TODO aufrufen unseres Verhaltens, in: on_Message()
    bot.setup_broker(subscriptions={'channelGruppe12': 'on_Message'})

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

def umdrehen():
    '''
    Roboter macht eine Dreipunktwende nach rechts hinten.
    Funktion ist NICHT kollisionsfrei.
    Basiert darauf dass alle Motoren zum Fahren unter allen Situationen gleich schnell laufen und
    einen gleichen gleichen Wendekreis haben.
    '''
    bot.drive_steer(1)
    time.sleep(1)
    bot.drive_power(-30)
    time.sleep(3.52)
    bot.drive_power(0)
    time.sleep(1)
    bot.drive_steer(0)
    time.sleep(1)
    bot.drive_steer(-1)
    bot.drive_power(30)
    time.sleep(3.52)
    bot.drive_power(0)
    bot.drive_steer(0)
    time.sleep(1)
    bot.drive_power(20)
    time.sleep(1)
    bot.drive_power(0)
    
def main():
    initialisiereRoboter()
    time.sleep(3)
    paletteAufheben()

if __name__ == "__main__":
    main()