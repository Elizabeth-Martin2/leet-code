package org.coursera.lab.capstone.staff;

/*
 * Observer pattern:
 *   Interface to be implemented by Staff to get time notifications
 */
public interface Observer {
    void update(int currentTime);
}