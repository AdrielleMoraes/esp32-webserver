package phoneApp;

public class Message {

    private String bodyMessage;
    private Contact sender;
    public Message(String message, Contact sender){
        this.bodyMessage = message;
        this.sender = sender;
    }

    public void printMessage(){
        System.out.println(bodyMessage);
    }
}
