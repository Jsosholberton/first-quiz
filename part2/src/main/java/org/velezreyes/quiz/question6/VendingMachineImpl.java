package org.velezreyes.quiz.question6;

import java.util.HashMap;
import java.util.Map;

public class VendingMachineImpl implements VendingMachine {
    private static VendingMachineImpl instance;
    private Map<String, Integer> drinkPrices;
    private int balance;

    private VendingMachineImpl() {
        drinkPrices = new HashMap<>();
        drinkPrices.put("ScottCola", 75);  // Price for ScottCola in cents
        drinkPrices.put("KarenTea", 100);   // Price for KarenTea in cents
    }

    public static VendingMachine getInstance() {
        if (instance == null) {
            instance = new VendingMachineImpl();
        }
        return instance;
    }

    @Override
    public void insertQuarter() {
        balance += 25;  // Inserting a quarter adds 25 cents to the balance
    }

    @Override
    public Drink pressButton(String drinkName) throws NotEnoughMoneyException, UnknownDrinkException {
        Integer price = drinkPrices.get(drinkName);

        if (price == null) {
            throw new UnknownDrinkException("Unknown drink: " + drinkName);
        }

        if (balance < price) {
            throw new NotEnoughMoneyException("Not enough money to purchase " + drinkName);
        }

        // If we reach here, it means there's enough money to purchase the drink
        balance -= price;

        if (drinkName.equals("ScottCola")) {
            return new MyDrink(drinkName, true);
        } else {
            return new MyDrink(drinkName, false);
        }
    }
}
