package phoneApp;

public class Message {

    private String bodyMessage;
    private Contact recipient;

    public Message(String message, Contact recipient){
        this.bodyMessage = message;
        this.recipient = recipient;
    }
    public void printMessage(){
        System.out.println(String.format("Message from: %s\n%s", recipient.getName(),bodyMessage));
    }
}
