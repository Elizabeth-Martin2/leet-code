package org.coursera.lab.capstone.factories;

import org.coursera.lab.capstone.cars.Car;
import org.coursera.lab.capstone.cars.japan.JapanSedan;
import org.coursera.lab.capstone.cars.japan.JapanCoupe;
import org.coursera.lab.capstone.cars.japan.JapanConvertible;

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
