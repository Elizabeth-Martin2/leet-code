package org.coursera.lab.abstractFactory.factories;

import org.coursera.lab.abstractFactory.cars.Car;

/** Abstract factory interface:
 Defines a common interface for all factories
 Concrete factories (USFactory and JapanFactory) will implement this
 */
public interface Factory {
    Car createSedan();

    Car createCoupe();

    Car createConvertible();
}
