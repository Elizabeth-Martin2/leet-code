package org.coursera.lab.abstractFactory.decorators;

import org.coursera.lab.abstractFactory.cars.Car;

public class ServiceDecorator extends CarDecorator {
    public ServiceDecorator(Car car) {
        super(car);
    }

    @Override
    public String getName() {
        return decoratedCar.getName() + " (add service visit)";
    }

    @Override
    public int getCost() {
        return decoratedCar.getCost() + 400;
    }
}
