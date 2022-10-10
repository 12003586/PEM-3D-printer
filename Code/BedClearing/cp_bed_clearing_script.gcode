M18 ; disable steppers
M104 T0 S0 ; extruder heater off
M140 S0 ; heated bed heater off
G1 Y195 ; Brings the bed all the way forward - so the ram is behind the part
G1 Z0 ; Homes Z axis, which touches nozzle to glass stopping any leaking and brings the ram down behind the part
G4 P360000 ;Do nothing for 360,000milliseconds (6 minutes) in order to allow the bed to cool so the parts come loose
G1 Z0.2 ; Lift the nozzle slightly so it doesn't scrape along the bed during the ramming movement
G1 Y0 F6000 ; Sends the bed moving backwards, print impacts ram and is pushed off front of bed onto paper chute
