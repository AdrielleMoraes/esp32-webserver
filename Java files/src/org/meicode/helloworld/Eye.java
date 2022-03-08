package org.meicode.helloworld;

import java.util.Scanner;

public class Eye extends Organ{

    private String colour;
    private String side;
    private boolean isOpen;
    public Eye(String colour, String eyeSide,boolean isOpen, String medicalCondition){
        super(eyeSide + "Eye", medicalCondition);
        this.colour = colour;
        this.side = eyeSide;
        this.isOpen = isOpen;
    }

    public String getColour() {
        return colour;
    }

    public void printOptions(){
        System.out.println("Colour: " + colour);
        if(isOpen)
            System.out.println("1. Close the eye");
    }

    public void performAction(){
        if (!isOpen)
            return;

        Scanner scanner = new Scanner(System.in);
        int option = scanner.nextInt();
        switch (option) {
            case 1:
                System.out.println(side + " eye closed");
                this.isOpen = false;
                break;

            default:
                break;
        }
        return;
    }


}
