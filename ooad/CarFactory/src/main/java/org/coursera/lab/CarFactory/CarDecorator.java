package org.coursera.lab.CarFactory;

// This is the abstract base decorator for Car
// The decorator pattern works by wrapping Car objects inside the decorator
public abstract class CarDecorator extends Car {
    protected Car decoratedCar; // This is the car object to be decorated

    // Decorates (wraps) the car object
    public CarDecorator(Car car) {
        super(car.type, car.cost, car.turnBehavior);
        this.decoratedCar = car;
    }

    // Decorator pattern extends functionality of getName()
    @Override
    public String getName() {
        return decoratedCar.getName();
    }

    // Decorator pattern extends functionality of getCost()
    @Override
    public int getCost() {
        return decoratedCar.getCost();
    }

    // Decorator pattern does not modify, but delegates to oringal car handle()
    @Override
    public void handle() {
        decoratedCar.handle();
    }
}

// Concrete decorator to add undercoat feature to car
class UndercoatDecorator extends CarDecorator {
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

// Concrete decorator to add seatcover feature to car
class SeatCoverDecorator extends CarDecorator {
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

// Concrete decorator to add service visit to car
class ServiceDecorator extends CarDecorator {
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