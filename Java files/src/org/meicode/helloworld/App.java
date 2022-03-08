package org.meicode.helloworld;

import java.util.Random;
import java.util.Scanner;

public class App {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int input;
        boolean isalive = true;


        Eye leftEye = new Eye("Blue", "Left", true, "Normal");
        Eye rightEye = new Eye("Green", "Right", true, "Short sighted");
        Heart heart = new Heart("Normal");
        Stomach stomach = new Stomach(false, "PUD");
        Organ skin = new Organ("Skin", "Burnt");

        Patient patient = new Patient("Tom", 25, rightEye, leftEye, heart, stomach, skin);

        patient.printDetails();

        while(isalive)
        {
            printOptions();

            input = scanner.nextInt();

            switch (input){
                case 1:
                    // left eye
                    organOptions(patient.leftEye);
                    break;

                case 2:
                    // right eye
                    organOptions(patient.rightEye);
                    break;

                case 3:
                    // Heart
                    organOptions(patient.heart);
                    break;

                case 4:
                    // Stomach
                    organOptions(patient.stomach);
                    break;

                case 5:
                    // Skin
                    organOptions(patient.skin);
                    break;

                default:
                    // quit
                    isalive = false;
                    break;
            }
        }
        System.out.print("Application finished!");
    }

    public static void printOptions(){
        System.out.println("Choose an organ: ");
        System.out.println("1. Left Eye");
        System.out.println("2. Right Eye");
        System.out.println("3. Heart");
        System.out.println("4. Stomach");
        System.out.println("5. Skin");
        System.out.println("6. Exit");
    }

    public static void organOptions(Organ organ){
        organ.printDetails();
        organ.printOptions();
        organ.performAction();
    }
}
