package org.coursera.lab.abstractFactory.factories;

import org.coursera.lab.abstractFactory.cars.Car;
import org.coursera.lab.abstractFactory.cars.japan.JapanSedan;
import org.coursera.lab.abstractFactory.cars.japan.JapanCoupe;
import org.coursera.lab.abstractFactory.cars.japan.JapanConvertible;

public class JapanFactory implements Factory {
    @Override
    public Car createSedan() {
        return new JapanSedan();
    }

    @Override
    public Car createCoupe() {
        return new JapanCoupe();
    }

    @Override
    public Car createConvertible() {
        return new JapanConvertible();
    }
}
