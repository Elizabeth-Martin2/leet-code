package org.coursera.lab.capstone.command;

/**
 * Command Pattern:
 *   This is the interface that represents the abstract command to be executed
 *   Will be overridden by the concrete commands for ordering, servicing, and buying
 */
public interface Command {
    void execute();
}
