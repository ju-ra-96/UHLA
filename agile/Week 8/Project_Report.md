### What did you work on this past week?
Sammy: Built a demo buzzer controlled by the Pi. It detects noise with one mic. A simple buzzer motor responds to that information. 
Arturo: Helped Sammy and built a python webserver that uses websockets to communicate sample data to a client.
Scott: Implemented client side code for the watch
Julian: Implemented watch buzzing functionality and experimented with different types and durations of buzz. 

### What will you work on this coming week?
Sammy: Double up on the demo buzzer. One for each side. 
Arturo: Work with Scott to decide what information the watches and server will communicate to each other and build out the corresponding backend.
Scott: Work with Arturo for the communication between watches and server. Work with Julian to ingreate buzzing software and websocket software in the watch. 
Julian: Work with Scott to integrate watch software

### What is in your way or impeding progress?
Thanksgiving, no access to the fancy mics yet, inexperience with Android Studio. Might need to get an ADC in the meantime.


This week, Sammy built a local-only demo buzzer. The Raspberry Pi controls two buzzers that turn on when their corresponding microphone detects noise. It buzzes a lot because the microphones are very very sensitive. Arturo helped Sammy and built a Python webserver that uses websockets to communicate simple data to a client. They then tested that server on the Pi, and accessed it from the web using ngrok. Scott built a wear OS websocket client, and Julian built a watch app that explores the different patterns, lengths and intensities of vibration that we can use.

In the coming week, we plan to combine the pieces that we have built so far. Scott and Julian will combine their Wear OS codebases to make 