#include <stdio.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "freertos/semphr.h"
#include "driver/gpio.h"
#include "freertos/queue.h"
#include "esp_log.h"


#define LED_GPIO GPIO_NUM_8   // CHANGE for your board
#define BUTTON_GPIO GPIO_NUM_10 // CHANGE for your board

static const char *TAG = "HearbeatApp";
volatile bool error[7] = {false, false, false, false, false, false};

static QueueHandle_t q_numbers;
static QueueHandle_t q_errors;
static SemaphoreHandle_t shared_counter;

struct DataPacket {
    int id;
    float value;
};

struct ErrorStatus {
    int task_id;
    bool error_state;
};

static void button_task1(void *pvParameters)
{
    gpio_reset_pin(BUTTON_GPIO);
    gpio_set_direction(BUTTON_GPIO, GPIO_MODE_INPUT);
    gpio_set_pull_mode(BUTTON_GPIO, GPIO_PULLUP_ONLY);
    float pressed_time = 0.0f;

    while (1) {
        bool current_state = !gpio_get_level(BUTTON_GPIO); // Active low
        if (current_state) {
            pressed_time += 0.05f; // Simulating time increment
        } 
        else if (!current_state && pressed_time > 0.0f) {
            ESP_LOGI(TAG, "Button 1 pressed for %f seconds", pressed_time);
            
            struct ErrorStatus status = {5, false};
            xQueueSend(q_errors, &status, pdMS_TO_TICKS(10));
            
            pressed_time = 0.0f;
        }
        
        vTaskDelay(pdMS_TO_TICKS(50)); // Polling delay
    }
}

static void button_task2(void *pvParameters)
{
    gpio_reset_pin(BUTTON_GPIO);
    gpio_set_direction(BUTTON_GPIO, GPIO_MODE_INPUT);
    gpio_set_pull_mode(BUTTON_GPIO, GPIO_PULLUP_ONLY);
    float pressed_time = 0.0f;

    while (1) {
        bool current_state = !gpio_get_level(BUTTON_GPIO); // Active low
        if (current_state) {
            pressed_time += 0.05f; // Simulating time increment
        }
        else if (!current_state && pressed_time > 0.0f) {
            ESP_LOGI(TAG, "Button 2 pressed for %f seconds", pressed_time);
            
            struct ErrorStatus status = {6, false};
            xQueueSend(q_errors, &status, pdMS_TO_TICKS(10));
            
            pressed_time = 0.0f;
        }
        
        vTaskDelay(pdMS_TO_TICKS(50)); // Polling delay
    }
}

static void producer_task(void *pvParameters)
{
    struct DataPacket packet;
    packet.id = 0;
    packet.value = 0.0f;
    while (1) {
       packet.id=rand()%1000;
       packet.value=(float)(rand()%1000)/10.0f;

        // Send to queue; wait up to 50ms if full
        if (xQueueSend(q_numbers, &packet, pdMS_TO_TICKS(50)) == pdPASS) {
            struct ErrorStatus status = {3, false};
            xQueueSend(q_errors, &status, pdMS_TO_TICKS(10));
            ESP_LOGI(TAG, "Produced %d with value %f", packet.id, packet.value);
        } else {
            struct ErrorStatus status = {3, false};
            xQueueSend(q_errors, &status, pdMS_TO_TICKS(10));
            ESP_LOGW(TAG, "Queue full, dropped %d with value %f", packet.id, packet.value);
        }

        vTaskDelay(pdMS_TO_TICKS(200));
    }
}

static void consumer_task(void *pvParameters)
{
     struct DataPacket packet_recv;

    while (1) {
        // Wait up to 1000ms for data
        if (xQueueReceive(q_numbers, &packet_recv, pdMS_TO_TICKS(1500)) == pdPASS) {
            struct ErrorStatus status = {4, false};
            xQueueSend(q_errors, &status, pdMS_TO_TICKS(10));
            ESP_LOGI(TAG, "Consumed %d with value %f", packet_recv.id, packet_recv.value);
        } else {
            struct ErrorStatus status = {4, false};
            xQueueSend(q_errors, &status, pdMS_TO_TICKS(10));
            ESP_LOGW(TAG, "No data in 1s");
        }
    }
}

static void heartbeat_task(void *pvParameters)
{
    while (1) {
        struct ErrorStatus status = {0, false};
        xQueueSend(q_errors, &status, pdMS_TO_TICKS(10));
        ESP_LOGI(TAG, "alive");
        vTaskDelay(pdMS_TO_TICKS(2000));
    }
}

static void hearbeatLED_task(void *pvParameters)
{
    gpio_reset_pin(LED_GPIO);
    gpio_set_direction(LED_GPIO, GPIO_MODE_OUTPUT);

    while (1) {
        struct ErrorStatus status = {2, false};
        xQueueSend(q_errors, &status, pdMS_TO_TICKS(10));
        gpio_set_level(LED_GPIO, 1);
        vTaskDelay(pdMS_TO_TICKS(300));
        gpio_set_level(LED_GPIO, 0);
        vTaskDelay(pdMS_TO_TICKS(300));
    }
}

static void bpm_task(void *pvParameters){
    while (1) {
        struct ErrorStatus status = {1, false};
        xQueueSend(q_errors, &status, pdMS_TO_TICKS(10));
        printf("BPM: %d\n", rand()%40 + 60);
        vTaskDelay(pdMS_TO_TICKS(500));
    }
}

static void error_task(void *pvParameters)
{
    struct ErrorStatus status;
    while (1) {
        if (xQueueReceive(q_errors, &status, pdMS_TO_TICKS(100)) == pdPASS) {
            if (xSemaphoreTake(shared_counter, pdMS_TO_TICKS(10)) == pdTRUE) {
                error[status.task_id] = status.error_state;
                xSemaphoreGive(shared_counter);
            }
        }
    }
}

void app_main(void)
{
    // Create mutex for shared resources
    shared_counter = xSemaphoreCreateMutex();
    if (shared_counter == NULL) {
        ESP_LOGE(TAG, "Mutex create failed");
        return;
    }
    
     q_numbers = xQueueCreate(5, sizeof(struct DataPacket)); // length 5
    if (q_numbers == NULL) {
        ESP_LOGE(TAG, "Queue create failed");
        return;
    }

    q_errors = xQueueCreate(10, sizeof(struct ErrorStatus));
    if (q_errors == NULL) {
        ESP_LOGE(TAG, "Error queue create failed");
        return;
    }

    xTaskCreate(error_task, "error_task", 2048, NULL, 0, NULL);
    xTaskCreate(heartbeat_task, "heartbeat", 2048, NULL, 0, NULL);
    xTaskCreate(bpm_task, "bpm_task", 2048, NULL, 1, NULL);
    xTaskCreate(hearbeatLED_task, "hearbeatLED_task", 2048, NULL, 1, NULL);
    xTaskCreate(producer_task, "producer_task", 2048, NULL, 2, NULL);
    xTaskCreate(consumer_task, "consumer_task", 2048, NULL, 2, NULL);
    xTaskCreate(button_task1, "button_task1", 2048, NULL, 3, NULL);
    xTaskCreate(button_task2, "button_task2", 2048, NULL, 3, NULL);

}