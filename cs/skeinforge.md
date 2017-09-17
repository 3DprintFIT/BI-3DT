Skeinforge
==========

> Skeinforge se v tomto roce nevyučuje. 
> Je příliš zastaralý a obtížný na pochopení.

Co to je?
---------

-   Nástroj/sada v jazyku Python pro převod STL na GCode
-   Detailní popis na [vlastních stránkách](http://fabmetheus.crsndoo.com/wiki/index.php/Skeinforge)

[](../images/skeinforge/skeinforge.png)

Kalibrace vs. Nastavení tisku
-----------------------------

-   Narozdíl od Slic3r je potřeba nejprve dobrá kalibrace profilu

-   Větší svoboda v nastavení všech parametrů tisku

-   Parametry v některých modulech jsou po kalibraci neměnné

Jak se to pouští ve Fedoře
--------------------------

-   Z řádky:
    -   ''skeinforge'' vyvolá nastavení 
        (nebo **Aplikace -> Grafika -> Skeinforge**)
    -   ''skeinforge soubor.stl'' soubor naslajsuje a udělá další věci (analýzu)
    -   ''skeinforge-craft soubor.stl'' soubor jen naslajsuje 
        (použije se PyPy místo Pythonu)

-   Z Pronterfacu:
    -   **Settings -> Slicing settings** zavolá ''skeinforge''
    -   **Load file (STL)** zavolá ''skeinforge-craft soubor.stl''
    -   obojí jde změnint

-   [český článek na Fedora.cz](http://fedora.cz/slicery-pro-3d-tisk-skeinforge/) 
    popisuje nejen to

Jak se to pouští jinde
----------------------

-   `python skeinforge/skeinforge_application/skeinforge.py`
-   `pypy 
    skeinforge/skeinforge_application/skeinforge_utilities/skeinforge_craft.py 
    file.stl`
-   `Funguje to i z Prontrefacu, pokud je skeinforge ve složce Printrun 
    (neověřeno na Windows)`

Rozdíl mezi Pythonem a PyPy
---------------------------

-   Čas (z-motor-mount-stl):
    -   Python: ''It took 2 minutes 2 seconds to export the file.''
    -   PyPy: ''It took 30 seconds to export the file.''

-   PyPy umí jen slicovat, neumí GUI!

Naše profily
------------

-   <https://github.com/3DprintFIT/3DPrintFIT-skeing>
-   ''git clone <https://github.com/3DprintFIT/3DPrintFIT-skeing.git> 
    ~/.skeinforge''

Nejdůležitější moduly
---------------------

Moduly jsou také popsány na [RepRap wiki](http://reprap.org/wiki/Skeinforge/cs)

### Kalibrační

-   Alternation
    -   Nastavení začátku a konce GCode
-   Clip
    -   Napojení perimetru a výplně
-   Chamber
    -   Teplota desky
-   Temperature
    -   Teplota trysky
-   Speed
    -   Rychlosti tisku
-   Cool
    -   Chlazení objektů
-   Dimension
    -   Retract

### Nastavení tisku

-   Carve
    -   Šířka a výška vrstvy
-   Raft
    -   Podpora a tisková základna
-   Multiply
    -   Střed tiskárny a možnost nastavení více kopií
-   Fill
    -   Nastavení výplně a perimetrů
-   Skirt
    -   Obrys objektů (vyčištění trysky)

Co není důležité, ale na co dávat pozor
---------------------------------------

-   Limit
    -   Omezení maximálního pohybu tiskové hlavy (pouze X a Y)
-   Scale
    -   Měřítko tištěného objektu

Zadání úloh
-----------

1.  {{:tutorials:slic3r:aligator_mini.stl|}} -- (předváděcí úloha) 16 krokoušů, 
    ať mají dva permietry, výšku vrstvy 0.35 mm a infill 40% včelí plásty
1.  {{:tutorials:slic3r:cube.stl|}} -- devět kostiček, každá s jedním perimterm,
    dutá, výška vrstvy 0.4 mm, nahoře i dole jen jeden plát
1.  {{:tutorials:slic3r:haky2.stl|}} -- čtyři háky, úplně plné, 
    výška vrstvy 0.3 mm
1.  {{:tutorials:slic3r:cute_octo.stl|}} -- jeden perimetr, žádný infill, 
    vrstva 0.3 mm
1.  {{:tutorials:slic3r:koch_snowflake.stl|}} -- dutá váza s otvorem nahoře 
    (nutno upravit GCODE!), tři perimtery, nastavit výšku vrstvy dle uvážení
1.  {{:tutorials:slic3r:liberty.stl|}} -- dutá s podporou venku, dva perimetry,
    nastavit výšku vrstvy dle uvážení
