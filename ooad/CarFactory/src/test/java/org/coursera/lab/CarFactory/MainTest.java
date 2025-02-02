package org.coursera.lab.CarFactory;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class MainTest {
    @BeforeEach
    public void resetCarCounter() {
        Car.carCounter = 0;
    }

    @Test
    public void decoratorTest() {
        assertTrue(true);
    }

    // Test that base car costs are correct 
    @Test
    public void testBaseCarCosts() {
        Car sedan = new Sedan();
        assertEquals(10000, sedan.getCost(), "Sedan base cost is incorrect");

        Car coupe = new Coupe();
        assertEquals(15000, coupe.getCost(), "Coupe base cost is incorrect");

        Car convertible = new Convertible();
        assertEquals(20000, convertible.getCost(), "Convertible base cost is incorrect");
    }

    //Test that handling behavior is correct for each car type
    @Test
    public void testHandlingBehavior(){
        Car sedan = new Sedan();
        Car coupe = new Coupe();
        Car convertible = new Convertible();

        assertTrue(sedan.turnBehavior instanceof SafetyHandling, "Sedan should have safety handling");
        assertTrue(coupe.turnBehavior instanceof SportHandling, "Coupe should have sport handling");
        assertTrue(convertible.turnBehavior instanceof RacingHandling, "Convertible should have racing handling");
    }

    // Test decorators are modifying cost correctly
    @Test
    public void testDecoratorsModifyCost() {
        Car car = new Convertible();
        car = new UndercoatDecorator(car);
        car = new SeatCoverDecorator(car);
        car = new SeatCoverDecorator(car);
        car = new ServiceDecorator(car);
        car = new ServiceDecorator(car);

        assertEquals(21800, car.getCost(), "Cost calculation with decorations failed");
    }

    // Test decorators are modifying the name correctly
    @Test
    public void testDecoratorsModifyName() {
        Car car = new Coupe();
        car = new UndercoatDecorator(car);
        car = new SeatCoverDecorator(car);
        car = new ServiceDecorator(car);

        String expectedName = "Coupe 1 (add undercoat) (add seat cover) (add service visit)";
        assertEquals(expectedName, car.getName(), "Name concatenation with decorations failed");
    }

    // Test changing handling behavior dynamically
    @Test
    public void testChangeHandlingBehavior() {
        Car car = new Sedan();
        car.setTurnBehavior(new RacingHandling());

        assertTrue(car.turnBehavior instanceof RacingHandling, "Handling behavior did not change correctly");
    }
}