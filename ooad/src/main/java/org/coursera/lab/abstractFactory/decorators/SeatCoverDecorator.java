package org.coursera.lab.abstractFactory.decorators;

import org.coursera.lab.abstractFactory.cars.Car;

public class SeatCoverDecorator extends CarDecorator {
    public SeatCoverDecorator(Car car) {
        super(car);
    }

    @Override
    public String getName() {
        return decoratedCar.getName() + " (add seat cover)";
    }

    @Override
    public int getCost() {
        return decoratedCar.getCost() + 250;
    }
}
