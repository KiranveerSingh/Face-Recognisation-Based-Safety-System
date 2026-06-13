#define RELAY 8
#define BUZZER 9

void setup() {
  pinMode(RELAY, OUTPUT);
  pinMode(BUZZER, OUTPUT);
  Serial.begin(9600);

  digitalWrite(RELAY, HIGH); // default OFF
}

void loop() {
  if (Serial.available()) {
    char c = Serial.read();

    if (c == 'U') {
      digitalWrite(RELAY, LOW);  // ON (unlock)
      digitalWrite(BUZZER, HIGH);
      delay(200);
      digitalWrite(BUZZER, LOW);
    }

    if (c == 'L') {
      digitalWrite(RELAY, HIGH); // OFF (lock)
    }

    if (c == 'A') {
      for(int i=0;i<3;i++){
        digitalWrite(BUZZER, HIGH);
        delay(200);
        digitalWrite(BUZZER, LOW);
        delay(200);
      }
    }
  }
}