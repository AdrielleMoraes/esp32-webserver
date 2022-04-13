package com.boilercontrolapp;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity implements View.OnClickListener{

    public void onClick(View v){
        switch (v.getId()){
            case R.id.btnLogin:
                Toast.makeText(this, "Hello Button", Toast.LENGTH_SHORT).show();
                break;
            default:
                break;
        }
    }
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Button loginBtn = findViewById(R.id.btnLogin);

        loginBtn.setOnClickListener(this);
    }

    //method called when button is pressed
    public void SendMessage(View view){
        //Do something in response to the button


    }
}