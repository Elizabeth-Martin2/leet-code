package org.coursera.lab.capstone.staff.state;

/*
 * State pattern:
 *   Concrete class state for Arriving
 */
public class ArrivingState extends StaffState {
    @Override
    public boolean isAvailable() {
        return true;
    }

    @Override
    public String getStateName() {
        return "Arriving";
    }
}