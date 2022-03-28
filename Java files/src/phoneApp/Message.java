package phoneApp;

public class Message {

    private String bodyMessage;
    private Contact sender;
    private String messageType;
    public Message(String message, Contact sender, String type){
        this.bodyMessage = message;
        this.sender = sender;
        this.messageType = type;
    }

    public void printMessage(){
        System.out.println(bodyMessage);
    }
}
