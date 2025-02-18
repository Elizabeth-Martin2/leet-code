package org.coursera.lab.abstractFactory.cars.japan;

import org.coursera.lab.abstractFactory.cars.Car;
import org.coursera.lab.abstractFactory.strategy.TurnBehavior;
import org.coursera.lab.abstractFactory.strategy.SportHandling;
import org.coursera.lab.abstractFactory.components.japan.JapanSportEngine;
import org.coursera.lab.abstractFactory.components.japan.JapanEconomySuspension;
import org.coursera.lab.abstractFactory.components.japan.JapanSportTires;

public class JapanCoupe extends Car {
    public JapanCoupe() {
        this(new SportHandling(), 15000);
    }

    public JapanCoupe(TurnBehavior turnBehavior, int cost) {
        super("JapanCoupe", cost, turnBehavior, new JapanSportEngine(), new JapanEconomySuspension(),
                new JapanSportTires());
    }
}
