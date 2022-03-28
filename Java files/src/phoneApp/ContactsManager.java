package phoneApp;

import java.util.ArrayList;
import java.util.Scanner;

public class ContactsManager {

    ArrayList<Contact> contacts;

// do singleton instance here to guarantee there is only on instance of the contacts manager
    public ContactsManager(){
        contacts = new ArrayList<Contact>();
    }

    public void showMenu(){
        Scanner scanner = new Scanner(System.in);
        System.out.println("1 . Show all contacts");
        System.out.println("2. Add a new contact");
        System.out.println("3. Search for a contact");
        System.out.println("4. Delete a contact");
        System.out.println("5. Go back to previous menu");

        int op = scanner.nextInt();
        switch (op) {
            case 1:
                showContacts();
                showMenu();
                break;
            case 2:
                addContact();
                showMenu();
                break;
            case 3:
                String contact_name = getNameInput();
                searchContact(contact_name);
                showMenu();
                break;
            case 4:
                deleteContact();
                showMenu();
                break;
            default:
                break;
        }
    }

    private String getNameInput(){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Contact name:");
        return scanner.next();
    }
    private void addContact(){

        String contact_name = getNameInput();
        //check if contact exists first
        if (searchContact(contact_name) != null){
            System.out.println("Contact with this name already exists");
            return;
        }

        Scanner scanner = new Scanner(System.in);
        System.out.println("Contact number:");
        int number = scanner.nextInt();


        Contact newContact = new Contact(contact_name, number);

        contacts.add(newContact);
        System.out.println(String.format("New contact %s was added", newContact.getName()));
    }

    private Contact searchContact(String contact_name){
        Contact result = contacts.stream()
                .filter(contact -> contact_name.equals(contact.getName()))
                .findAny()
                .orElse(null);

        if (result != null){
            System.out.println("Found Contact");
            result.printDetails();
            return result;
        }
        else
            System.out.println("Contact not in the list");
        return null;
    }

    private void deleteContact(){

        String contact_name = getNameInput();
        // check first if contact is in the list
        Contact tobe_deleted = searchContact(contact_name);
        if(tobe_deleted != null){
            contacts.remove(tobe_deleted);
            System.out.println(String.format("%s was successfully removed from your phone", tobe_deleted.getName()));
            return;
        }
        System.out.println(String.format("Contact not in the list %s", contact_name));
    }

    public void showContacts(){
        System.out.println("Contacts in phone: ");
        contacts.forEach(contact -> contact.printDetails());
    }
}
