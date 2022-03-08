package org.meicode.helloworld;

import java.util.ArrayList;
import java.util.List;

public class Patient {

    private String name;
    private int age;

    Eye leftEye;
    Eye rightEye;
    Heart heart;
    Stomach stomach;
    Organ skin;

    public Patient(String name, int age, Eye rightEye, Eye leftEye, Heart heart, Stomach stomach, Organ skin){
        this.name = name;
        this.age = age;

        this.leftEye = leftEye;
        this.rightEye = rightEye;
        this.heart = heart;
        this.stomach = stomach;
        this.skin = skin;
    }

    public void printDetails(){
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
    }

}
