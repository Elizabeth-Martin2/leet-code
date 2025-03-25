package org.coursera.lab.capstone.staff.state;

/*
 * State pattern:
 *   Concrete class state for NotIn
 */
public class NotInState extends StaffState {
    @Override
    public boolean isAvailable() {
        return false;
    }

    @Override
    public String getStateName() {
        return "NotIn";
    }
}
