# AutoQueue

## Continous Print
Om een bestand in de Conitnous print queue te plaatsen moeten deze stappen gevolgd worden.

- Stap 1
    Ga naar het tabblad van conitnous print </br>
    
![coninousprint_1](https://user-images.githubusercontent.com/79916496/204254929-894f9e62-b42e-48f3-9f69-99bfa25101eb.png)

- Stap 2
    Voeg het bestand toe aan octoprint </br>
  
![CP_2](https://user-images.githubusercontent.com/79916496/204254951-110330ed-7464-41f5-b93e-ebd371acc106.png)

- Stap 3
    Voeg het bestand dat geprint moet worden toe aan de queue </br>
    
![CP_3](https://user-images.githubusercontent.com/79916496/204254970-593132c3-80a6-4a70-9623-f610bbc4099d.png)

- Stap 4
    Geef de job een naam en save de job </br>
    
![CP_4](https://user-images.githubusercontent.com/79916496/204255006-3827da1c-3aea-4eb6-b9c6-c742dc7404e6.png)

Het bestand staat nu in de queue en zal geprint worden als de voorgaande jobs geprint zijn.

## BedClearing

Een bedclearing script is nodig zodat er opeenvolgende prints kunnen worden geprint. De code maakt gebruik van de nozzle om de print van het bed te verwijderen.

### OctoPrint

De code moet worden uitgevoerd na iedere print en op het einde van de queue. In de plugin van continous print wordt deze code geplaatst.

![bedclearing octoprint](https://user-images.githubusercontent.com/79916496/200277744-76a09bcc-5003-4456-b4dc-ff604bb9cb7f.png)



### Gcode

De code is [hier](https://github.com/12003586/PEM-3D-printer/blob/main/Code/BedClearing/Print%20Removal%20Code%20Prusa%20mk3.gcode) terug te vinden.

|Code                       |  Uitleg                                                |
|---------------------------|--------------------------------------------------------|
| G1 Z 210 F3000 ;          | Nozzle gaat omhoog                                     |
| G1 X0 Y200 Z 210 F3000 ;  | Nozzle gaat naar linkerzijkant en bed gaat naar achter |
| G1 X0 Y200 Z 80 F3000 ;   | Nozzle gaat omlaag                                     |
| G1 X0 Y000 Z 80 F3000 ;   | Bed gaat naar voor                                     |
| G1 X0 Y200 Z 80 F3000 ;   | Bed gaat naar achter                                   |
| G1 X0 Y200 Z 1 F3000 ;    | Nozzle gaat omlaag                                     |
| G1 X44 F3000;             | Beweegt op x-as voor eerste sweep                      |
| G1 X45 F3000;             | Bed beweegt naar voren voor eerste sweep               |
| G1 Z50 F3000;             | Nozzle gaat omhoog                                     |
| G1 Y200 F3000;            | Bed gaat naar achter                                   |
| G1 Z1 F3000;              | Nozzle gaat omlaag                                     |
| G1 X116 F3000;            | Beweegt op x-as voor tweede sweep                      |
| G1 Y45 F3000;             | Bed beweegt naar voren voor tweede sweep               |
| G1 Z50 F3000;             | Nozzle gaat omhoog                                     |
| G1 Y200 F3000;            | Bed gaat naar achter                                   |
| G1 Z1 F3000;              | Nozzle gaat omlaag                                     |
| G1 X209 F3000;            | Beweegt op x-as voor derde sweep                       |
| G1 Y45 F3000;             | Bed beweegt naar voren voor derde sweep                |
| G1 Z50 F3000;             | Nozzle beweegt omhoog                                  |
| G1 Y200 F3000;            | Bed beweegt naar achter                                |
| G1 Z1 F3000;              | Nozzle gaat omlaag                                     |

## Auteurs
- **[Bo Mengels](https://github.com/12003586)** - _CONTRIBUTOR_ - 



