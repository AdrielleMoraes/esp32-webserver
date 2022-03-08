package org.meicode.helloworld;

import java.util.Scanner;

public class Stomach extends Organ{

    private boolean isFed;
    public Stomach(boolean isFed, String medicalCondition){
        super("Stomach", medicalCondition);
        this.isFed = isFed;
    }

    public void setFed(boolean fed) {
        isFed = fed;
    }

    public void digest(){
        setFed(true);
        System.out.println("Digestion begins");
    }

    public void printOptions(){
        if (isFed){
            System.out.println("Doesn't need to be fed");
        }
        else{
            System.out.println("Needs to be fed");
        }

        System.out.println("1. Digest");
    }

    public void performAction(){
        Scanner scanner = new Scanner(System.in);
        int option = scanner.nextInt();
        switch (option){
            case 1:
                digest();
                break;
            default:
                break;
        }
    }
}
