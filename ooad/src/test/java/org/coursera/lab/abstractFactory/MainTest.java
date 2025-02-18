package org.coursera.lab.abstractFactory;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.coursera.lab.abstractFactory.cars.Car;
import org.coursera.lab.abstractFactory.factories.*;
import org.coursera.lab.abstractFactory.components.*;
import org.coursera.lab.abstractFactory.decorators.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class MainTest {

    private Factory usFactory;
    private Factory japanFactory;

    @BeforeEach
    public void setUp() {
        // Reset factories & count before each test
        Car.resetCarCounter();
        usFactory = new USFactory();
        japanFactory = new JapanFactory();
    }

    // Test 1: Verify Car Creation From US Factory
    @Test
    public void testUSFactoryCarCreation() {
        Car sedan = usFactory.createSedan();
        Car coupe = usFactory.createCoupe();
        Car convertible = usFactory.createConvertible();

        assertEquals("USSedan 1", sedan.getName());
        assertEquals(13000, sedan.getCost());

        assertEquals("USCoupe 2", coupe.getName());
        assertEquals(18000, coupe.getCost());

        assertEquals("USConvertible 3", convertible.getName());
        assertEquals(23000, convertible.getCost());
    }

    // Test 2: Verify Car Creation From Japan Factory
    @Test
    public void testJapanFactoryCarCreation() {
        Car sedan = japanFactory.createSedan();
        Car coupe = japanFactory.createCoupe();
        Car convertible = japanFactory.createConvertible();

        assertEquals("JapanSedan 1", sedan.getName());
        assertEquals(10000, sedan.getCost());

        assertEquals("JapanCoupe 2", coupe.getName());
        assertEquals(15000, coupe.getCost());

        assertEquals("JapanConvertible 3", convertible.getName());
        assertEquals(20000, convertible.getCost());
    }

    // Test 3: Verify Decorators Modify Cost & Name
    @Test
    public void testCarDecorators() {
        Car convertible = usFactory.createConvertible();
        convertible = new UndercoatDecorator(convertible);
        convertible = new SeatCoverDecorator(convertible);
        convertible = new ServiceDecorator(convertible);

        assertEquals("USConvertible 1 (add undercoat) (add seat cover) (add service visit)", convertible.getName());
        assertEquals(23000 + 500 + 250 + 400, convertible.getCost());
    }

    // Test 4: Verify Multiple Decorators Stack Correctly
    @Test
    public void testMultipleDecorators() {
        Car coupe = japanFactory.createCoupe();
        coupe = new UndercoatDecorator(coupe);
        coupe = new SeatCoverDecorator(coupe);
        coupe = new SeatCoverDecorator(coupe);
        coupe = new ServiceDecorator(coupe);
        coupe = new ServiceDecorator(coupe);

        assertEquals(
                "JapanCoupe 1 (add undercoat) (add seat cover) (add seat cover) (add service visit) (add service visit)",
                coupe.getName());
        assertEquals(15000 + (500 + 250 + 250 + 400 + 400), coupe.getCost());
    }

    // Test 5: Verify Global Car Counter
    @Test
    public void testGlobalCarCounter() {
        Car sedan1 = usFactory.createSedan();
        Car sedan2 = japanFactory.createSedan();
        Car coupe1 = usFactory.createCoupe();

        assertEquals("USSedan 1", sedan1.getName());
        assertEquals("JapanSedan 2", sedan2.getName());
        assertEquals("USCoupe 3", coupe1.getName());
    }

    // Test 6: Verify US Car Components
    @Test
    public void testUSCarComponents() {
        Car coupe = usFactory.createCoupe();
        Engine engine = coupe.getEngine();
        Suspension suspension = coupe.getSuspension();
        Tires tires = coupe.getTires();

        assertEquals("Standard Engine", engine.getInfo(), "Engine should be Standard Engine");
        assertEquals("Racing Suspension", suspension.getInfo(), "Suspension should be Racing Suspension");
        assertEquals("Racing Tires", tires.getInfo(), "Tires should be Racing Tires");

        // Verify `getComponents()` returns correct string
        assertEquals("Standard Engine, Racing Suspension, Racing Tires", coupe.getComponents(),
                "getComponents() output is incorrect");
    }

    // Test 7: Verify Japan Car Components
    @Test
    public void testJapanCarComponents() {
        Car sedan = japanFactory.createSedan();
        Engine engine = sedan.getEngine();
        Suspension suspension = sedan.getSuspension();
        Tires tires = sedan.getTires();

        assertEquals("Economy Engine", engine.getInfo(), "Engine should be Economy Engine");
        assertEquals("Economy Suspension", suspension.getInfo(), "Suspension should be Economy Suspension");
        assertEquals("Economy Tires", tires.getInfo(), "Tires should be Economy Tires");

        // Verify `getComponents()` returns correct string
        assertEquals("Economy Engine, Economy Suspension, Economy Tires", sedan.getComponents(),
                "getComponents() output is incorrect");
    }

    // Test 8: Ensure Each Car Has a Unique Component Setup
    @Test
    public void testDifferentCarModelsHaveDifferentComponents() {
        Car usConvertible = usFactory.createConvertible();
        Car japanCoupe = japanFactory.createCoupe();

        // Ensure they have different engine types
        assertEquals("Racing Engine", usConvertible.getEngine().getInfo(), "US Convertible should have Racing Engine");
        assertEquals("Sport Engine", japanCoupe.getEngine().getInfo(), "Japan Coupe should have Sport Engine");

        // Ensure they have different suspensions
        assertEquals("Racing Suspension", usConvertible.getSuspension().getInfo(),
                "US Convertible should have Racing Suspension");
        assertEquals("Economy Suspension", japanCoupe.getSuspension().getInfo(),
                "Japan Coupe should have Economy Suspension");

        // Ensure they have different tires
        assertEquals("Racing Tires", usConvertible.getTires().getInfo(), "US Convertible should have Racing Tires");
        assertEquals("Sport Tires", japanCoupe.getTires().getInfo(), "Japan Coupe should have Sport Tires");
    }
}
