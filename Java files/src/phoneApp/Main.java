package phoneApp;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        boolean isAlive = true;
        /**
         * Simulate your phone's contacts and message applications
         *
         * Greet the user
         * show these 3 options: 1.Manage Contacts 2.Messages 3.Quit
         * In case of selecting 1 choose these options:
         *      1. Show all contacts
         *      2. Add a new contact
         *      3. Search for a contact
         *      4. Delete a contact
         *      5. Go back to previous menu
         * In case od selecting 2 choose these options:
         *      1. See the list of all messages
         *      2. Send a new message
         *      3. Go back to previous menu
         *
         * In case of 3 -> Quit the application
         *
          */

        // create new messages and contact manager
        MessageManager messagesManager = new MessageManager();
        ContactsManager contactsManager = new ContactsManager();

        // Greet the user
        System.out.println("Hello, Welcome!");

        while(isAlive){
            switch (menuOptions()){
                case 1:
                    System.out.println("Managing Contacts");
                    contactsManager.showMenu();
                    break;
                case 2:
                    System.out.println("Messages box");
                    messagesManager.showMenu(contactsManager);
                    break;
                default:
                    isAlive = false;
                    break;
            }
        }
    }

    private static int menuOptions(){

        Scanner scanner = new Scanner(System.in);
        System.out.println("Select one of the options below");
        System.out.println("1. Manage Contacts");
        System.out.println("2. Messages");
        System.out.println("3. Quit");

        int option = scanner.nextInt();
        return option;
    }
}
