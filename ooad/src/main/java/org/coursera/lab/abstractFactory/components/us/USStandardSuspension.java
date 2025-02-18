package org.coursera.lab.abstractFactory.components.us;

import org.coursera.lab.abstractFactory.components.Suspension;

public class USStandardSuspension implements Suspension {
    public String getInfo() {
        return "Standard Suspension";
    }
}