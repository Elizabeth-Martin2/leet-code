package org.coursera.lab.abstractFactory.strategy;

public class SafetyHandling implements TurnBehavior {
    @Override
    public void turn() {
        System.out.println("eases through turn");
    }
}