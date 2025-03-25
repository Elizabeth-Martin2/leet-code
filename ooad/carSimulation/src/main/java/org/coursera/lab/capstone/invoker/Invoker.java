package org.coursera.lab.capstone.invoker;

import org.coursera.lab.capstone.staff.Staff;
import org.coursera.lab.capstone.command.Command;
import java.util.Random;

/*
 * Command & Singleton Pattern:
 * The invoker class handles executing commands
 * Only one invoker instance allowed 
 * Initialized when required (lazy)
 */
public class Invoker {
    private Staff[] staffMembers;
    private static Invoker instance = null;
    private Random rand = new Random();

    private Invoker(Staff[] staffMembers) {
        this.staffMembers = staffMembers;
    }

    public static Invoker getInstance(Staff[] staffMembers) {
        if (instance == null) {
            instance = new Invoker(staffMembers);
        }
        return instance;
    }

    public void executeCommand(Command command) {
        command.execute();
    }

    // Returns the first available staff starting from a random index.
    public Staff getAvailableStaff() {
        int n = staffMembers.length;
        int start = rand.nextInt(n);
        for (int i = 0; i < n; i++) {
            int index = (start + i) % n;
            Staff s = staffMembers[index];
            if (s.isAvailable()) {
                return s;
            } else {
                System.out.println("Sorry, " + s.getName() + " is " + s.getCurrentStateName());
            }
        }
        return null;
    }
}