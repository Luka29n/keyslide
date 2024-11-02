#include <Keypad.h>
#include <Keyboard.h>

const int NUM_SLIDERS = 3;
const int analogInputs[NUM_SLIDERS] = {A3, A2, A1};
int analogSliderValues[NUM_SLIDERS];
int HystoryValue[NUM_SLIDERS] = {0,0,0};
bool toggleState = false;

const byte ROWS = 4; // four rows
const byte COLS = 3; // three columns
char keys[ROWS][COLS] = {
  {'1', '2', '3'},
  {'4', '5', '6'},
  {'7', '8', '9'},
  {'*', '0', '#'}
};
byte rowPins[ROWS] = {5, 4, 3, 2};   
byte colPins[COLS] = {9, 7, 6};      

Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

void setup() {
  for (int i = 0; i < NUM_SLIDERS; i++) {
    pinMode(analogInputs[i], INPUT);
  }

  Serial.begin(9600);
  Keyboard.begin();
}

void loop() {
  updateSliderValues();
  sendSliderValues();
  checkKeypad();
  delay(10);
}

void changefunctionpotentiometer() {

  for (int i = 0; i < NUM_SLIDERS; i++) {
    HystoryValue[i] = 1023 - analogRead(analogInputs[i]); // Inversion des valeurs
  }
}

void updateSliderValues() {
  for (int i = 0; i < NUM_SLIDERS; i++) {
    analogSliderValues[i] = 1023 - analogRead(analogInputs[i]); // Inversion des valeurs
  }
}

void sendSliderValues() {
  String builtString = "";
  String builtStringHystory = "";
  for (int i = 0; i < NUM_SLIDERS; i++) {
    builtString += String(analogSliderValues[i]);

    if (i < NUM_SLIDERS - 1) {
      builtString += "|";
    }
  }
  for (int i = 0; i < NUM_SLIDERS; i++) {
    builtStringHystory += String(HystoryValue[i]);

    if (i < NUM_SLIDERS - 1) {
      builtStringHystory += "|";
    }
  }
  if (toggleState == false) {
    Serial.println(builtString);
  } else if (toggleState == true){
    Serial.println(builtStringHystory+"|"+builtString);
  }
  
}

void checkKeypad() {
  char key = keypad.getKey();
  if (key) {
    switch (key) {
      case '1':
        Keyboard.write(KEY_F13);
        break;
      case '2':
        Keyboard.write(KEY_F14);
        break;
      case '3':
        Keyboard.write(KEY_F15);
        break;
      case '4':
        Keyboard.write(KEY_F16);
        break;
      case '5':
        Keyboard.write(KEY_F17);
        break;
      case '6':
        Keyboard.write(KEY_F18);
        break;
      case '7':
        Keyboard.write(KEY_F19);
        break;
      case '8':
        Keyboard.write(KEY_F20);
        break;
      case '9':
        Keyboard.write(KEY_F21);
        break;
      case '*':
        toggleState = !toggleState; 
        changefunctionpotentiometer();// Basculer l'état de toggleState
        break;
      case '0':
        Keyboard.write(KEY_F23);
        break;
      case '#':
        Keyboard.write(KEY_F24);
        break;
    }
  }
}
