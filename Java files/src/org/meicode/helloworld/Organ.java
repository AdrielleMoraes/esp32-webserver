package org.meicode.helloworld;

public class Organ {

    private String name;
    private String medicalCondition;

    public Organ(String name, String medicalCondition){
        this.name = name;
        this.medicalCondition = medicalCondition;
    }

    public void printDetails(){
        System.out.println(name);
        System.out.println("Medical Condition: " + medicalCondition);
    }

    public void printOptions(){
        System.out.print("\n");
    }

    public void performAction(){
        return;
    }
}
