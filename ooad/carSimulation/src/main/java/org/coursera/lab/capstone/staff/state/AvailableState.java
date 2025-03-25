package org.coursera.lab.capstone.staff.state;

/*
 * State pattern:
 *   Concrete class state for Available
 */
public class AvailableState extends StaffState {
    @Override
    public boolean isAvailable() {
        return true;
    }

    @Override
    public String getStateName() {
        return "Available";
    }
}