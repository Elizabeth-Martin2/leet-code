package org.coursera.lab.CarFactory;
import java.util.ArrayList;


public class Main {
	public static void main(String[] args) {
        ArrayList<Car> cars = new ArrayList<Car>();
        
        // Example 1: No additions
        Car sedan = new Sedan();
        cars.add(sedan); 

        // Example 2: Add undercoat
        Car coupe = new Coupe();
        coupe = new UndercoatDecorator(coupe);
        cars.add(coupe); 

        // Example 3: Add undercoat, seat covers x 2, service x 2
        Car convertible = new Convertible();
        convertible = new UndercoatDecorator(convertible);
        convertible = new SeatCoverDecorator(convertible);
        convertible = new SeatCoverDecorator(convertible);
        convertible = new ServiceDecorator(convertible);
        convertible = new ServiceDecorator(convertible);
        cars.add(convertible); 

        for (Car c : cars) {
            System.out.println("Name: " + c.getName());
            System.out.println("Cost: " + c.getCost());
            System.out.println("Handling: ");
            c.handle();
            System.out.println("--------------------------");
        }
    }
}

