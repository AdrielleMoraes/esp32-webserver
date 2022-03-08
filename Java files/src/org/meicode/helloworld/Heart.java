package org.meicode.helloworld;

import java.util.Scanner;

public class Heart extends Organ{
    private int heartRate;

    public Heart(String medicalCondition){
        super("Heart", medicalCondition);
    }

    public int getHeartRate(){
        return  heartRate;
    }

    public void setHeartRate(int heartRate) {
        this.heartRate = heartRate;
    }

    public void printOptions(){
        System.out.println("1. Change Heart Rate");
    }

    public void performAction(){

        Scanner scanner = new Scanner(System.in);
        int option = scanner.nextInt();
        switch (option){
            case 1:
                System.out.print("New value to heart rate:");
                int newrate = scanner.nextInt();
                setHeartRate(newrate);

                System.out.println("Heart rate set to: " + newrate);
                break;
            default:
                break;
        }
    }
}
