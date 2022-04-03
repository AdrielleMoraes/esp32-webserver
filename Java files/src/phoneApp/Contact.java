package phoneApp;

import java.util.ArrayList;

public class Contact {

    private String name;
    private int number;


    public Contact(String name, int number){
        this.name = name;
        this.number = number;
    }

    public String getName() {
        return name;
    }

    public void printDetails(){
        System.out.println(String.format("Name: %s - Number: %d", name,number));
    }

}
