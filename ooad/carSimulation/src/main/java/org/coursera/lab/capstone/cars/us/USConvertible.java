package org.coursera.lab.capstone.cars.us;

import org.coursera.lab.capstone.cars.Car;
import org.coursera.lab.capstone.components.us.USRacingEngine;
import org.coursera.lab.capstone.components.us.USRacingSuspension;
import org.coursera.lab.capstone.components.us.USRacingTires;

public class USConvertible extends Car {
    public USConvertible() {
        this(23000);
    }

    public USConvertible(int cost) {
        super("USConvertible", cost, new USRacingEngine(), new USRacingSuspension(),
                new USRacingTires());
    }
}
