package org.coursera.lab.capstone.cars;

import org.coursera.lab.capstone.components.Engine;
import org.coursera.lab.capstone.components.Suspension;
import org.coursera.lab.capstone.components.Tires;

public abstract class Car {
    protected String type;
    protected String name;
    protected Engine engine;
    protected Suspension suspension;
    protected Tires tires;
    protected int cost;
    private static int carCounter = 0;

    protected Car(String type, int baseCost, Engine engine, Suspension suspension,
            Tires tires) {
        carCounter++;
        this.type = type;
        this.name = type + " " + carCounter;
        this.cost = baseCost;
        this.engine = engine;
        this.suspension = suspension;
        this.tires = tires;
    }

    public static void resetCarCounter() {
        carCounter = 0;
    }

    public String getName() {
        return name;
    }

    public int getCost() {
        return cost;
    }

    public String getComponents() {
        return engine.getInfo() + ", " + suspension.getInfo() + ", " + tires.getInfo();
    }

    public Engine getEngine() {
        return engine;
    }

    public Tires getTires() {
        return tires;
    }

    public Suspension getSuspension() {
        return suspension;
    }
}
