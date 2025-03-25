package org.coursera.lab.capstone.cars.japan;

import org.coursera.lab.capstone.cars.Car;
import org.coursera.lab.capstone.components.japan.JapanSportEngine;
import org.coursera.lab.capstone.components.japan.JapanEconomySuspension;
import org.coursera.lab.capstone.components.japan.JapanSportTires;

public class JapanCoupe extends Car {
    public JapanCoupe() {
        this(15000);
    }

    public JapanCoupe(int cost) {
        super("JapanCoupe", cost, new JapanSportEngine(), new JapanEconomySuspension(),
                new JapanSportTires());
    }
}
