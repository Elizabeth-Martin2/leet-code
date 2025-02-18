package org.coursera.lab.abstractFactory.cars.us;

import org.coursera.lab.abstractFactory.cars.Car;
import org.coursera.lab.abstractFactory.strategy.TurnBehavior;
import org.coursera.lab.abstractFactory.strategy.SportHandling;
import org.coursera.lab.abstractFactory.components.us.USStandardEngine;
import org.coursera.lab.abstractFactory.components.us.USRacingSuspension;
import org.coursera.lab.abstractFactory.components.us.USRacingTires;

public class USCoupe extends Car {
    public USCoupe() {
        this(new SportHandling(), 18000);
    }

    public USCoupe(TurnBehavior turnBehavior, int cost) {
        super("USCoupe", cost, turnBehavior, new USStandardEngine(), new USRacingSuspension(), new USRacingTires());
    }
}
