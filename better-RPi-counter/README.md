This is a modified counter circuit that still runs off of a Raspberry Pi B+.

In this circuit, the RPi GPIO output (in my case pin 5) will be used to trigger the start of a counting cycle.

Problem is, the RPi pins are only 3.3V which in not enough on the output of the 555 timer (only about 1.75V) to then trigger the counter in the 4026 chip.

So, solved this by having a separate 5V power supply (might be able to use the RPi 5V output, I just used by bench power supply...

Anyway, the RPi pin 5 is used via a 1k resistor to trigger a 2N2222 transistor which will then connect the LOW side (GND - pin 1 of the 555) to trigger the 555 and supply enough on the 555 output (pin 3) to trigger the 4026 and begin the count.

Counting speed out of the 555 timer is controlled by the capacitor between pins 4/6 on the 555 to ground. 10uF counts at about 10 steps per second.

The switch in the circuit will stop the counter and increment the second 7-segment counter (which indicates the number of times the switched is pushed) via the 74LS47 BCD 7-segment counter. Note: the 7447 is the counter for a common anode 7-segment display - meaning connecting to the LOW side (ground) is necessary through the 7447 - a bit trickier, but I am the moron who ordered the 7447 from Jameco and not the 7448's...
