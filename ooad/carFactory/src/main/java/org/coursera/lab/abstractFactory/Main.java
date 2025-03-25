package org.coursera.lab.abstractFactory;

import org.coursera.lab.abstractFactory.cars.Car;
import org.coursera.lab.abstractFactory.factories.*;
import org.coursera.lab.abstractFactory.decorators.*;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {      
        // Create Factories
        Factory usFactory = new USFactory();
        Factory japanFactory = new JapanFactory();

        // Create a List to Store Cars
        List<Car> cars = new ArrayList<>();

        // Create US Cars (Sedan, Coupe, Convertible)
        Car usSedan = usFactory.createSedan();
        Car usCoupe = usFactory.createCoupe();
        Car usConvertible = usFactory.createConvertible();

        cars.add(usSedan);
        cars.add(usCoupe);
        cars.add(usConvertible);

        // Create Japanese Cars (Sedan, Coupe, Convertible)
        Car japanSedan = japanFactory.createSedan();
        Car japanCoupe = japanFactory.createCoupe();
        Car japanConvertible = japanFactory.createConvertible();

        cars.add(japanSedan);
        cars.add(japanCoupe);
        cars.add(japanConvertible);

        // Decorate a Convertible (as per assignment example)
        Car decoratedConvertible = usFactory.createConvertible();
        decoratedConvertible = new UndercoatDecorator(decoratedConvertible);
        decoratedConvertible = new SeatCoverDecorator(decoratedConvertible);
        decoratedConvertible = new SeatCoverDecorator(decoratedConvertible);
        decoratedConvertible = new ServiceDecorator(decoratedConvertible);
        decoratedConvertible = new ServiceDecorator(decoratedConvertible);

        cars.add(decoratedConvertible);

        // Display Information for Each Car
        System.out.println("🚗 Car Factory Output:");
        for (Car car : cars) {
            System.out.println("Name: " + car.getName());
            System.out.println("Cost: $" + car.getCost());
            System.out.println("Components: " + car.getComponents());
            System.out.println("---------------------------");
        }
    }
}