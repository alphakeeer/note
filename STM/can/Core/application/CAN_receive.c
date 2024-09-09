#include "CAN_receive.h"
#include "main.h"

extern CAN_HandleTypeDef hcan1;
extern CAN_HandleTypeDef hcan2;

// 从data中提取电机测量数据存入ptr
#define get_motor_measure(ptr, data)                                   \
    {                                                                  \
        (ptr)->last_ecd = (ptr)->ecd;                                  \
        (ptr)->ecd = (uint16_t)((data)[0] << 8 | (data)[1]);           \
        (ptr)->speed_rpm = (uint16_t)((data)[2] << 8 | (data)[3]);     \
        (ptr)->given_current = (uint16_t)((data)[4] << 8 | (data)[5]); \
        (ptr)->temperate = (data)[6];                                  \
    }

/*电机数据:
        0:底盘电机1 3508电机
        1:底盘电机2 3508电机
        2:底盘电机3 3508电机
        3:底盘电机4 3508电机;
        4:yaw云台电机 6020电机;
        5:pitch云台电机 6020电机;
        6:拨弹电机 2006电机*/
static motor_measure_t motor_total[7];

// CAN_TxHeaderTypeDef -> 可理解为CAN发送消息的头部，包含了发送消息的ID、格式、类型、数据长度等信息
static CAN_TxHeaderTypeDef gimbal_tx_message;
static uint8_t gimbal_can_send_data[8]; // 发送至云台电机的控制数据
static CAN_TxHeaderTypeDef chassis_tx_message;
static uint8_t chassis_can_send_data[8]; // 发送至底盘电机的控制数据

// 从can中接收电机数据并解码存入motor_chassis
void HAL_CAN_RxFifo0MsgPendingCallback(CAN_HandleTypeDef *hcan)
{

    CAN_RxHeaderTypeDef rx_header; // 利用其接收CAN消息的头部
    uint8_t rx_data[8];            // 利用其接收CAN消息的数据

    HAL_CAN_GetRxMessage(hcan, CAN_RX_FIFO0, &rx_header, rx_data); // 从CAN接收FIFO0中获取消息

    switch (rx_header.StdId)
    {
    case CAN_3508_M1_ID:
    case CAN_3508_M2_ID:
    case CAN_3508_M3_ID:
    case CAN_3508_M4_ID:
    case CAN_YAW_MOTOR_ID:
    case CAN_PIT_MOTOR_ID:
    case CAN_TRIGGER_MOTOR_ID:
    {
        static uint8_t i = 0;
        // 获取电机ID
        i = rx_header.StdId - CAN_3508_M1_ID;
        get_motor_measure(&motor_total[i], rx_data);
        break;
    }

    default:
    {
        break;
    }
    }
}

void CAN_cmd_gimbal(int16_t yaw, int16_t pitch, int16_t shoot, int16_t rev)
{
    uint32_t send_mail_box;                      // 发送邮箱，缓冲待发送消息，跟踪消息发送状态
    gimbal_tx_message.StdId = CAN_GIMBAL_ALL_ID; // 设置发送ID
    gimbal_tx_message.IDE = CAN_ID_STD;          // 设置发送ID格式
    gimbal_tx_message.RTR = CAN_RTR_DATA;        // 设置发送类型
    gimbal_tx_message.DLC = 0x08;                // 设置发送数据长度
    gimbal_can_send_data[0] = (yaw >> 8);
    gimbal_can_send_data[1] = yaw;
    gimbal_can_send_data[2] = (pitch >> 8);
    gimbal_can_send_data[3] = pitch;
    gimbal_can_send_data[4] = (shoot >> 8);
    gimbal_can_send_data[5] = shoot;
    gimbal_can_send_data[6] = (rev >> 8);
    gimbal_can_send_data[7] = rev;
    HAL_CAN_AddTxMessage(&GIMBAL_CAN, &gimbal_tx_message, gimbal_can_send_data, &send_mail_box); // 添加发送消息
}

void CAN_cmd_chassis(int16_t motor1, int16_t motor2, int16_t motor3, int16_t motor4)
{
    uint32_t send_mail_box;
    chassis_tx_message.StdId = CAN_CHASSIS_ALL_ID;
    chassis_tx_message.IDE = CAN_ID_STD;
    chassis_tx_message.RTR = CAN_RTR_DATA;
    chassis_tx_message.DLC = 0x08;
    chassis_can_send_data[0] = motor1 >> 8;
    chassis_can_send_data[1] = motor1;
    chassis_can_send_data[2] = motor2 >> 8;
    chassis_can_send_data[3] = motor2;
    chassis_can_send_data[4] = motor3 >> 8;
    chassis_can_send_data[5] = motor3;
    chassis_can_send_data[6] = motor4 >> 8;
    chassis_can_send_data[7] = motor4;

    HAL_CAN_AddTxMessage(&CHASSIS_CAN, &chassis_tx_message, chassis_can_send_data, &send_mail_box);
}