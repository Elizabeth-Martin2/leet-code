package org.coursera.lab.capstone;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assertions.assertSame;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import org.junit.jupiter.api.Test;

import org.coursera.lab.capstone.clock.Clock;
import org.coursera.lab.capstone.invoker.Invoker;
import org.coursera.lab.capstone.staff.Staff;
import org.coursera.lab.capstone.command.*;
import org.coursera.lab.capstone.cars.Car;
import org.coursera.lab.capstone.cars.us.*;
import org.coursera.lab.capstone.simulation.Simulation;


public class MainTest {   
    @Test
    public void capstoneTest() {
        Simulation s = new Simulation();
        s.run();
        assertTrue(s instanceof Simulation);
    }

    @Test
    public void testStaffStateTransition() {
        Staff ann = new Staff("Ann", 8, 12, 4);
        
        // Initially, staff should be NotIn.
        assertEquals("NotIn", ann.getCurrentStateName());

        // At time 8, Ann should move to Arriving.
        ann.updateState(8);
        assertEquals("Arriving", ann.getCurrentStateName());

        // At time 9, she should become Available.
        ann.updateState(9);
        assertEquals("Available", ann.getCurrentStateName());

        // At time 12, she should be in Lunch state.
        ann.updateState(12);
        assertEquals("Lunch", ann.getCurrentStateName());

        // At time 1 PM (represented as 1), she should return to Available.
        ann.updateState(1);
        assertEquals("Available", ann.getCurrentStateName());

        // At time 4 PM, she should be NotIn.
        ann.updateState(4);
        assertEquals("NotIn", ann.getCurrentStateName());
    }

    @Test
    public void testClockSingleton() {
        Clock clock1 = Clock.getInstance();
        Clock clock2 = Clock.getInstance();
        assertSame(clock1, clock2, "Clock should be a singleton instance");
    }

    @Test
    public void testClockTickAndReset() {
        Clock clock = Clock.getInstance();
        clock.reset(); // Reset to 8 AM.
        int firstTick = clock.tick();
        assertEquals(8, firstTick, "First tick should report 8 AM");
        int secondTick = clock.tick();
        assertEquals(9, secondTick, "Second tick should report 9 AM");
    }

    @Test
    public void testInvokerSelectsAvailableStaff() {
        // Create two staff members with different schedules.
        Staff ann = new Staff("Ann", 8, 12, 4);
        Staff bob = new Staff("Bob", 9, 1, 5);

        // Update their states:
        ann.updateState(9); // Ann: Available (arrived at 8).
        bob.updateState(8); // Bob: NotIn (arrival time is 9).

        Staff[] staffArray = { ann, bob };

        Invoker invoker = Invoker.getInstance(staffArray);
        Staff selected = invoker.getAvailableStaff();
        assertNotNull(selected, "There should be at least one available staff");
        assertEquals("Available", selected.getCurrentStateName());
        assertEquals("Ann", selected.getName(), "Ann should be chosen because Bob is not available");
    }

    @Test
    public void testCommandExecution() throws Exception {
        // Create a staff member and set her state to Available.
        Staff cal = new Staff("Cal", 10, 2, 6);
        cal.updateState(11); // For Cal, time 11 should be Available.
        
        Car car = new USSedan();
        int initialOrders = cal.getOrders();

        Command orderCommand = new OrderCarCommand(cal, car);
        orderCommand.execute();

        int ordersAfter = cal.getOrders();
        assertEquals(initialOrders + 1, ordersAfter, "Executing an order command should increment orders by 1");
    }
}

