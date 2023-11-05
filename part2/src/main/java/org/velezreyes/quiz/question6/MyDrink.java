package org.velezreyes.quiz.question6;

public class MyDrink implements Drink {
        private String name;
        private boolean fizzy;
    
        public MyDrink(String name, boolean fizzy) {
            this.name = name;
            this.fizzy = fizzy;
        }
    
        @Override
        public String getName() {
            return name;
        }
    
        @Override
        public boolean isFizzy() {
            return fizzy;
        }
}
