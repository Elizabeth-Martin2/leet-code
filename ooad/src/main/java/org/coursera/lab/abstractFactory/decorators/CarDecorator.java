package org.coursera.lab.abstractFactory.decorators;

import org.coursera.lab.abstractFactory.cars.Car;

public abstract class CarDecorator extends Car {
    protected Car decoratedCar;

    public CarDecorator(Car car) {
        super(car.getName(), car.getCost(), car.getTurnBehavior(), car.getEngine(), car.getSuspension(),
                car.getTires());
        this.decoratedCar = car;
    }

    @Override
    public String getName() {
        return decoratedCar.getName();
    }

    @Override
    public int getCost() {
        return decoratedCar.getCost();
    }

    @Override
    public void handle() {
        decoratedCar.handle();
    }
}
