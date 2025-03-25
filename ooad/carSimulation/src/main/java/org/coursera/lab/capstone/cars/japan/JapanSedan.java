package org.coursera.lab.capstone.cars.japan;

import org.coursera.lab.capstone.cars.Car;
import org.coursera.lab.capstone.components.japan.JapanEconomyEngine;
import org.coursera.lab.capstone.components.japan.JapanEconomySuspension;
import org.coursera.lab.capstone.components.japan.JapanEconomyTires;

public class JapanSedan extends Car {
    public JapanSedan() {
        this(10000);
    }

    public JapanSedan(int cost) {
        super("JapanSedan", cost, new JapanEconomyEngine(), new JapanEconomySuspension(),
                new JapanEconomyTires());
    }
}
