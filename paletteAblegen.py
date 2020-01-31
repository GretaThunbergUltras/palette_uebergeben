''' Code für das Fahrzeug mit der Palette

    Der Code für das Fahrzeug dass anfangs die Palette trägt, das zweite, entgegenkommende
    Fahrzeug erkennt. Dann die Palette abstellt, sich umdreht, wegfährt und das zweite
    Fahrzeug informiert, dass es loslegen kann.

'''

from botlib.bot import Bot
import time

bot = None
    

def initialisiereRoboter():
    '''
    Kreiert und Konfiguriert eine Bot() Instanz, so dass die angeschlossenen Geräte einfach
    angesprochen werden können.
    '''
    global bot
    bot = Bot()
    bot.calibrate()

def scanNachEntgegenkommendemFahrzeug():
    '''
    Schaut ob ein anderes Fahrzeug entgegenkommt.

    Returns:
    True    -   Falls ein anderes Fahrzeug erkannt wurde.
    False   -   Falls kein anderes Fahrzeug erkannt wurde.
    '''
    #TODO realisieren der kompletten Funktion.
    #TODO testen ob Fahrzeuge mit Palette auch erkannt werden
    pass

def entgegenkommendesFahrzeugOhnePaletteErkannt():
    '''
    Routine die ausgeführt werden sollte, wenn ein entgegenkommendes Fahrzeug ohne Palette erkannt wurde:
    - Setzt Palette ab
    - Dreht um
    - Benachrichtigt das zweite Fahrzeug
    '''
    #TODO testen der Funktion
    paletteAbsetzen()
    umdrehen()
    nachrichtAnFahrzeugZwei()
    pass


def paletteAbsetzen():
    '''
    Roboter setzt seine Palette auf der stelle ab und fährt so weit nach hinten,
    dass seine Gabel frei ist.
    Funktion ist NICHT kollisionsfrei.
    '''
    bot._forklift.to_pickup_mode()
    time.sleep(3)
    bot.drive_steer(0)
    bot.drive_power(-30)
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

def nachrichtAnFahrzeugZwei():
    '''
    Publishes auf einem bestimmten Channel eine Nachricht, die dem zweiten Fahrzeug signalisiert,
    dass Fahrzeug 1 fertig ist und Fahrzeug 2 anfangen kann.
    Funktioniert mit MQTT
    '''
    #TODO realisieren der kompletten Funktion
    bot.setup_broker()
    bot._broker.send_message("absetzchannel", "abgesetzt")

def main():
    initialisiereRoboter()
    time.sleep(3)
    paletteAbsetzen()
    umdrehen()

if __name__ == "__main__":
    main()