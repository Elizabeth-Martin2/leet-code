package org.coursera.lab.abstractFactory.strategy;

public class RacingHandling implements TurnBehavior {
    @Override
    public void turn() {
        System.out.println("skids through turn");
    }
}