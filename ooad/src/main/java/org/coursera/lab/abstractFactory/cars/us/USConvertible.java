package org.coursera.lab.abstractFactory.cars.us;

import org.coursera.lab.abstractFactory.cars.Car;
import org.coursera.lab.abstractFactory.strategy.TurnBehavior;
import org.coursera.lab.abstractFactory.strategy.RacingHandling;
import org.coursera.lab.abstractFactory.components.us.USRacingEngine;
import org.coursera.lab.abstractFactory.components.us.USRacingSuspension;
import org.coursera.lab.abstractFactory.components.us.USRacingTires;

public class USConvertible extends Car {
    public USConvertible() {
        this(new RacingHandling(), 23000);
    }

    public USConvertible(TurnBehavior turnBehavior, int cost) {
        super("USConvertible", cost, turnBehavior, new USRacingEngine(), new USRacingSuspension(),
                new USRacingTires());
    }
}
