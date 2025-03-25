package org.coursera.lab.capstone.cars.japan;

import org.coursera.lab.capstone.cars.Car;
import org.coursera.lab.capstone.components.japan.JapanSportEngine;
import org.coursera.lab.capstone.components.japan.JapanSportSuspension;
import org.coursera.lab.capstone.components.japan.JapanSportTires;

public class JapanConvertible extends Car {
    public JapanConvertible() {
        this(20000);
    }

    public JapanConvertible(int cost) {
        super("JapanConvertible", cost, new JapanSportEngine(), new JapanSportSuspension(),
                new JapanSportTires());
    }
}
