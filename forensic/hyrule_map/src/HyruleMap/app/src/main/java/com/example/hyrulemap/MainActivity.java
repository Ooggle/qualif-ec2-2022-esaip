package com.example.hyrulemap;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;
import com.ortiz.touchview.TouchImageView;

import java.util.ArrayList;
import java.util.Random;

public class MainActivity extends AppCompatActivity {

    ArrayList<String> messages = new ArrayList<>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        messages.add("What are you trying to do?");
        messages.add("Click doesn't do anything...");
        messages.add("Stop your useless actions.");
        messages.add("Shoutout to Mizu and Ooggle :)");
        messages.add("Try zooming :)");

        TouchImageView img = findViewById(R.id.imageCarte);
        img.setMaxZoom(20);
        img.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Random random = new Random();
                int rand = random.nextInt(messages.size());
                Toast.makeText(MainActivity.this, messages.get(rand), Toast.LENGTH_SHORT).show();
            }
        });

        int tok1 = 5;
        tok1*= 679;
        tok1<<= 6;

        int tok2 = -50;
        tok2*= -tok1;

        RequestQueue queue = Volley.newRequestQueue(this);
        String url = "https://ooggle.re/flag.php?token=";

        StringRequest stringRequest = new StringRequest(Request.Method.GET, url + String.valueOf((tok1<<2) + tok2),
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
                        if(response.equals("Wrong token")) {
                            Log.i("APP", "Wrong token.");
                        } else {
                            Log.i("APP", "Successfully sent information about compromised device.");
                        }
                    }
                }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                Log.i("APP", "Error while requesting the server.");
            }
        });

        queue.add(stringRequest);
    }
}