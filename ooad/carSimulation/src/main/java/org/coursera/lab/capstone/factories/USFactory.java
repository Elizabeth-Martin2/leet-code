package org.coursera.lab.capstone.factories;

import org.coursera.lab.capstone.cars.Car;
import org.coursera.lab.capstone.cars.us.USSedan;
import org.coursera.lab.capstone.cars.us.USCoupe;
import org.coursera.lab.capstone.cars.us.USConvertible;

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
