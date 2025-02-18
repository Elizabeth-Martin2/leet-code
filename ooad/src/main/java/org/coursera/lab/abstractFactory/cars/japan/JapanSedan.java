package org.coursera.lab.abstractFactory.cars.japan;

import org.coursera.lab.abstractFactory.cars.Car;
import org.coursera.lab.abstractFactory.strategy.TurnBehavior;
import org.coursera.lab.abstractFactory.strategy.SafetyHandling;
import org.coursera.lab.abstractFactory.components.japan.JapanEconomyEngine;
import org.coursera.lab.abstractFactory.components.japan.JapanEconomySuspension;
import org.coursera.lab.abstractFactory.components.japan.JapanEconomyTires;

public class JapanSedan extends Car{
    public JapanSedan() {
        this(new SafetyHandling(), 10000);
    }

    public JapanSedan(TurnBehavior turnBehavior, int cost) {
        super("JapanSedan", cost, turnBehavior, new JapanEconomyEngine(), new JapanEconomySuspension(),
                new JapanEconomyTires());
    }
}
