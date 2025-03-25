package org.coursera.lab.capstone.staff.state;

/*
 * State pattern:
 *   StaffState acts as abstract class for other states
 */
public abstract class StaffState {
    public abstract boolean isAvailable();

    public abstract String getStateName();
}