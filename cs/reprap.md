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
[Video](https///www.youtube.com/watch?v=NM55ct5KwiI)

![Stereolitografie](../images/stereolithography_apparatus.jpg)

Práškový tisk (SLS, DMLS)
------------------------

Technologie je založena na kladení tenkých vrstev prášku a následného vytvrzení 
pouze potřebných míst. Vytvrzení může probíhat buď zapečením prášku laserem 
(například kov, DMLS), nebo použitím tekutého polymeru a ozářením většinou 
UV zářením. [Video SLS](https///www.youtube.com/watch?v=9E5MfBAV_tA), 
[Video DMLS](https///www.youtube.com/watch?v=bgQvqVq-SQU)

![](../images/f0hg3k6gijg2h2t.large.jpg)

PolyJet
-------

Podobně jako v inkoustových tiskárnách je polymer vytryskáván z tiskové hlavy 
pomocí miniaturních trysek. Následně je vrstva vytvrzena UV paprskem.
[Video](https///www.youtube.com/watch?v=ZjXh1RJfA34)

![](../images/polyjetprocess72dpi.jpg)

FFF/FDM/Thermoplastic extrusion
-------------------------------

FFF (fused filament fabrication) nebo FDM (Fused Deposition Modeling) je 
technologie, která je založena na principu "tavné pistole". Plast je tlačen do 
trysky, kde je roztaven a následně je kladen na podložku.
[Video](https///www.youtube.com/watch?v=WHO6G67GJbM)

![](../images/fdm_by_zureks.png)

*1 - tryska vytlačující plast, 2 - vymodelovaná část objektu, 
3 - pohybující se platforma*

RepRap
------

-   Adrian Bowyer, University of Bath 2006
-   RepRap Darwin, 2007
-   RepRap Mendel, 2009
-   3DPrintLab, 2012

Více na <http://reprap.org/wiki/RepRap_history>

Technologie RepRap
------------------

FFF/FDM - technologie tavení plastového drátu (termoplastu) v trysce. 
Principem RepRap tiskárny je částečná replikace sebe sama.

### Výhody

-   Levné (Pořizovací náklady cca 10000 Kč, cena plastu cca 0.7 Kč/g)
-   OpenSource/OpenHardware

### Nevýhody

-   Pořízení první tiskárny (slepice/vejce)

Základní modely Reprap
----------------------

{{:tutorials:reprap:reprap_darwin.jpg?200|Darwin}}
{{:tutorials:reprap:reprap_v2_mendel.jpg?200|Mendel}}
{{:tutorials:reprap:rostock.jpg?200|Rostock}}

Fork-modely
-----------

{{:tutorials:reprap:linuxalt-2012-29.jpg?200|Huxley}}
{{:tutorials:reprap:assembled-prusa-mendel.jpg?200|PrusaMendel}}
{{:tutorials:reprap:prusai3-metalframe.jpg?200|Prusa i3}}
{{:tutorials:reprap:rebel2-lcd-bez-zdroje.jpg?200|Rebel II}}
{{:tutorials:reprap:rebelix.jpg?200|RebeliX}}
{{:tutorials:reprap:kossels.jpeg?200|Kossel}}

Speciální typy
--------------

{{:tutorials:reprap:reprap_magazine_morgan-article-mockup-11.jpg?200|Morgan}}
{{:tutorials:reprap:below2_preview_featured.jpg?200|Folding RepRap}}

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
-   [FilaFlex](https///www.youtube.com/watch?v=Vmb9iwFpaOs) - elastický

Literatura a užitečné odkazy
----------------------------

Najdete v sekci [Literatura](literature.md)
