package phoneApp;

import java.util.ArrayList;

public class ContactsManager {

    ArrayList<Contact> contacts;
// do singleton instance here to guarantee there is only on instance of the contacts manager
    public ContactsManager(){
        contacts = new ArrayList<Contact>();

        contacts.add(new Contact("Admin", 987654321));
    }

    public void showMenu(){
        System.out.println("1 . Show all contacts");
        System.out.println("2. Add a new contact");
        System.out.println("3. Search for a contact");
        System.out.println("4. Delete a contact");
        System.out.println("5. Go back to previous menu");
    }

    public void showContacts(){
        System.out.println("Contacts in phone");
        contacts.forEach(contact -> contact.printDetails());
        // show menu again after printing options
        showMenu();
    }
}
