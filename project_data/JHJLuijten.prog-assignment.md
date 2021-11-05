# Toets PHP

**Datum:** 20 april 2017

**Toegstaan:** Internet, Codecademy, W3schools, Eigen aantekeningen en/of oefenbestanden

**Niet toegestaan:** Hulp vragen van klasgenoten!

**Tijdsduur:** 08:30 - 15:00

Je mag gebruik maken van het framework ‘github.com/davinci-ao/framework-php’.
De SQL om de database aan te maken en te vullen is erbij gegeven, net zoals de layout van de pagina’s.
Blijf niet te lang hangen als iets niet werkt, ga dan verder met andere pagina’s.

Maak van al je bestanden een zip file en lever deze in via It’s Learning.

Het is niet toegestaan, nadat je het framework hebt gekopieerd, nog te werken met sourcetree of github.

## index pagina
* Maak een overzicht van alle schrijvers (zie voorbeeld index.html)
* Zorg dat achter elke schrijver via de link ‘show’ je doorgestuurd wordt naar de show pagina

## show pagina
*	Maak een overzicht van alle boeken bij een bepaalde schrijver (zie voorbeeld, books.html)
*	Zorg ervoor dat als je van de index ‘home’ pagina kom via de link ‘show’, alleen de boeken van de gekozen schrijver worden getoond
*	Zorg dat je een boek kan toevoegen, door op de ‘add book’ link te klikken
*	Zorg ervoor dat je een book kan deleten door op de ‘delete’ link te klikken (automatisch doorsturen naar de index ‘home’ pagina)
*	Zorg ervoor dat je een book kan editten door op de ‘edit’ link te klikken (automatisch doorsturen naar de index ‘home’ pagina)

## edit pagina
* Zorg ervoor dat je alle gegevens hier kan aanpassen
*	Zorg ervoor dat je na de submit keuze automatisch wordt doorgestuurd naar de index ‘home’ pagina
*	**Extra**, zorg ervoor dat je na de submit automatisch wordt doorgestuurd naar het overzicht van de boeken behorende bij de zojuist aangepaste schrijver. Bijv. Ik sta op het overzicht van Stephen King en kies ervoor om het book ‘It’ aan te passen. Na het aanpassen wordt ik dan automatisch doorgestuurd naar het overzocht van boeken van Stephen King. (daar kwam ik vandaan)
* **Extra**, zorg ervoor dat bij de Author i.p.v. het id zijn juiste naam staat. Dat je hier d.m.v. een dropdown ok kan kiezen voor een andere author

## add pagina
*	Zorg ervoor dat je hier een boek kan toevoegen. (zie voorbeeld add.html)
*	Bij author id vul je het desbetreffende id in van die author
*	Zorg dat je nadat een boek is toegevoegd automatisch wordt doorgestuurd naar de index ‘home’ pagina
*	**Extra**, zorg ervoor dat je na de submit automatisch wordt doorgestuurd naar het overzicht van de boeken van het zojuist aangemaakte boek, van die schrijver
*	**Extra**, zorg ervoor dat je d.m.v. een dropdown menu een author kan kiezen
*	**Extra**, zorg ervoor dat deze dropdown info uit de database komt

## delete pagina
*	Zorg dat een boek verwijderd wordt uit de database, nadat ik op de ‘delete’ link heb geklikt.
*	**Extra**, zorg ervoor dat ik na de delete automatisch wordt doorgestuurd naar het overzicht van de boeken behorende bij de schrijver van het zojuist verwijderde boek.

## voeg boeken toe
Voeg de twee volgende boeken toe.

kolom | omschrijving
--- | ---
name | Emily Barr id = 4
title | Klasgenoten
publisher | Uitgeverij Maarten
summary	| Susie, een succesvolle kunstenares die met haar geliefde in Zuid-Frankrijk woont, besluit in een opwelling een reünie te organiseren. Ze nodigt haar vier beste schoolvriendinnen uit om ze te imponeren met haar mooie huis, haar lekker foute vriend en haar zonnige bestaan. Tenminste, dat maakt ze zichzelf wijs. 

kolom | omschrijving
--- | ---
name | Tom Clancy  id = 5
title | Ongelijke Strijd
publisher | Zwarte Beertjes
summary | Jack Ryan, historicus, ex-marinier en CIA-medewerker, kijkt tijdens zijn vakantie in Londen binnen een half uur de dood twee keer recht in de ogen. De eerste keer wordt hij op een haar na door een dubbeldekker overreden wanneer hij bij het oversteken de verkeerde kant op kijkt. 

