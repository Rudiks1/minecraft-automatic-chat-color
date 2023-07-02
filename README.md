# Minecraft server auto chat color

<p>This is a Python program that automatically adds color to your Minecraft chat messages. By running this program in the background while playing Minecraft, you can enhance the visual appeal of your messages with the selected color.</p>

# Usage
<ol>
<li>Clone the repository to your local machine or download the autocolorchat.py file.</li>
<li>Make sure you have Python installed on your system.</li>
<li>Install the required dependencies using the following command in your CMD: pip install keyboard</li>
<li>Open a terminal or command prompt and navigate to the directory where autocolorchat.py is located.</li>
<li>Run the program by executing the following command: python autocolorchat.py</li>
<li>Start Minecraft and join a server.</li>
</ol>

# Operation

<p>Whenever you want to send a message, press the "T" key to open the chat and begin typing. The program will automatically insert the chosen color code at the start of your message.
Press "Enter" to send the message. The program will remember if the chat is open or closed and reapply the color code accordingly. The allowed color codes and the format of the color codes can be different between servers. Please check the color format on your server before using this tool.</p>

<p>List of Minecraft colors and formats: <a href="https://www.digminecraft.com/lists/color_list_pc.php">www.digminecraft.com/lists/color_list_pc.php</a></p>

# How It Works
<p>The program utilizes the keyboard library to detect key press events in real-time. When you press the "T" key to open the chat, the program starts a separate thread to continuously monitor if you intend to type a command or a regular message. If it detects a command, it temporarily disables the colorization. Otherwise, it injects the chosen color code at the beginning of your message before sending it. You can choose the chat color by typing it to the input field after running the code.</p>

<p>Please note that the program runs in the background and requires Python to be active while you play Minecraft. Make sure to keep the program running for the automatic colorization to work.</p>

<p>This program is intended for educational purposes and personal use. Make sure to abide by the rules and guidelines of the Minecraft servers you are playing on.</p>
