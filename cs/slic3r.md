Slic3r
======

Program Slic3r
--------------

-   OpenSource nástroj pro generování GCode
-   Více na [Webu projektu](http://slic3r.org)

Ukázka
------

[](../images/slic3r/slic3r.png)

Panely
------

-   Plater - Na rozložení objektů po tiskové ploše
-   Print Settings - Veškerá nastavení tisku, jako rychlost, 
    výplň, podpory, atd.
-   Filament Settings - Nastavení specifické pro materiál. 
    Teploty, průměr, chlazení.
-   Printer Settings - Nastavení specifické pro tiskárnu. Průměr trysky, 
    velikost tiskové plochy, atd.

Pozn.: Jelikož jsme experti, tak budeme pracovat v Expert modu 8-)

Printer Settings
----------------

-   General
    -   Nastavení rozměrů tiskárny
    -   Typ firmwaru
    -   Počet extruderů

-   Custom G-code
    -   Vlastní definice startu a konce souboru

-   Extruder X
    -   Průměr trysky
    -   Offset, pokud máme více trysek vedle sebe
    -   Rectraction
        -   Eliminace tlaku v trysce

Filament Settings
-----------------

-   Filament
    -   Průměr materiálu
    -   Teploty

-   Cooling
    -   Chlazení objektů, aby se nepřehřívaly/nedeformovaly

Print Settings
--------------

### Layers and Perimeters

#### Výška vrstvy

Ideální výška je okolo 0,2mm

[Zdroj: http://arduinoblog11.blogspot.cz/2012_04_01_archive](../images/slic3r/layer_height_comparison.jpg)

#### Perimeters

Jak silný bude "plášť" objektu

[](../images/slic3r/very_slightly_over_stuck_down_print.jpg)

### Infill

Více o výplni na stránce [programu](http://manual.slic3r.org/expert-mode/infill)

[](../images/slic3r/linear_2pc_25pc_50pc_with_scale.jpg)

[](../images/slic3r/rectilinear_line.jpg)

[](../images/slic3r/concentric_and_archimedial_fill.jpg)

[](../images/slic3r/hilbert_octag.jpg)

### Speed

Možnost nastavit rychlosti konkrétních částí objektu.

### Skirt

Obvodová linie objektu.

[](../images/slic3r/screen_shot_2013-10-16_at_21.50.13.png)

Lze nastavit počet linií a výšku.
Proč asi výšku?

### Support Material

Proč?

Více na stránce [programu](http://manual.slic3r.org/expert-mode/support-material)

Plater
------

-   Poskládání objektů na tiskovou plochu

Odkazy
------

-   starší ale zajímavý třídílný článek **slic3r is nicer** [1](http://richrap.blogspot.cz/2012/01/slic3r-is-nicer-part-1-settings-and.html), [2](http://richrap.blogspot.cz/2012/01/slic3r-is-nicer-part-2-filament-and.html), [3](http://richrap.blogspot.cz/2012/01/slic3r-is-nicer-part-3-how-low-can-you.html), 
