package org.coursera.lab.abstractFactory.decorators;

import org.coursera.lab.abstractFactory.cars.Car;

public class UndercoatDecorator extends CarDecorator {
    public UndercoatDecorator(Car car) {
        super(car);
    }

    @Override
    public String getName() {
        return decoratedCar.getName() + " (add undercoat)";
    }

    @Override
    public int getCost() {
        return decoratedCar.getCost() + 500;
    }
}
