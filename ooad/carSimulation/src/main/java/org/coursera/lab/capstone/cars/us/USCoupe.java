package org.coursera.lab.capstone.cars.us;

import org.coursera.lab.capstone.cars.Car;
import org.coursera.lab.capstone.components.us.USStandardEngine;
import org.coursera.lab.capstone.components.us.USRacingSuspension;
import org.coursera.lab.capstone.components.us.USRacingTires;

public class USCoupe extends Car {
    public USCoupe() {
        this(18000);
    }

    public USCoupe(int cost) {
        super("USCoupe", cost, new USStandardEngine(), new USRacingSuspension(), new USRacingTires());
    }
}
