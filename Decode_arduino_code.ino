#include <mcp_can.h>
#include <SPI.h>
#include <math.h>

#define engine_speed_ID   0x202
#define vehicle_speed_ID  0x202
#define pedal_gas_ID      0x202
#define steer_angle_ID    0x082
#define wheel_speed_ID    0x215 

long unsigned int rxId;
unsigned char len = 0;
unsigned char rxBuf[8];
char msgString[128];                        

unsigned char byte_1;
unsigned char byte_2;
unsigned char byte_3;
unsigned char byte_4;
unsigned char byte_5;
unsigned char byte_6;
unsigned char byte_7;
unsigned char byte_8;

#define CAN0_INT 2                              
MCP_CAN CAN0(9);                               

unsigned int Engine_speed(unsigned int message_ID);
unsigned int Vehicle_speed(unsigned int message_ID);
unsigned int Pedal_Gas(unsigned int message_ID);
unsigned int Steer_angle(unsigned int message_ID );
unsigned int FL_wheel_speed(unsigned int message_ID );
unsigned int FR_wheel_speed(unsigned int message_ID );
unsigned int RL_wheel_speed(unsigned int message_ID );
unsigned int RR_wheel_speed(unsigned int message_ID );


void setup()
{
  Serial.begin(115200);
  CAN0.begin(MCP_ANY, CAN_500KBPS, MCP_8MHZ);
  CAN0.setMode(MCP_NORMAL);                     
  pinMode(CAN0_INT, INPUT);                            
  
}

void loop()
{
  if(!digitalRead(CAN0_INT))                       
  {
    CAN0.readMsgBuf(&rxId, &len, rxBuf); 
  
    Engine_speed(engine_speed_ID);
    Vehicle_speed(vehicle_speed_ID);
    Pedal_Gas(pedal_gas_ID);
    Steer_angle(steer_angle_ID);
    FL_wheel_speed(wheel_speed_ID);
    FR_wheel_speed(wheel_speed_ID);
    RL_wheel_speed(wheel_speed_ID);
    RR_wheel_speed(wheel_speed_ID);

  }delay(10);
}

unsigned int Engine_speed(unsigned int message_ID)
{
  if(rxId == message_ID)
  {
    byte_1 = rxBuf[0];
    byte_2 = rxBuf[1];
    unsigned int combined_engine_hex = ((byte_1 << 8) | byte_2);
    Serial.println(round(0.25 * combined_engine_hex));
  }
}

unsigned int Vehicle_speed(unsigned int message_ID)
{
  if(rxId == message_ID)
  byte_3 = rxBuf[2];
  byte_4 = rxBuf[3];
  unsigned int combined_vehicle_hex = ((byte_3 << 8) | byte_4);
  Serial.println(round(0.01 * combined_vehicle_hex));
}

unsigned int Pedal_Gas(unsigned int message_ID)
{
  if(rxId == message_ID)
  {
    byte_5 = rxBuf[4]; 
    byte_6 = rxBuf[5];
    unsigned int half_hex_of_byte_6 = (byte_6 & 0xF0) >> 4;
    unsigned int combined_pedal_gas = (byte_5|(half_hex_of_byte_6 << 8));
    Serial.println(round(0.02*combined_pedal_gas));
  }
}

unsigned int Steer_angle(unsigned int message_ID )
{
  if(rxId == message_ID)
  {
    byte_1 = rxBuf[2];
    byte_2 = rxBuf[3];
    unsigned int combined_Steer_angle = ((byte_1 << 8)| byte_2);
    Serial.println(round((0.05*combined_Steer_angle) - 1600));
  }
}

unsigned int FL_wheel_speed(unsigned int message_ID )
{
  if(rxId == message_ID)
  {
    byte_1 = rxBuf[0];
    byte_2 = rxBuf[1];
    unsigned int combined_FL_hex = ((byte_1 << 8) | byte_2);
    Serial.println(round(0.01 * combined_FL_hex - 100));
  }
}

unsigned int FR_wheel_speed(unsigned int message_ID )
{
  if(rxId == message_ID)
  {
    byte_3 = rxBuf[2];
    byte_4 = rxBuf[3];
    unsigned int combined_FR_hex = ((byte_3 << 8) | byte_4);
    Serial.println(round(0.01 * combined_FR_hex - 100));
  }
}

unsigned int RL_wheel_speed(unsigned int message_ID )
{
  if(rxId == message_ID)
  {
    byte_5 = rxBuf[4];
    byte_6 = rxBuf[5];
    unsigned int combined_RL_hex = ((byte_5 << 8) | byte_6);
    Serial.println(round(0.01 * combined_RL_hex - 100));
  }
}

unsigned int RR_wheel_speed(unsigned int message_ID )
{
  if(rxId == message_ID)
  {
    byte_7 = rxBuf[6];
    byte_8 = rxBuf[7];
    unsigned int combined_RR_hex = ((byte_7 << 8) | byte_8);
    Serial.println(round(0.01 * combined_RR_hex - 100));
  }
}