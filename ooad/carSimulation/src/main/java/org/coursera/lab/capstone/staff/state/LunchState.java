package org.coursera.lab.capstone.staff.state;

/*
 * State pattern:
 *   Concrete class state for Lunch
 */
public class LunchState extends StaffState {
    @Override
    public boolean isAvailable() {
        return false;
    }

    @Override
    public String getStateName() {
        return "Lunch";
    }
}