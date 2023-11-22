# OIBSIP

PROJECT 1 - Voice Assistant : 
This Python script is a voice assistant that listens to user commands via a microphone using the speech_recognition library. It converts text to speech with pyttsx3, enabling interaction through voice commands. The assistant can respond to commands related to time, date, greetings, and web searches. The take_command() function captures user speech, assistant() interprets the commands, and executes actions based on recognized phrases. The main loop continuously listens for user input, processing commands and providing responses through voice synthesis.

PROJECT 2 - BMI Calculator : 
This Python script calculates Body Mass Index (BMI) based on user inputs for weight and height. It consists of:
calculate_bmi: Calculates BMI by dividing weight (in kilograms) by the square of height (in meters).
classify_bmi: Classifies the calculated BMI into predefined categories such as Underweight, Normal, Overweight, or Obese.
main: Accepts user inputs for weight and height within a loop to ensure validity. It calculates BMI and classifies it, displaying the result.
The script validates input values, ensuring they are numeric and greater than zero. It uses a loop (while flag == 0) to continuously prompt the user for valid inputs until correct values are provided, then calculates the BMI and displays the result along with the corresponding classification.

PROJECT 3 - Random Password Generator : 
This Python script generates passwords based on user-defined criteria:
generate_password: Generates a password of specified length, incorporating character sets as per user preferences (letters, numbers, symbols). It ensures at least one character from each selected set is included for stronger passwords.
main: Prompts the user to input preferences for password length, and whether to include letters, numbers, or symbols. It generates a password based on these preferences and displays the result.
The script ensures at least one character set is selected for the password generation, validating user inputs for character set preferences and length. It creates a random password using the chosen characters and confirms the inclusion of at least one character from each selected set for enhanced security. Finally, it displays the generated password to the user.






