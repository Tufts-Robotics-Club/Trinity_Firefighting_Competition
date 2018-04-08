
const int NUM_SENSORS = 8;
int pin[NUM_SENSORS][2] = {{2,3},{4,5},{6,7},{8,9},{10,11},{22,23},{46,47},{44,45}}; 

int TIMEOUT = 10000;

void setup() {
  Serial.begin(9600);
}

void loop() {
  long duration, cm;
  int dis[NUM_SENSORS];
    int in = Serial.read();
    for (int i = 0; i < NUM_SENSORS; i++)
    {
      pinMode(pin[i][1], OUTPUT);
      digitalWrite(pin[i][1], LOW);
      delayMicroseconds(2);
      digitalWrite(pin[i][1], HIGH);
      delayMicroseconds(5);
      digitalWrite(pin[i][1], LOW);
      
      pinMode(pin[i][0], INPUT);
      duration = pulseIn(pin[i][0], HIGH, TIMEOUT);

      if(duration == 0) {
          duration = TIMEOUT;
      }

      cm = microsecondsToCentimeters(duration);
      dis[i] = cm;

    }
    Serial.println(String(dis[0])+" "+String(dis[1])+" "+String(dis[2])+" "+String(dis[3])+" "+String(dis[4])
                   +" "+String(dis[5])+" "+String(dis[6])+" "+String(dis[7])); 
}

long microsecondsToCentimeters(long microseconds) {
  return microseconds / 29 / 2;
}
