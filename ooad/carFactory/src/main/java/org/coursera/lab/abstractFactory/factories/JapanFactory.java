package org.coursera.lab.abstractFactory.factories;

import org.coursera.lab.abstractFactory.cars.Car;
import org.coursera.lab.abstractFactory.cars.japan.JapanSedan;
import org.coursera.lab.abstractFactory.cars.japan.JapanCoupe;
import org.coursera.lab.abstractFactory.cars.japan.JapanConvertible;

/**
 * Japan Concrete Factory: JapanFactory
 * Implements the abstract factory Factory to produce Japan-specific cars
 * Ensures that all cars produced use Japan equipment
 */
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
