package org.coursera.lab.capstone.command;

import org.coursera.lab.capstone.cars.Car;
import org.coursera.lab.capstone.staff.Staff;

/*
 * Command Pattern:
 * This is the concrete command to execute servicing a car
 */
public class ServiceCarCommand implements Command {
    private Staff staff;
    private Car car;

    public ServiceCarCommand(Staff staff, Car car) {
        this.staff = staff;
        this.car = car;
    }

    @Override
    public void execute() {
        staff.serviceCar(car);
    }
}