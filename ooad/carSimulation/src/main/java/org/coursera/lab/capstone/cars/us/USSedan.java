package org.coursera.lab.capstone.cars.us;

import org.coursera.lab.capstone.cars.Car;
import org.coursera.lab.capstone.components.us.USStandardEngine;
import org.coursera.lab.capstone.components.us.USStandardSuspension;
import org.coursera.lab.capstone.components.us.USStandardTires;

public class USSedan extends Car {
    public USSedan() {
        this(13000);
    }

    public USSedan(int cost) {
        super("USSedan", cost, new USStandardEngine(), new USStandardSuspension(), new USStandardTires());
    }
}
