# OpenSCAD: Molekula

```cpp
module molecule(ar=2, ac=6, ad=5, tr=0.5) {
    for(x=[0:(ac-1)],y=[0:(ac-1)],z=[0:(ac-1)]) {
        translate([x*ad,y*ad,z*ad]) sphere(ar);
        trc([x*ad,y*ad,0], [0,0,0], ad*(ac-1), tr);
        trc([x*ad,0,z*ad], [-90,0,0], ad*(ac-1), tr);
        trc([0,y*ad,z*ad], [0,90,0], ad*(ac-1), tr);
    }
}

module trc(tv, rc, ch, cr) {
    translate(tv)
            rotate(rc)
                cylinder(h=ch, r=cr);
}

molecule();
```




```cpp
module molecule(ar=3, ac=4, ad=8, rr=0.5) {
    for (x = [0:ac-1], y = [0:ac-1], z = [0:ac-1]) {
        translate([x*ad, y*ad, z*ad]) sphere(ar);
    }
    for (i = [0:ac-1], j = [0:ac-1]) {
        trc([i*ad, j*ad, 0], [0,0,0], rr=rr, h=ad*(ac-1));
        trc([0, i*ad, j*ad], [0,90,0], rr=rr, h=ad*(ac-1));
        trc([i*ad, 0, j*ad], [-90,0,0], rr=rr, h=ad*(ac-1));
    }
}

module trc(tra, rot, rr, h) {
    translate(tra)
        rotate(rot)
            cylinder(r=rr, h=h);
}

molecule(ac=2);
```
