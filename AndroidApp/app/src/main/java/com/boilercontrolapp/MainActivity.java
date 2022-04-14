package com.boilercontrolapp;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity implements View.OnClickListener{

    private EditText accountName;
    public void onClick(View v){
        switch (v.getId()){
            case R.id.btnLogin:
                Toast.makeText(this, accountName.getText().toString(), Toast.LENGTH_SHORT).show();
                break;
            case R.id.accountEditTxt:
//                Toast.makeText(this, "Editing...", Toast.LENGTH_SHORT).show();
            default:
                break;
        }
    }
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Button loginBtn = findViewById(R.id.btnLogin);
        accountName = findViewById(R.id.accountEditTxt);
        loginBtn.setOnClickListener(this);
        accountName.setOnClickListener(this);
    }

    //method called when button is pressed
    public void SendMessage(View view){
        //Do something in response to the button


    }
}