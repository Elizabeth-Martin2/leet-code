package org.coursera.lab.abstractFactory.cars;

import org.coursera.lab.abstractFactory.components.Engine;
import org.coursera.lab.abstractFactory.components.Suspension;
import org.coursera.lab.abstractFactory.components.Tires;
import org.coursera.lab.abstractFactory.strategy.TurnBehavior;

public abstract class Car {
    protected String type;
    protected String name;
    protected Engine engine;
    protected Suspension suspension;
    protected Tires tires;
    protected int cost;
    protected TurnBehavior turnBehavior; // This is the strategy pattern attribute
    private static int carCounter = 0;


    protected Car(String type, int baseCost, TurnBehavior turnBehavior, Engine engine, Suspension suspension, Tires tires) {
        carCounter++;
        this.type = type;
        this.name = type + " " + carCounter;
        this.cost = baseCost;
        this.turnBehavior = turnBehavior;
        this.engine = engine;
        this.suspension = suspension;
        this.tires = tires;
    }

    public static void resetCarCounter() {
        carCounter = 0;
    }

    public void setTurnBehavior(TurnBehavior turnBehavior) {
        this.turnBehavior = turnBehavior;
    }

    public TurnBehavior getTurnBehavior(){
        return turnBehavior;
    }

    public void handle() {
        turnBehavior.turn();
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