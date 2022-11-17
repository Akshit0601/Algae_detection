int motor1pin1=2;
int motor1pin2=3;
int motor2pin1=4;
int motor2pin2=5;
int rpi_input1=7;
int rpi_input2=8;

void setup() {
  pinMode(rpi_input1,INPUT);
  pinMode(rpi_input2,INPUT);
  pinMode(motor1pin1,OUTPUT);
  pinMode(motor1pin2,OUTPUT);
  pinMode(motor2pin1,OUTPUT);
  pinMode(motor2pin2,OUTPUT);
  
}

void loop() {
  int state_l=digitalRead(7);
  int state_r=digitalRead(8);
  if(state_l==HIGH && state_r==LOW){
    digitalWrite(motor1pin1,HIGH);
    digitalWrite(motor1pin2,LOW);
  }
  else if(state_r==HIGH && state_r==LOW){
    digitalWrite(motor2pin1,HIGH);
    digitalWrite(motor2pin2,LOW);
  }
  else if(state_l==HIGH && state_r==HIGH){
   digitalWrite(motor1pin1,HIGH);
   digitalWrite(motor1pin2,LOW);
   digitalWrite(motor2pin1,HIGH);
   digitalWrite(motor2pin2,LOW);   
   }
}
