# Raspberry Pi met 3d-printer verbinden [#3](https://github.com/12003586/PEM-3D-printer/issues/3)

## Onderzoek [#6](https://github.com/12003586/PEM-3D-printer/issues/6)
Op de [website](https://www.prusa3d.com/#_ga=2.234599902.1193074351.1663597125-2091642634.1663597125) van de Prusa 3d-printers staat een voorbeeld project hoe Octoprint kan geconfigureerd en geïnstalleerd worden op een Raspberry Pi zodat dit met 3d-printers werkt. 

[Octoprint - Configuration and install](https://help.prusa3d.com/article/octoprint-configuration-and-install_2182)

## Testing [#7](https://github.com/12003586/PEM-3D-printer/issues/7)
Na het volgen van de stappen op deze website [Octoprint - Configuration and install](https://help.prusa3d.com/article/octoprint-configuration-and-install_2182) om OctoPrint te installeren op de Raspberry PI kan de RPI aangezet worden. Deze start dan op en kan via http://raspberrypi.local of via het ip-adres mee verbonden worden. Wanneer de verbinding gelukt is moet er ingelogd worden. De login is: username: Eclair4837, password: ZBwFARHJ9oD@8Tk4 .

De SSH login => username: OctoPi , password: XEMRYTPGgbk79W

Dan wordt onderstaand scherm getoond. Links boven op de foto staat dat er nog geen verbinding is met de 3d-printer. Zorg ervoor dat de usb printerkabel in de usb poort van RPI en printer aasluiting van de 3d-printer steekt. Hierna kan er op connect gedrukt worden. </Br>
![image](https://user-images.githubusercontent.com/56915229/192243268-a17fac71-4925-4771-aa13-894883801602.png)
</Br>


# Raspberry Pi booten met ssd

## Stappen

1. Launch Raspberry Pi imager tool en kies Choose OS. Voor een OS image dat gedownload is in de lokale bestanden, selecteer Custom en selecteer .img OS van het systeem.
2. Klik op Choose Storage en selecteer de geconnecteerde USB storage media. klik op Write
3. Nadat de OS is geflashed op de USB boot media, dismount/eject de media en daarna de drive van het systeem disconnecten
4. Verbind de USB drive met de Raspberry Pi 4
5. Power on de Raspberry Pi, deze zal dan zoeken naar de bootable USB media en daarna het systeem booten vanuit de geconnecteerde USB drive 

## Auteur
- **[Martijn Guilliams](https://github.com/MartijnGuilliamsPXL)** - _CONTRIBUTOR_ - 
- **[Bo Mengels](https://github.com/12003586)** - _CONTRIBUTOR_ - 
