package org.coursera.lab.CarFactory;

/**
 * TurnBehavior: Strategy interface for handling turn behavior
 */
public interface TurnBehavior {
    void turn();
}

/**
 * Strategy classes to override turn behavior based on car type
 */
class SafetyHandling implements TurnBehavior {
    @Override
    public void turn() {
        System.out.println("eases through turn");
    }
}

class SportHandling implements TurnBehavior {
    @Override
    public void turn() {
        System.out.println("makes a right turn");
    }
}

class RacingHandling implements TurnBehavior {
    @Override
    public void turn() {
        System.out.println("skids through turn");
    }
}