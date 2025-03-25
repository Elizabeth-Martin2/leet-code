package org.coursera.lab.capstone.factories;

import org.coursera.lab.capstone.cars.Car;

public interface Factory {
    Car createSedan();

    Car createCoupe();

    Car createConvertible();
}
