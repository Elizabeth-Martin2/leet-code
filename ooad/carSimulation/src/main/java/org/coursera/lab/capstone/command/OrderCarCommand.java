package org.coursera.lab.capstone.command;

import org.coursera.lab.capstone.cars.Car;
import org.coursera.lab.capstone.staff.Staff;

/**
 * Command Pattern: 
 * This is the concrete command to execute ordering a car
 */
public class OrderCarCommand implements Command {
    private Staff staff;
    private Car car;

    public OrderCarCommand(Staff staff, Car car) {
        this.staff = staff;
        this.car = car;
    }

    @Override
    public void execute() {
        staff.orderCar(car);
    }
}
