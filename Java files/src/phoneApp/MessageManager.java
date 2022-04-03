package phoneApp;

import java.util.ArrayList;
import java.util.Scanner;

public class MessageManager {

    ArrayList<Message> messages;
    ContactsManager contacts;
    /*
         *      1. See the list of all messages
         *      2. Send a new message
         *      3. Go back to previous menu
     */

    // create a list with all messages on constructor
    public MessageManager(){
        messages = new ArrayList<>();
    }

    public void showMenu(ContactsManager contacts){
        this.contacts = contacts;
        Scanner scanner = new Scanner(System.in);
        if(contacts.contactsSize() <= 0){
            System.out.println("No contacts in this phone");
            return;
        }
        System.out.println("1 . See list of all messages");
        System.out.println("2. Send a new Message");
        System.out.println("3. Go back to previous menu");

        int option = scanner.nextInt();

        switch (option){
            case 1:
                printMessages();
                showMenu(contacts);
                break;
            case 2:
                sendMessage();
                showMenu(contacts);
                break;
            default:
                break;
        }
    }

    public void printMessages(){
        messages.forEach((message) -> message.printMessage());
    }

    public void sendMessage(){

        Scanner scanner = new Scanner(System.in).useDelimiter("\n");
        System.out.println("Select Contact to send message to: ");

        String recipient_name = scanner.next();
        Contact recipient = contacts.searchContact(recipient_name);
        if ( recipient == null) {
            System.out.println("Contact not in the list");
            return;
        }
        System.out.println("Please type text body");

        String msg = scanner.next();
        Message newMessage = new Message(msg, recipient);

        messages.add(newMessage);
    }
}
