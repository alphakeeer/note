#include "bsp_can.h"
#include "main.h"

extern CAN_HandleTypeDef hcan1;
extern CAN_HandleTypeDef hcan2;

// CAN过滤器初始化 + CAN启动 + CAN接收中断激活
void can_filter_init(void)
{
    // 初始化CAN过滤器结构体
    CAN_FilterTypeDef can_filter_st;
    can_filter_st.FilterActivation = ENABLE;                           // 启用过滤器
    can_filter_st.FilterMode = CAN_FILTERMODE_IDMASK;                  // 使用标识符屏蔽模式
    can_filter_st.FilterScale = CAN_FILTERSCALE_32BIT;                 // 使用32位过滤器
    can_filter_st.FilterIdHigh = 0x0000;                               // 过滤器标识符高位
    can_filter_st.FilterIdLow = 0x0000;                                // 过滤器标识符低位
    can_filter_st.FilterMaskIdHigh = 0x0000;                           // 过滤器屏蔽标识符高位
    can_filter_st.FilterMaskIdLow = 0x0000;                            // 过滤器屏蔽标识符低位
    can_filter_st.FilterBank = 0;                                      // 过滤器组编号
    can_filter_st.FilterFIFOAssignment = CAN_RX_FIFO0;                 // 过滤器分配给FIFO0接收缓冲区
    HAL_CAN_ConfigFilter(&hcan1, &can_filter_st);                      // 配置CAN过滤器
    HAL_CAN_Start(&hcan1);                                             // 启动CAN1
    HAL_CAN_ActivateNotification(&hcan1, CAN_IT_RX_FIFO0_MSG_PENDING); // 激活CAN1接收中断

    // 为什么can2设置的过滤器组编号为14？
    can_filter_st.SlaveStartFilterBank = 14;                           // 从14号过滤器组开始
    can_filter_st.FilterBank = 14;                                     // 过滤器组编号为14
    HAL_CAN_ConfigFilter(&hcan2, &can_filter_st);                      // 配置CAN过滤器
    HAL_CAN_Start(&hcan2);                                             // 启动CAN2
    HAL_CAN_ActivateNotification(&hcan2, CAN_IT_RX_FIFO0_MSG_PENDING); // 激活CAN2接收中断
}
