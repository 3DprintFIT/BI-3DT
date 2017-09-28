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

![Stereolitografie](../images/reprap/stereolithography_apparatus.jpg)

(Obrázek z [Wikipedie](https://commons.wikimedia.org/wiki/File:Stereolithography_apparatus.jpg) © Materialgeeza (CC BY-SA).)

Práškový tisk (SLS, DMLS)
------------------------

Technologie je založena na kladení tenkých vrstev prášku a následného vytvrzení 
pouze potřebných míst. Vytvrzení může probíhat buď zapečením prášku laserem 
(například kov, DMLS), nebo použitím tekutého polymeru a ozářením většinou 
UV zářením. [Video SLS](https://www.youtube.com/watch?v=9E5MfBAV_tA), 
[Video DMLS](https://www.youtube.com/watch?v=bgQvqVq-SQU)

![Práškový tisk](../images/reprap/sls.jpg)

([Obrázek](https://www.prlog.org/12539309-3d-printing-powder-market-analysis-till-2021-download.html) © PRLog.)

PolyJet
-------

Podobně jako v inkoustových tiskárnách je polymer vytryskáván z tiskové hlavy 
pomocí miniaturních trysek. Následně je vrstva vytvrzena UV paprskem.
[Video](https://www.youtube.com/watch?v=ZjXh1RJfA34)

![PolyJet](../images/reprap/polyjet.jpg)

(Nedokážeme dohledat původ obrázku, pomůžete nám? Na internetu je příliš rozšířený.)

FFF/FDM/Thermoplastic extrusion
-------------------------------

FFF (fused filament fabrication) nebo FDM (Fused Deposition Modeling) je 
technologie, která je založena na principu "tavné pistole". Plast je tlačen do 
trysky, kde je roztaven a následně je kladen na podložku.
[Video](https://www.youtube.com/watch?v=WHO6G67GJbM)

![FDM](../images/reprap/fdm_by_zureks.png)

(Obrázek z [Wikipedie](https://commons.wikimedia.org/wiki/File:FDM_by_Zureks.png) © Zureks (CC BY-SA).)

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

(© [Adrian Bowyer](http://reprap.org/wiki/File:RepRapOneDarwin-darwin.jpg), GNU FDL)

![RepRap Mendel](../images/reprap/reprap_v2_mendel.jpg)

(© [Adrian Bowyer](http://reprap.org/wiki/File:Mendel.jpg), GNU FDL)

![Rostock](../images/reprap/rostock.jpg)

(© [Johann C. Rocholl](http://reprap.org/wiki/File:Rostock.jpg), GNU FDL)


Fork-modely
-----------

![Huxley](../images/reprap/huxley.jpg)

(© [Petr Krčmář, root.cz](https://www.root.cz/galerie/linuxalt-2012/#29), použito se svolením)

![Prusa Mendel](../images/reprap/assembled-prusa-mendel.jpg)

(© [Josef Průša](http://reprap.org/wiki/File:Assembled-prusa-mendel.jpg), GNU FDL)

![Prusa i3](../images/reprap/prusai3-metalframe.jpg)

(© [Bitflusher](http://reprap.org/wiki/File:Prusai3-metalframe.jpg), GNU FDL)

![Rebel 2](../images/reprap/rebel2.jpg)

(© [Petr Zahradník](https://www.clexpert.cz/3dtisk/rebel2/), fair use)

![RebeliX](../images/reprap/rebelix.jpg)

(vlastní foto)

![Kossel](../images/reprap/kossel.jpg)

(© [Johann C. Rocholl](http://reprap.org/wiki/File:Kossel.jpg), GNU FDL)


Speciální typy
--------------

![Morgan](../images/reprap/morgan.jpg)

(© [Morgan 3D Printers](http://www.morgan3dp.com/reprap-morgan-source/), GPLv2)

![FoldaRap](../images/reprap/foldarap.jpg)

(© [Emmanuel](https://www.thingiverse.com/thing:15877), GPLv2)


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
