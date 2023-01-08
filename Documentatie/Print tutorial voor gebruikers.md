# Print tutorial voor gebruikers [#43](https://github.com/12003586/PEM-3D-printer/issues/43)

Dit is een tutorial voor studenten om van een 3d-bestand naar G-code te gaan en deze dan te uploaden op Octoprint.

## Stappenplan
1. Download en installeer [PrusaSlicer](https://www.prusa3d.com/page/prusaslicer_424/)
   Dit gebruiken we omdat deze de minste problemen of beter gezegd minste onhandigheden geeft.
   Andere slicers zouden ook werken maar raden we af zo lang dat er een Prusa printer in gebruik is.
2. Add printer
   Klik op "printer settings" en dan op "add/remove printers".
   Zoek dan de "Original Prusa i3 MK3S & MK3S+" op en selecteer deze met de standaard nozzle.
   (Dit is de printer die nu momenteel gebruikt wordt.)
3. Ga nu naar "print settings"
4. Klik rechtsboven op "Expert"
5. Zorg dat onderstaande settings hetzelfde zijn
![image](https://user-images.githubusercontent.com/56915229/211200942-9e6f816a-9c3c-461e-b551-300cb1800fd2.png)
Bij onderstaande foto: let vooral op de "Raft".
![image](https://user-images.githubusercontent.com/56915229/211201037-80521708-3e99-4716-af89-bc4cbd5e2c89.png)

6. Druk op opslaan, klik rechtsboven op "Simple" en ga dan naar "Plater"
7. Een STL-file openen
   Een 3d-bestand is vaak een STL-file, hier gaan we dus ook mee verder.
   Het openen kan door het bestand in Prusa te slepen.
8. (LET OP! zorg dat de print niet linksachter in de hoek staat)
   Een print staat standaard in het midden van het printbed.
   Voor hele grote prints raden we te strenge aan om deze naar rechts en naar voor op te schuiven.
   Dit is omdat de print wanneer het gedaan is automatisch er af gaat duwen. Maar omdat de printkop hetgeen is wat de print er van afduwt heeft de printkop linkachter de plaats nodig om terug naar beneden te gaan.
9. Klik nu rechtsonder op "Slice".
   Dit ziet er zo uit. De geschatte printtijd is hier ook zichtbaar.
![image](https://user-images.githubusercontent.com/56915229/211201722-053be4eb-66cb-4d7c-845c-c5fba849ed73.png)
10. Druk rechtsonder op "Export G-code".
    Sla dit bestand ergens tijdelijk op.
11. Ga nu in een browser naar [Octoprint](http://octopi.pxl-ea-ict.be:24081/).
12. Login met de gebruikersnaam en wachtwoord dat u gekregen heeft.
13. Upload het G-code bestand. Deze komt dan automatisch in de queue.
14. Hopen dat de print lukt.

## Auteurs
- **Martijn Guilliams** - _CONTRIBUTOR_ - [Martijn Guilliams](https://github.com/MartijnGuilliamsPXL)
