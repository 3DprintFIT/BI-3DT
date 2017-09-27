Technologie tisku a RepRap
==========================

Proč 3D tisk?
-------------

-   levná a rychlá výroba prototypů (v řádu hodin)
-   snadné přenesení grafických návrhů do fyzické podoby
-   nejsme dostatečně zruční abychom si to vyrobili sami
-   nechceme sériovou výrobu
-   zábava 😎

Základní princip
----------------

Jak to celé funguje?

Všechny technologie 3D tisku mají společný základní princip kladení vrstev na 
sebe, kterému se říká aditivní výroba. Je to opačný proces k obrábění materiálu.
Místo toho, aby byl objekt z kusu materiálu vyřezán, je z materiálu 
postupně vyráběn.

3D model je "rozřezán" na tenké vrstvy, které se pak v tiskárně kladou na sebe. 
Můžeme si to představit, jako kdybychom chtěli za pomocí stolní tiskárny vyrobit
3D objekt z papíru. Nejprve vytiskneme všechny potřebné vrstvy, poté nůžkami 
vystříháme a nalepujeme na sebe.

Stereolitografie (SLA)
----------------------

Metoda vytváření objektů z tekutého polymeru, který je postupně vytvrzován 
pomocí záření různých vlnových délek. 
[Video](https://www.youtube.com/watch?v=NM55ct5KwiI)

![Stereolitografie](../images/stereolithography_apparatus.jpg)

Práškový tisk (SLS, DMLS)
------------------------

Technologie je založena na kladení tenkých vrstev prášku a následného vytvrzení 
pouze potřebných míst. Vytvrzení může probíhat buď zapečením prášku laserem 
(například kov, DMLS), nebo použitím tekutého polymeru a ozářením většinou 
UV zářením. [Video SLS](https://www.youtube.com/watch?v=9E5MfBAV_tA), 
[Video DMLS](https://www.youtube.com/watch?v=bgQvqVq-SQU)

![Práškový tisk](../images/sls.jpg)

PolyJet
-------

Podobně jako v inkoustových tiskárnách je polymer vytryskáván z tiskové hlavy 
pomocí miniaturních trysek. Následně je vrstva vytvrzena UV paprskem.
[Video](https://www.youtube.com/watch?v=ZjXh1RJfA34)

![PolyJet](../images/polyjet.jpg)

FFF/FDM/Thermoplastic extrusion
-------------------------------

FFF (fused filament fabrication) nebo FDM (Fused Deposition Modeling) je 
technologie, která je založena na principu "tavné pistole". Plast je tlačen do 
trysky, kde je roztaven a následně je kladen na podložku.
[Video](https://www.youtube.com/watch?v=WHO6G67GJbM)

![FDM](../images/reprap/fdm_by_zureks.png)

*1 - tryska vytlačující plast, 2 - vymodelovaná část objektu, 
3 - pohybující se platforma*

RepRap
------

-   Adrian Bowyer, University of Bath 2006
-   RepRap Darwin, 2007
-   RepRap Mendel, 2009
-   3DPrintLab, 2012

Více na [reprap.org/wiki/RepRap_history](http://reprap.org/wiki/RepRap_history).

Technologie RepRap
------------------

FFF/FDM - technologie tavení plastového drátu (termoplastu) v trysce. 
Principem RepRap tiskárny je částečná replikace sebe sama.

### Výhody

-   Levné (Pořizovací náklady cca 10000 Kč, cena plastu cca 0.7 Kč/g)
-   OpenSource/OpenHardware

### Nevýhody

-   Pořízení první tiskárny (slepice/vejce)

Základní modely RepRap
----------------------

![RepRap Darwin](../images/reprap/reprap_darwin.jpg)
![RepRap Mendel](../images/reprap/reprap_v2_mendel.jpg)
![Rostock](../images/reprap/rostock.jpg)

Fork-modely
-----------

![Huxley](../images/reprap/huxley.jpg)
![Prusa Mendel](../images/reprap/assembled-prusa-mendel.jpg)
![Prusa i3](../images/reprap/prusai3-metalframe.jpg)
![Rebel 2](../images/reprap/rebel2.jpg)
![RebeliX](../images/reprap/rebelix.jpg)
![Kossel](../images/reprap/kossels.jpeg)

Speciální typy
--------------

![Morgan](../images/reprap/morgan.jpg)
![FoldaRap](../images/reprap/foldarap.jpg)

Vstupní formát (Slicing)
------------------------

**STL** (STereoLitography) -- mesh trojúhelníků, popisuje povrchovou geometrii 
modelu.

Exportovaný z jakéhokoliv 3D modelovacího programu. Více informací v
kapitole [Práce s meshí](mesh.md).

Vstupní formát tiskárny
-----------------------

**GCode** -- instrukce pro tiskárnu 

Příklad:

```plain
G1 X10 Y10 Z10 E10
M220 S150 
```

Tiskové materiály
-----------------

### SLA

Fotopolymer - pro domácí použití příliš drahý

### SLS

Práškový materiál (kov nebo plast)

### FDM/FFF

Plastový materiál v drátu

-   ABS - lego a tiskárny
-   PLA - ekologický
-   Nylon - vysoce odolný
-   PVA - rozpustný ve vodě
-   [FilaFlex](https://www.youtube.com/watch?v=Vmb9iwFpaOs) - elastický
