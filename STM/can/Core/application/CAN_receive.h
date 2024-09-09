#ifndef CAN_RECEIVE_H
#define CAN_RECEIVE_H

#include "struct_typedef.h"

#define CHASSIS_CAN hcan1
#define GIMBAL_CAN hcan2

// can发送、接收至电机的ID
typedef enum
{
    CAN_CHASSIS_ALL_ID = 0x200,
    CAN_3508_M1_ID = 0x201,
    CAN_3508_M2_ID = 0x202,
    CAN_3508_M3_ID = 0x203,
    CAN_3508_M4_ID = 0x204,

    CAN_GIMBAL_ALL_ID = 0x1FF,
    CAN_YAW_MOTOR_ID = 0x205,
    CAN_PIT_MOTOR_ID = 0x206,
    CAN_TRIGGER_MOTOR_ID = 0x207,
};

// 电机测量数据结构体
typedef struct
{
    uint16_t ecd;          // 机械角度
    int16_t speed_rpm;     // 转速
    int16_t given_current; // 电流
    uint8_t temperate;     // 温度
    int16_t last_ecd;
} motor_measure_t;

extern void CAN_cmd_gimbal(int16_t yaw, int16_t pitch, int16_t shoot, int16_t rev);

// extern void CAN_cmd_chassis_reset_ID(void);

extern void CAN_cmd_chassis(int16_t motor1, int16_t motor2, int16_t motor3, int16_t motor4);

#endif