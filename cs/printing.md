Tisk
====

OctoPrint
---------

Při kalibračním a dalším tisku budeme používat webový 
ovládací interface [OctoPrint](http://octoprint.org).

![Náhled](../images/printing/octoprint.png)

(Obrázek z [README] OctoPrintu © Gina Häußge (AGPL).)

[README]: https://github.com/foosel/OctoPrint/blob/master/README.md

Předletová příprava
-------------------

Před spuštěním tisku je potřeba dodržet několik kroků. V případě tiskárnu 
nezkontrolujeme, můžeme skončit s špatným výtiskem, nebo v horším 
případě s poškozenou tiskárnou. 

1.  Zkontrolovat správné nastavení osy Z (výška endstopu)
2.  Připravit tiskovou desku (bude upřesněno)
3.  Předehřát tiskovou desku (trvá déle než předehřátí trysky)

Nastavení pro Slic3r
--------------------

Config bundle ke stažení [zde](../configs/printing/slic3r_config_bundle.ini)

Testovací objekt
-----------------

[20mm-box.stl](../stls/printing/20mm-box.stl)


Úkol
----

### 1. úkol (1 bod)

Tiskárna, která se vám objevila na stole, zrovna přijela na kontrolu.
Je tedy potřeba abyste ověřili, zda dělá to, co by dělat měla.
K tiskárně jste dostali tiskový profil, který na ní byl doteď používán.
Předpokládejme, že není potřeba ho upravovat po kalibrační stránce
(hodnoty jako velikost trysky a údaje o materiálu jsou správné).
Jako testovací objekt jste si vybrali [model kostky o přesných rozměrech
20×20×10 mm](../stls/printing/20mm-box.stl). Potřebujete ověřit, zda tiskárna
skutečně vytiskne stejné rozměry, které jsou v modelu.
Abyste ušetřili materiál, nastavte tisk tak, aby se vytiskly kostky 4 a každá
z nich byla dutá, měla jednu obvodovou vrstvu a žádnou vrchní vrstvu
(ve výsledku byste měli dostat 4 hranaté kalíšky).

(Model je z [The Essential Calibration Set](https://www.thingiverse.com/thing:5573), Public Domain.)

### 2. úkol (1 bod)

V předchozím úkolu jste již ověřili, že tiskárna tiskne správné rozměry.
Teď byste rádi vynahradili své drahé polovičce, že jste v práci a testujete
tiskárny místo toho, abyste byli doma. Proto se rozhodnete vytisknout [model
chobotnice](../stls/printing/cuteocto.stl) na památku.
Bohužel je moc velká a nemáte tolik času. Proto musíte upravit rozměry a
vytisknout ji o polovinu menší. Kdyby se něco pokazilo, vytisknete najednou
raději hned 2 kopie. U chobotnice není nutné, aby byla dutá, nastavte tedy tisk
tak, aby měla výplň alespoň 10%. Zajistěte, aby hlava chobotnice nebyla
propadlá (použijte dostatečné množství perimetrů).

(Model je z [Cute Octopus Says Hello](https://www.thingiverse.com/thing:27053), CC BY MakerBot.)

### 3. úkol (1 bod, povinný úkol)

Ukliďte po sobě. Kdo po sobě neuklidí, nedostane body.
