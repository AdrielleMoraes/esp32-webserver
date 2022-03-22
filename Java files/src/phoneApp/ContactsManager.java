package phoneApp;

import java.util.ArrayList;
import java.util.Scanner;

public class ContactsManager {

    ArrayList<Contact> contacts;
    Scanner scanner;
// do singleton instance here to guarantee there is only on instance of the contacts manager
    public ContactsManager(){
        contacts = new ArrayList<Contact>();
        scanner = new Scanner(System.in);
        contacts.add(new Contact("Admin", 987654321));
    }

    public void showMenu(){

        System.out.println("1 . Show all contacts");
        System.out.println("2. Add a new contact");
        System.out.println("3. Search for a contact");
        System.out.println("4. Delete a contact");
        System.out.println("5. Go back to previous menu");

        int op = scanner.nextInt();
        switch (op){
            case 1:
                showContacts();
                break;
            case 2:
                addContact();
                break;
            case 3:
                searchContact(new Contact("Myself", 1234));
                break;
            case 4:

                break;
            default:
                break;
        }

    }

    private void addContact(){
        Contact newContact = new Contact("default", 12345);
        contacts.add(newContact);
    }

    private boolean searchContact(Contact contact){
        if (contacts.contains(contact)){
            System.out.println("Found Contact");
            contact.printDetails();
            return true;
        }
        else
            System.out.println("Contact not in the list");
        return false;
    }

    private void deleteContact(Contact contact){
        // check first if contact is in the list
        if(searchContact(contact)){
            contacts.remove(contact);
            System.out.println(String.format("{} was successfully removed from your phone", contact.getName()));
            return;
        }
        System.out.println(String.format("Contact not in the list", contact.getName()));

    }
    public void showContacts(){
        System.out.println("Contacts in phone: ");
        contacts.forEach(contact -> contact.printDetails());
        // show menu again after printing options
        showMenu();
    }
}
