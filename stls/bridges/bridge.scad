module bridge(width = 12.5,
              length = 138,
              height = 10) {
    base = 8;
    bridge_thick = 1;
    magic = 0.75;

    cube([base,width,height],center=true);
    translate([length+base,0,0])
        cube([base,width,height],center=true);
    color("red")
        translate([length/2+base/2,0,height/2+bridge_thick/2])
            cube([length+2*base,width,bridge_thick],center=true);

    mySize = (width > length) ? length : width;
    translate([0,-width/2*magic,height/2+bridge_thick])
        resize([length*magic,width*magic,1])
            linear_extrude(height = magic)
                text("TEST", size=mySize/2);
}


bridge();
