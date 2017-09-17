# MeshMixer a řezání STL souborů

Aktuální MeshMixer 2.9 najdete na [stránkách programu](http://www.meshmixer.com/). Existuje verze pro Windows a Mac OS X. A experimentální balíček pro Ubuntu 14.04 (můžete si z něj relativně jednoduše udělat [AppImage](https///github.com/hroncok/meshmixer-docker/blob/master/README.md#how-to-create-meshmixer-appimage) a spouštět ho na jiných distribucích).

<https://www.youtube.com/watch?v=cVx1vXq8Xao>

Cura je dostupná ve dvou variantách, já doporučuji stáhnout [Cura Lulzbot Edititon](https///www.lulzbot.com/cura) nebo [starší verzi Ultimaker Cura (15.x)](https///ultimaker.com/en/products/cura-software/list) (nová verze je celá předělaná a návod nebude souhlasit).

<https://www.youtube.com/watch?v=FNOLtlEaJKA>

Mohlo by se vám také hodit: <https://www.youtube.com/watch?v=SiBXboixe2g>

A ještě řezání ve Slic3ru: <https://www.youtube.com/watch?v=1U4MVuaSv0U>

# MeshMixer 2.4

Tato část návodu (bez videí) je pro starou verzi MeshMixeru, ale vystačíte si s jedním programem.

## Instalace

MeshMixer 2.4 najdete na [stránkách programu](http://www.meshmixer.com/). Existuje verze pro Windows a Mac OS X. V Linuxu jde verze pro Windows nainstalovat pomocí programu Wine, jen musíte do složky s programem (obvykle ''~/.wine/drive_c/Program Files/Autodesk/Meshmixer/'') dodat soubory [mfc110u.dll](http://www.dllme.com/dll/files/mfc110u_dll.html) a [prntvpt.dll](http://www.dllme.com/dll/files/prntvpt_dll.html). Jediný problém, se kterým jsme se setkali, jsou divné fonty a crash při prvním spuštění.

{{:tutorials:meshmixer:meshmixer1.png?400}}

## Řez objektem

Nejprve importujte STL soubor pomocí tlačítka **Import**.

{{:tutorials:meshmixer:meshmixer2.png?400}}

Poté z nabídky **Edit** vyberte **Plane Cut**.

{{:tutorials:meshmixer:meshmixer3.png?400}}

Pomocí všelijakých šipek můžete manipulovat rovinou řezu. Můžete také táhnout stisknutou myš a vytvořit čáru (na obrázku červená), podél které se rovina přemístí, rovnoběžně s vaším pohledem. Pokud je objekt umístěn nepříhodně, můžete s ním rotovat pravým tlačítkem myši. Před stisknutím tlačítka **Accept** se ujistěte, že máte vybráno **Type: Slice**, jinak skončíte pouze s jednou částí objektu.

{{:tutorials:meshmixer:meshmixer4.png?400}}

Po provedení řezu vypadá objekt stejně jako předtím. Musíte opět z menu **Edit** vybrat **Separate Shells**.

{{:tutorials:meshmixer:meshmixer5.png?400}}

V modálním okně můžete vybírat, který shell bude vidět, případně na jakém se provádí akce (pozor, to je rozdíl, jedno řeší to očičko, druhé řeší jakoby zvolení a zvýraznění toho shellu v seznamu). Rovnou pro jeden shell vyberte z nabídky **Edit** možnost **Align**. To proto, aby objekt ležel na placaté části, jinak byl řez k ničemu.

{{:tutorials:meshmixer:meshmixer8.png?400}}

V dialogu **Align** je vybrána ve výchozím stavu osa Y. To by snad mělo zajistit položení objektu na plocho (i když možná vzhůru nohama, k tomu se dostaneme), takže stačí dát **Accept**.

{{:tutorials:meshmixer:meshmixer9.png?400}}

Z menu **File** zvolte **Export** a uložte danou část jako STL soubor. Doporučuji zkontrolovat, že jste vyexportovali správnou část (otevřením výsledného STL v nějakém programu).

{{:tutorials:meshmixer:meshmixer10.png?400}}

Postup zopakujte pro druhou polovinu. Zde nastal případ, že **Align** otáčí objekt jinak, než chceme. Stačí kliknout na šipku (označenou zeleným puntíkem) a pokračovat jako u předchozí části.

{{:tutorials:meshmixer:meshmixer11.png?400}}

{{:tutorials:meshmixer:meshmixer12.png?400}}

{{:tutorials:meshmixer:meshmixer13.png?400}}
