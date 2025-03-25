package org.coursera.lab.capstone.staff;

import org.coursera.lab.capstone.cars.Car;
import org.coursera.lab.capstone.staff.state.*;

/*
 * Command & Observer Patterns:
 * The staff class acts as the receiver processing orders / servicing cars
 * Every tick of the clock notifies the staff so they update their state
 */
public class Staff implements Observer {
    private String name;
    private int orders, services, sales;
    private double bonus;
    private int arrivalTime, lunchTime, leaveTime;
    private StaffState currentState;

    public Staff(String name, int arrivalTime, int lunchTime, int leaveTime) {
        this.name = name;
        this.arrivalTime = arrivalTime;
        this.lunchTime = lunchTime;
        this.leaveTime = leaveTime;
        this.currentState = new NotInState();
    }

    // Action methods (commands)
    public void orderCar(Car car) {
        System.out.println(name + " is ordering " + car.getName());
        orders++;
        bonus += car.getCost() * 0.03; // 3% bonus
    }

    public void serviceCar(Car car) {
        System.out.println(name + " is servicing " + car.getName());
        services++;
        bonus += car.getCost() * 0.01; // 1% bonus
    }

    public void buyCar(Car car) {
        System.out.println(name + " is selling " + car.getName() + " for $" + car.getCost());
        sales++;
        bonus += car.getCost() * 0.02; // 2% bonus
    }

    public void printSummary() {
        System.out.println(name + ":");
        System.out.println(" Orders: " + orders);
        System.out.println(" Services: " + services);
        System.out.println(" Sales: " + sales);
        System.out.println(" Bonus: $" + bonus);
    }

    // Getters and state helpers
    public String getName() {
        return name;
    }

    public int getArrivalTime() {
        return arrivalTime;
    }

    public int getLunchTime() {
        return lunchTime;
    }

    public int getLeaveTime() {
        return leaveTime;
    }

    public int getOrders() {
        return this.orders;
    }

    public int getServices() {
        return this.services;
    }

    public int getSales() {
        return this.sales;
    }

    public double getBonus() {
        return this.bonus;
    }

    public boolean isAvailable() {
        return currentState.isAvailable();
    }

    public String getCurrentStateName() {
        return currentState.getStateName();
    }

    public void setState(StaffState state) {
        this.currentState = state;
    }

    // Observer update method – called by the Clock each tick.
    @Override
    public void update(int currentTime) {
        updateState(currentTime);
    }

    // Determine new state based on the current time and the staff's schedule.
    // A helper method to convert our clock times to a comparable 24-hour style
    // integer.
    public static int mapTime(int time) {
        // Times 8-12 are morning; 1-7 are afternoon (add 12 to map them to 13-19).
        if (time >= 8 && time <= 12)
            return time;
        else
            return time + 12;
    }

    // Formats time for output (AM/PM).
    public static String formatTime(int time) {
        if (time >= 8 && time <= 12)
            return time + " AM";
        else
            return time + " PM";
    }

    // Update state based on current time.
    public void updateState(int currentTime) {
        int mappedCurrent = mapTime(currentTime);
        int mappedArrival = mapTime(arrivalTime);
        int mappedLunch = mapTime(lunchTime);
        int mappedLeave = mapTime(leaveTime);
        StaffState newState;
        
        if (mappedCurrent < mappedArrival || mappedCurrent >= mappedLeave) {
            newState = new NotInState();
        } else if (mappedCurrent == mappedArrival) {
            newState = new ArrivingState();
        } else if (mappedCurrent == mappedLunch) {
            newState = new LunchState();
        } else {
            newState = new AvailableState();
        }
        
        if (!newState.getStateName().equals(currentState.getStateName())) {
            System.out.println(name + " moved to " + newState.getStateName() + " at " + formatTime(currentTime));
            currentState = newState;
        }
    }
}
