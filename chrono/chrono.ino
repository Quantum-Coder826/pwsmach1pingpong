#define startPoort 9
#define stopPoort 8
#define led 13

const float afstand = 0.225;
int startTijd;
int eindTijd;
float deltaTijd;
float snelheid;

void setup() {
  Serial.begin(9600); // start serieel
  pinMode(startPoort, INPUT);   // set all de nodige pin modi
  pinMode(stopPoort, INPUT);
  pinMode(led, OUTPUT);

  // serial reset output
  Serial.print("reset");
  Serial.println();
  digitalWrite(led, LOW);

  while (digitalRead(startPoort) == 1) { 
    // wacht tot de eerste poort gebroken is.
  }
  startTijd = micros(); // sla de start tijd op
  digitalWrite(led, HIGH);
  
  while (digitalRead(stopPoort) == 1) { 
    // wacht tot de tweede poort gebroken is.
  }
  eindTijd = micros(); // sla de eindtijd op

  deltaTijd = eindTijd - startTijd; // reken het verschil uit
  deltaTijd /= 1000000; // ga van microseconden naar seconden

  snelheid = afstand / deltaTijd; // bereken de snelheid.

  // al de tijden printen over serial
  Serial.print("startTijd (microseconden): ");
  Serial.println(startTijd, 8);
  Serial.print("eindTijd (microseconden): ");
  Serial.println(eindTijd, 8);
  Serial.print("deltaTijd (seconden): ");
  Serial.println(deltaTijd, 8);

  Serial.println(); // lege regel printen
  Serial.print("v=");
  Serial.println(snelheid, 8);
}

void loop() {
  // loop tot reset
}
    
//     Serial.print("beginTijd (ms):"); // print al de losse waarden met 8 decimalen
//     Serial.println(beginTijd, 8);
//     Serial.print("eindTijd (ms):");
//     Serial.println(eindTijd, 8);
//     Serial.print("deltaTijd (s):");
//     Serial.println(tijd, 8);

//     Serial.println(); // lege regel printen
//     snelheid = afstand / tijd; // bereken snelheid
//     Serial.print("v="); // print snelheid met 8 decimalen
//     Serial.print(snelheid, 8);

//     while(true) {continue;} // loop voor altijd
//   }
// }
