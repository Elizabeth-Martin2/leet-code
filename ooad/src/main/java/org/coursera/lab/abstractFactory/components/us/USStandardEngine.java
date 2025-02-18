package org.coursera.lab.abstractFactory.components.us;

import org.coursera.lab.abstractFactory.components.Engine;

public class USStandardEngine implements Engine {
    public String getInfo() {
        return "Standard Engine";
    }
}
