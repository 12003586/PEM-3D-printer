# Firmware updaten [#28](https://github.com/12003586/PEM-3D-printer/issues/28)

 Deze [handleiding](https://blog.svenadolph.net/update-prusa-i3-m-k3-s-firmware-from-octo-pi-using-the-octo-print-firmware-updater-plugin/) heb ik gevolgd om de firmware te updaten en ervoor te zorgen dat dit van op afstand mogelijk is.

 ## Installatie stappen

1. Installeer de FirmwareUpdater Plugin. (octopi.local > Settings > Pluginmanager > zoek naar [FirmwareUpdater](https://github.com/OctoPrint/OctoPrint-FirmwareUpdater) > installeer plugin)
2. Installeer avrdude op de RaspberryPi, dit is nodig om te Flashen. Verbind met SSH en voer dit uit: avrdude sudo apt install avrdude. 
3. Ga naar de plugin settings en stel dit in:

Flash method: avrdude (Atmel AVR Family)


AVR MCU: ATmega2560


Path to avrdude: /usr/bin/avrdude 


AVR Programmer Type: wiring



## Update stappen

1. Download de juiste [Firmware](https://help.prusa3d.com/downloads).
2. Ga naar de plugin en selecteer daar het hex-bestand.
3. Druk op Flash.
4. Wacht tot de update gedaan is.


## Auteur
- **[Martijn Guilliams](https://github.com/MartijnGuilliamsPXL)** - _CONTRIBUTOR_ - 
