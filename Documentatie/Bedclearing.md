# BedClearing

Een bedclearing script is nodig zodat er opeenvolgende prints kunnen worden geprint. De code maakt gebruik van de nozzle om de print van het bed te verwijderen.

## OctoPrint

De code moet worden uitgevoerd na iedere print en op het einde van de queue. In de plugin van continous print wordt deze code geplaatst.

![bedclearing octoprint](https://user-images.githubusercontent.com/79916496/200277744-76a09bcc-5003-4456-b4dc-ff604bb9cb7f.png)



## Gcode

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



