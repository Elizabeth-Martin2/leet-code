package org.coursera.lab.capstone.simulation;

import org.coursera.lab.capstone.factories.*;
import org.coursera.lab.capstone.staff.Staff;
import org.coursera.lab.capstone.invoker.Invoker;
import org.coursera.lab.capstone.cars.Car;
import org.coursera.lab.capstone.command.*;
import org.coursera.lab.capstone.clock.Clock;

import java.util.Random;

/*
 * Command Pattern:
 * The simulation class acts as the client setting up & excuting commands
 */
public class Simulation {
    private Factory usFactory = new USFactory();
    private Factory japanFactory = new JapanFactory();
    private Staff[] staff = {
            new Staff("Ann", 8, 12, 4),
            new Staff("Bob", 9, 1, 5),
            new Staff("Cal", 10, 2, 6),
            new Staff("Deb", 11, 3, 7)
    };
    
    private Invoker invoker = Invoker.getInstance(staff);
    private Random rand = new Random();

    public void run() {
        Clock clock = Clock.getInstance();
        for (Staff s : staff) {
            clock.registerObserver(s);
        }
        
        // Simulate 10 days.
        for (int day = 1; day <= 10; day++) {
            System.out.println("Day " + day + ":");
            clock.reset();
            
            for (int i = 0; i < 12; i++) {
                int currentTime = clock.tick();
                if (currentTime != 7) {
                    Car car = getRandomCar();
                    Staff availableStaff = invoker.getAvailableStaff();
                    Command command = getRandomCommand(availableStaff, car);
                    invoker.executeCommand(command);
                }
            }
            System.out.println();
        }
        System.out.println("Final Summary:");
        for (Staff s : staff) {
            s.printSummary();
        }
    }

    private Car getRandomCar() {
        int choice = rand.nextInt(6);
        switch (choice) {
            case 0:
                return usFactory.createSedan();
            case 1:
                return usFactory.createCoupe();
            case 2:
                return usFactory.createConvertible();
            case 3:
                return japanFactory.createSedan();
            case 4:
                return japanFactory.createCoupe();
            case 5:
                return japanFactory.createConvertible();
            default:
                return usFactory.createSedan();
        }
    }

    private Command getRandomCommand(Staff staff, Car car) {
        int action = rand.nextInt(3);
        switch (action) {
            case 0:
                return new OrderCarCommand(staff, car);
            case 1:
                return new ServiceCarCommand(staff, car);
            default:
                return new BuyCarCommand(staff, car);
        }
    }
}
