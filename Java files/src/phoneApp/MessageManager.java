package phoneApp;

public class MessageManager {
    /*
             *      1. See the list of all messages
         *      2. Send a new message
         *      3. Go back to previous menu
     */
    // do singleton instance here to guarantee there is only on instance of the contacts manager
    public MessageManager(){

    }

    private void printOptions(){
        System.out.println("1 . See list of all messages");
        System.out.println("2. Send a new Message");
        System.out.println("3. Go back to previous menu");
    }

    public int selectOption(){
        this.printOptions();
        return 0;
    }
}
