package org.coursera.lab.abstractFactory.cars.japan;

import org.coursera.lab.abstractFactory.cars.Car;
import org.coursera.lab.abstractFactory.strategy.TurnBehavior;
import org.coursera.lab.abstractFactory.strategy.RacingHandling;
import org.coursera.lab.abstractFactory.components.japan.JapanSportEngine;
import org.coursera.lab.abstractFactory.components.japan.JapanSportSuspension;
import org.coursera.lab.abstractFactory.components.japan.JapanSportTires;

public class JapanConvertible extends Car{
    public JapanConvertible() {
        this(new RacingHandling(), 20000);
    }

    public JapanConvertible(TurnBehavior turnBehavior, int cost) {
        super("JapanConvertible", cost, turnBehavior, new JapanSportEngine(), new JapanSportSuspension(),
                new JapanSportTires());
    }
}
