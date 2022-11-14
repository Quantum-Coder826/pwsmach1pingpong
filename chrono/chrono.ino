// alle standaart variabelen
const int lazer1 = 8;
const int lazer2 = 9;
const int ledPin = 13;
const float afstand = 0.30;
int beginTijd;
int eindTijd;
float tijd;
float snelheid;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); // start serieel
  pinMode(lazer1, INPUT);   // set all de nodige pin modi
  pinMode(lazer2, INPUT);
  pinMode(ledPin, OUTPUT);
  Serial.println(); // doe een mooie reset output maken
  Serial.print("reset");
  Serial.println();
  digitalWrite(ledPin, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(digitalRead(lazer1) < 1) { // wacht tot eerste lezer onderbroken is.
    beginTijd = micros(); // micros function retruns passed microseconds since start progam
    while(digitalRead(lazer2) > 0) {continue;} // wacht tot de bal door de tweede lazerpoort gaat
    eindTijd = micros();
    digitalWrite(ledPin, HIGH);
    tijd = beginTijd - eindTijd; // krijg de tijd die nodig is om afstand af te leggen.
    tijd = tijd / 1000000; // ga microseconden naar seconden
    
    Serial.print("beginTijd (ms):"); // print al de losse waarden met 8 decimalen
    Serial.println(beginTijd, 8);
    Serial.print("eindTijd (ms):");
    Serial.println(eindTijd, 8);
    Serial.print("deltaTijd (s):");
    Serial.println(tijd, 8);

    Serial.println(); // lege regel printen
    snelheid = afstand / tijd; // bereken snelheid
    Serial.print("v="); // print snelheid met 8 decimalen
    Serial.print(snelheid, 8);

    while(true) {continue;} // loop voor altijd
  }
}
