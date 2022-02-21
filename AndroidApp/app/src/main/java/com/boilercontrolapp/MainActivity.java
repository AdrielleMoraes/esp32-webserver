package com.boilercontrolapp;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    //method called when button is pressed
    public void SendMessage(View view){
        //Do something in response to the button
        TextView txtFirstName = findViewById(R.id.textFirstName);
        TextView txtLastName = findViewById(R.id.textLastName);
        TextView txtEmail = findViewById(R.id.textEmail);


        EditText editFirstName = findViewById(R.id.editFirstName);
        EditText editLastName = findViewById(R.id.editLastName);
        EditText editEmail = findViewById(R.id.editEmail);

        txtFirstName.setText(editFirstName.getText());
        txtLastName.setText(editLastName.getText());
        txtEmail.setText(editEmail.getText());
    }
}