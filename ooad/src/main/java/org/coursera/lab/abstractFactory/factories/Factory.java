package org.coursera.lab.abstractFactory.factories;

import org.coursera.lab.abstractFactory.cars.Car;

public interface Factory {
    Car createSedan();

    Car createCoupe();

    Car createConvertible();
}
