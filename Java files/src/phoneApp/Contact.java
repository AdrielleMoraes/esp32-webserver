package phoneApp;

public class Contact {

    private String name;
    private int number;

    public Contact(String name, int number){
        this.name = name;
        this.number = number;
    }

    public void printDetails(){
        System.out.println(name);
        System.out.println(number);
    }
}
