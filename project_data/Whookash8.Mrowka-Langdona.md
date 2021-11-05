# Mrowka-Langdona

Mrówka Langtona – prosty automat komórkowy wymyślony i opisany przez Chrisa Langtona w 1986 roku[1]. Może być traktowany również jako rozszerzona do dwóch wymiarów bardzo prosta maszyna Turinga.

W każdym kroku wyróżniona jest jedna komórka nazywana "mrówką", która oprócz koloru ma określony także kierunek, w którym się porusza. Mrówka zachowuje się według następujących zasad:

jeśli znajduje się na polu białym to obraca się w lewo (o kąt prosty), zmienia kolor pola na czarny i przechodzi na następną komórkę;
jeśli znajduje się na polu czarnym to obraca się w prawo (o kąt prosty), zmienia kolor pola na biały i przechodzi na następną komórkę;
porusza się na nieskończonej planszy podzielonej na kwadratowe komórki (pola) w dwóch możliwych kolorach: czarnym i białym.
Inny opis: Mrówka znajduje się w określonym polu i porusza się w określonym kierunku (skręca w prawo lub w lewo w zależności na jakie trafi pole). Jeśli trafi na czarną pełną komórkę (pole żywe o wartości 1), to skręca w prawo o kąt 90 stopni i zjada ją czyli zamienia w pustą wolną komórkę (pole martwe, stan o wartości 0), jeśli zaś mrówka trafi na pole martwe to skręca w lewo o kąt 90 stopni i ożywia je.

Mówiąc inaczej mrówka wchodząc w białą kratkę maluje ją na czarno i skręca w lewo, natomiast jeśli wejdzie w czarną kratkę, to maluje ją na biało i skręca w prawo. Początkowo wszystkie kratki na kartce są białe. Po kilkudziesięciu krokach mrówki pokolorowane przez nią kratki tworzą formę chaotyczną. Jednakże po ok. 10 tysiącach kroków mrówka zaczyna replikować pewien charakterystyczny wzór tworząc tzw. autostradę.

Zadziwiającą własnością tego automatu jest cykl, który pojawia się po pewnym czasie chaotycznego błądzenia. Jednakże, gdy symulacja rozpoczyna się na planszy posiadającej wszystkie pola o tym samym kolorze, wówczas po ok. 10 tysiącach kroków mrówka przestaje poruszać się chaotycznie, tworząc na planszy regularny wzór w kształcie grubego na kilka kratek pasa. Co 104 kroki czasowe pas ten zwiększa swoją długość. Podobnie jak w maszynach Turinga, mimo bardzo prostych zasad zachowanie mrówki przez długi czas od rozpoczęcia symulacji może być bardzo trudne do przewidzenia.

Powstały modyfikacje podstawowych reguł zwiększające liczbę możliwych kolorów (stanów) komórki.

Ciekawe symulacje otrzymuje się, gdy mrówka ma do pokonania przeszkody z żywych komórek albo gdy jest kilka aktywnych mrówek, np. 3.

Źródło: https://pl.wikipedia.org/wiki/Mrówka_Langtona
