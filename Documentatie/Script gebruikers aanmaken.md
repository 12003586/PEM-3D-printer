# Script gebruikers aanmaken [#30](https://github.com/12003586/PEM-3D-printer/issues/3) (EPIC)

Het doel is om een script te maken waarmee users worden aangemaakt op Octoprint zodat in de jobhistory bekeken kan worden wie welke print heeft opgezet.

## Octoprint API

Om dit script te schrijven hebben we de Octoprint API nodig. In de [API documentatie](https://docs.octoprint.org/en/master/api/index.html) zit een gedeelte om users toe te voegen, deze staat [hier](https://docs.octoprint.org/en/master/api/access.html#add-a-new-user).

Deze add user heb ik eerst getest gehad via Burp Suite. Ik heb de Burp Suite live task gebruikt en een gebruiker in Octoprint aangemaakt. Deze post heb ik opgevangen. Door deze op te vangen kan ik deze repeaten en aanpassen zoals op onderstaanden foto. 

![image](https://user-images.githubusercontent.com/56915229/197717837-eae960e3-e08e-46df-a6cd-3b641e2c6455.png)

Nu om deze te testen in een Python script waren er een aantal aanpassingen nodig. Eerst moest er een api-key aangemaakt worden omdat in BurpSuite een tijdelijke token werd gebruikt.

Deze heb ik hieronder aangemaakt.
![image](https://user-images.githubusercontent.com/56915229/205618198-82cc0535-2f79-4d14-b241-895749606ce8.png)

Omdat dit te groot is om in de eerste keer juist te hebben, heb ik dit opgedeeld in enkele kleine gedeeltes. Deze gedeeltes zal ik ook apart bespreken.

## Gebruikers-aanmaken [#39](https://github.com/12003586/PEM-3D-printer/issues/39)

## Gebruikers-aanmaken-command-test [#40](https://github.com/12003586/PEM-3D-printer/issues/40)

## Gebruikers-aanmaken-mail [#41](https://github.com/12003586/PEM-3D-printer/issues/41)

## Gebruikers-aanmaken-wachtwoord-genereren [#42](https://github.com/12003586/PEM-3D-printer/issues/42)

## Gebruikers-aanmaken-csv [#44](https://github.com/12003586/PEM-3D-printer/issues/44)

## Gebruikers-verwijderen [#45](https://github.com/12003586/PEM-3D-printer/issues/45)


## Auteurs
- **Martijn Guilliams** - _CONTRIBUTOR_ - [Martijn Guilliams](https://github.com/MartijnGuilliamsPXL)