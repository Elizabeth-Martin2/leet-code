package org.coursera.lab.abstractFactory.cars.us;

import org.coursera.lab.abstractFactory.cars.Car;
import org.coursera.lab.abstractFactory.strategy.TurnBehavior;
import org.coursera.lab.abstractFactory.strategy.SafetyHandling;
import org.coursera.lab.abstractFactory.components.us.USStandardEngine;
import org.coursera.lab.abstractFactory.components.us.USStandardSuspension;
import org.coursera.lab.abstractFactory.components.us.USStandardTires;

public class USSedan extends Car {
    public USSedan() {
        this(new SafetyHandling(), 13000);
    }

    public USSedan(TurnBehavior turnBehavior, int cost) {
        super("USSedan", cost, turnBehavior, new USStandardEngine(), new USStandardSuspension(), new USStandardTires());
    }
}
