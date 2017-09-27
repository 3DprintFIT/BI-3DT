# Programy

Pokud chcete při cvičení používat vlastní počítač, nutně budete potřebovat tyto programy:

 -  [OpenSCAD](http://openscad.org) 2015.03
 -  [netfabb Basic](http://www.netfabb.com/downloadcenter.php?basic=1) (firmu netfabb koupil Autodesk a link nefunguje, naše zálohy najdete na [GitHubu](https://github.com/3DprintFIT/netfabb-basic-download/releases))
 -  [Printrun](http://reprap.org/wiki/Printrun)
 -  [Slic3r](http://slic3r.org/) 
 -  [KiSSlicer](http://kisslicer.com/)
 -  [ADMesh](https://github.com/admesh/admesh) >= 0.98 (včetně devel balíků, pokud instalujete z repozitářů)

Dále by se vám mohlo hodit:

 -  [Cura Lulzbot Edition](https://www.lulzbot.com/cura)
 -  [Meshlab](http://meshlab.sourceforge.net/)
 -  [ADMeshGUI](https://github.com/admesh/ADMeshGUI) na prohlížení STL souborů
 -  [Blender](http://www.blender.org/) >= 2.67

## Instalace v Linuxu

Doporučenou linuxovou distribucí je **Fedora**, protože obsahuje všechny toto nástroje v
repozitářích (kromě netfabbu a KISSliceru, které nejsou open-source, ty ale najdete v
oblíbeném repozitáři [RPM Fusion](http://rpmfusion.org/)).

K ovládání tiskárny je potřeba, aby váš uživatel mohl přistupovat k USB přes serial interface,
což ve většině linuxových distribucí obnáší **přidání uživatele do skupiny dialout**. Na cvičení
to ale nebude potřeba.

### Fedora

 -  Pro instalaci všech nástrojů a aplikací: `# dnf install @3d-printing admesh-devel admeshgui`
 -  Pouze nezbytně nutné: `# dnf install printrun slic3r openscad admesh-devel admeshgui`
 -  netfabb Basic a KISSlicer naleznete v repozitáři [RPM Fusion](http://rpmfusion.org/),
jako `netfabb-basic`, respektive `kisslicer`

Používejte podporovanou verzi Fedory, jinak budete mít staré verze programů. Na cvičení používáme
Slic3r 1.2.9.

### Ostatní distribuce

Existuje určitá pravděpodobnost, že některé tyto programy jsou k dispozici přes balíčkovací
systém vaší distribuce. U těch známějších (Blender, Meshlab) je ta pravděpodobnost vyšší.
Pokud je v distribuci nenajdete, postupujte podle instrukcí na webu aplikace.

 -  [Instalace OpenSCADu](http://www.openscad.org/downloads.html#linux)
 -  [Stažení netfabbu](https://github.com/3DprintFIT/netfabb-basic-download/releases)
 -  [Stažení KISSliceru](http://kisslicer.com/download.html)
 -  [Instalace Printrunu](http://reprap.org/wiki/Printrun#GNU.2FLinux_.26_Distros)
 -  [Binárky Slic3ru](http://dl.slic3r.org/linux/)
 -  [Instalace ADMeshe](https://github.com/admesh/admesh/blob/master/INSTALL)
 -  [Instalace ADMeshGUI](https://github.com/admesh/ADMeshGUI#building)

### Instalace v macOS

V OS X máme připraveny předkompilovanou verzi Pronterface, který stačí stáhnout a spustit
(viz odkazy níže). 

 -  [Printrun](http://koti.kapsi.fi/~kliment/printrun/)

Další možností je instalace (stažení) a spuštění přímo ze zdrojových kódů aplikace
(odkazy v linuxové části).

ADMesh je třeba zkompilovat stejně jako na Linuxu, případně lze použít homebrew.
Stejně tak pro [ADMeshGUI](https://github.com/admesh/ADMeshGUI#building).

[Netfabb](https://github.com/3DprintFIT/netfabb-basic-download/releases) je třeba stáhnout z
našeho GitHubu.

Ostatní software má vždy svou Mac variantu ke stažení na stránce programu.

### Instalace ve Windows

Pro Windows je všechen software, až na výjimky, připraven v předkompilované verzi. Ve většině
případů na stránkách programu uvedených výše.

Výjimky:

 -  [Printrun](http://koti.kapsi.fi/~kliment/printrun/)
 -  [Předkompilovaný ADMesh pro Windows](https://github.com/admesh/admesh/releases)

Netfabb Basic: Můžete použít [Oficiální Trial verzi pro Windows](https://www.netfabb.com/try-netfabb-premium-now), která po vypršení funguje jako Basic, nebo starší verzi Netfabb Basic
[z našeho GitHubu](https://github.com/3DprintFIT/netfabb-basic-download/releases).

Pro připojení některých tiskáren je třeba instalovat všelijaké drivery. Na cvičení to ale
