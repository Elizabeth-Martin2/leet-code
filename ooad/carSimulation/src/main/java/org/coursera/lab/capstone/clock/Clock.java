package org.coursera.lab.capstone.clock;

import java.util.ArrayList;
import java.util.List;
import org.coursera.lab.capstone.staff.Observer;

/*
 * Singleton pattern:
 *   Only one clock implementation allowed
 *   Instance initialized with class definition (eager)
 */
public class Clock {
    private static final Clock instance = new Clock();
    private int currentTime;
    private List<Observer> observers;

    private Clock() {
        currentTime = 8;
        observers = new ArrayList<>();
    }

    public static Clock getInstance() {
        return instance;
    }

    public void registerObserver(Observer o) {
        observers.add(o);
    }

    public void removeObserver(Observer o) {
        observers.remove(o);
    }

    // Notify all observers (the staff) with the current time.
    public void notifyObservers() {
        for (Observer o : observers) {
            o.update(currentTime);
        }
    }

    // Tick the clock: announce the time, notify observers, then increment time.
    // Returns the time value that was just processed.
    public int tick() {
        int timeToReport = currentTime;
        System.out.println("Time now: " + formatTime(timeToReport));
        notifyObservers();

        if (currentTime == 12)
            currentTime = 1;
        else if (currentTime == 7)
            currentTime = 8; // end of day: next tick resets to 8 (for simulation, reset each day)
        else
            currentTime++;
        return timeToReport;
    }

    public void reset() {
        currentTime = 8;
    }

    private String formatTime(int time) {
        if (time >= 8 && time <= 12)
            return time + " AM";
        else
            return time + " PM";
    }
}
