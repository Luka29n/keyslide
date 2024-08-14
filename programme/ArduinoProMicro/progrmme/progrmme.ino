int pourcentageVolumeMaster;
int volumePrecedent;

void setup() {
  Serial.begin(9600);
  volumePrecedent = pourcentageVolumeMaster;
}

void loop() {
  pourcentageVolumeMaster = map(analogRead(A0), 0, 1023, 0, 100);
  if (volumePrecedent!=pourcentageVolumeMaster && volumePrecedent!=(pourcentageVolumeMaster+1) && volumePrecedent!=(pourcentageVolumeMaster-1)){
    Serial.println(pourcentageVolumeMaster);
    volumePrecedent = pourcentageVolumeMaster;
  }
  
  delay(100); 
}