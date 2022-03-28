package phoneApp;

import java.util.ArrayList;
import java.util.Scanner;

public class MessageManager {

    ArrayList<Message> messages;
    /*
         *      1. See the list of all messages
         *      2. Send a new message
         *      3. Go back to previous menu
     */

    // do singleton instance here to guarantee there is only on instance of the contacts manager
    // create a list with all messages on constructor
    public MessageManager(){
        messages = new ArrayList<Message>(); // Create an ArrayList object

        // add a few messages to the list
        messages.add(new Message("Hello World", new Contact("User", 123456789), "Received"));
    }

    public void showMenu(){

        Scanner scanner = new Scanner(System.in);

        System.out.println("1 . See list of all messages");
        System.out.println("2. Send a new Message");
        System.out.println("3. Go back to previous menu");

        int option = scanner.nextInt();

        switch (option){
            case 1:
                printMessages();
                break;
            case 2:
                sendMessage();
                break;
            default:
                break;
        }
    }

    public void printMessages(){
        messages.forEach((message) -> message.printMessage());
        showMenu();
    }

    public void sendMessage(){
        System.out.println("Please type text body");
        Scanner scanner = new Scanner(System.in);

        String msg = scanner.next();

        System.out.println("Select Contact to send message to: ");
        showMenu();
    }
}
