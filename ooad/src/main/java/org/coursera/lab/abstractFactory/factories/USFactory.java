package org.coursera.lab.abstractFactory.factories;

import org.coursera.lab.abstractFactory.cars.Car;
import org.coursera.lab.abstractFactory.cars.us.USSedan;
import org.coursera.lab.abstractFactory.cars.us.USCoupe;
import org.coursera.lab.abstractFactory.cars.us.USConvertible;

public class USFactory implements Factory {
    @Override
    public Car createSedan() {
        return new USSedan();
    }

    @Override
    public Car createCoupe() {
        return new USCoupe();
    }

    @Override
    public Car createConvertible() {
        return new USConvertible();
    }
}
