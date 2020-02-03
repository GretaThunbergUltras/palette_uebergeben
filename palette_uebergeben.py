from botlib.bot import Bot
import time

bot = None
traegtPalette = False
nachrichtErhalten = False

def initialisiereRoboter():
    '''
    Kreiert und Konfiguriert eine Bot() Instanz, so dass die angeschlossenen Geräte einfach
    angesprochen werden können.
    '''
    global bot
    bot = Bot()
    bot.calibrate()

def paletteAbsetzen():
    '''
    Roboter setzt seine Palette auf der stelle ab und fährt so weit nach hinten,
    dass seine Gabel frei ist.
    Funktion ist NICHT kollisionsfrei.
    '''
    global traegtPalette
    bot._forklift.to_pickup_mode()
    time.sleep(3)
    bot.drive_steer(0)
    bot.drive_power(-30)
    time.sleep(1)
    bot.drive_power(0)
    traegtPalette = False
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
    Publishes auf dem Channel "channelGruppe12" eine Nachricht, die dem zweiten Fahrzeug signalisiert,
    dass Fahrzeug 1 fertig ist und Fahrzeug 2 anfangen kann.
    Funktioniert mit MQTT
    '''
    #TODO Testen
    bot.setup_broker()
    bot._broker.send_message("channelGruppe12", "abgesetzt")

def paletteUebergeben:
    '''
    Routine die ausgeführt wird, wenn ein anderes Fahrzeug erkannt wurde und eine
    Palette getragen wird.
    - Setzt Palette ab
    - Dreht um
    - Benachrichtigt das zweite Fahrzeug
    '''
    paletteAbsetzen()
    umdrehen()
    nachrichtAnFahrzeugZwei()




def onMessage(client_id, userdata, message):
    nachricht = str(message.payload)
    if "abgesetzt" in nachricht:
        nachrichtErhalten = True

def hörenAufNachrichtVonErstemFahrzeug():
    '''
    Subsribes einen bestimmten Channel auf dem das erste Fahrzeug seine Nachricht sendet wenn es fertig ist.
    Wartet so lange, bis es die Nachricht erhält.
    Funktioniert mit MQTT
    '''
    bot.setup_broker(subscriptions={'channelGruppe12': 'on_Message'})

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

def paletteEntgegennehmen():
    paletteAufheben()
    umdrehen()

def main():
    initialisiereRoboter()
    while True:
        if True: #TODO Hier sollte ein anderes Fahrzeug erkannt werden.
            if traegtPalette:
                paletteUebergeben()
            else:
                hörenAufNachichtVonErstemFahrzeug()
                while not nachrichtErhalten:
                    time.sleep(1)
                paletteEntgegennehmen()
        else:
            followLine #TODO tu dies

if __name__ == "__main__":
    main()