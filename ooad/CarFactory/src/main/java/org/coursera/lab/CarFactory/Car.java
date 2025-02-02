package org.coursera.lab.CarFactory;

public abstract class Car {
    protected String type;
    protected String name;
    protected int cost;
    protected TurnBehavior turnBehavior; // This is the strategy pattern attribute
    protected static int carCounter = 0;

    Car(String type, int baseCost, TurnBehavior turnBehavior) {
        carCounter++;
        this.type = type;
        this.name = type + " " + carCounter;
        this.cost = baseCost;
        this.turnBehavior = turnBehavior;
    }

    public void setTurnBehavior(TurnBehavior turnBehavior) {
        this.turnBehavior = turnBehavior;
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
}

// Extended car classes for Coupe, Sedan, & Convertibles
// Updates for assignment 2: Constructor chaining for flexibility without
// redundancy
class Coupe extends Car {
    public Coupe() {
        this(new SportHandling(), 15000);
    }

    public Coupe(TurnBehavior turnBehavior) {
        this(turnBehavior, 15000);
    }

    public Coupe(TurnBehavior turnBehavior, int cost) {
        super("Coupe", cost, turnBehavior);
    }
}

class Sedan extends Car {
    public Sedan() {
        this(new SafetyHandling(), 10000);
    }

    public Sedan(TurnBehavior turnBehavior) {
        this(turnBehavior, 10000);
    }

    public Sedan(TurnBehavior turnBehavior, int cost) {
        super("Sedan", cost, turnBehavior);
    }
}

class Convertible extends Car {
    public Convertible() {
        this(new RacingHandling(), 20000);
    }

    public Convertible(TurnBehavior turnBehavior) {
        this(turnBehavior, 20000);
    }

    public Convertible(TurnBehavior turnBehavior, int cost) {
        super("Convertible", cost, turnBehavior);
    }
}