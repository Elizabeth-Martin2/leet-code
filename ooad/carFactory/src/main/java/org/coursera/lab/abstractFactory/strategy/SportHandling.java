package org.coursera.lab.abstractFactory.strategy;

public class SportHandling implements TurnBehavior {
    @Override
    public void turn() {
        System.out.println("makes a right turn");
    }
}
