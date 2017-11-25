#include <wiringPi.h>
#include <stdio.h>
#define LEDPIN  0 //LEDPIN is wiringPi Pin#0 or physical pin#11 or GPIO#17
int main(){
    //when initialize wiring failed,print message to screen
    if(wiringPiSetup()== -1){
        printf("Setup wiringPi Failed!");
        return -1;
    }
    pinMode(LEDPIN,OUTPUT);
    while(1){
        for (int i = 0; i < 3; i++)
        {
            digitalWrite(LEDPIN, HIGH);
            delay(100);
            digitalWrite(LEDPIN, LOW);
            delay(100);
        }
        delay(400);
        for (int i = 0; i < 3; i++)
        {
            digitalWrite(LEDPIN, HIGH);
            delay(500);
            digitalWrite(LEDPIN, LOW);
            delay(500);
        }
    }
    return 0;
}

