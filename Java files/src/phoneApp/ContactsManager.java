package phoneApp;

public class ContactsManager {

// do singleton instance here to guarantee there is only on instance of the contacts manager
    public ContactsManager(){

    }
    private void printOptions(){
        System.out.println("1 . Show all contacts");
        System.out.println("2. Add a new contact");
        System.out.println("3. Search for a contact");
        System.out.println("4. Delete a contact");
        System.out.println("5. Go back to previous menu");
    }

    public int selectOption(){
        this.printOptions();
        return 0;
    }
}
