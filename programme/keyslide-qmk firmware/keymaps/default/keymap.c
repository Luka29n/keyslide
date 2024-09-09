#include QMK_KEYBOARD_H
#include "raw_hid.h"

bool toggle = false;

#define UART_BAUD_RATE 9600  // Exemple de baud rate


const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    [0] = LAYOUT_ortho_3x4(
        KC_F13,    KC_F14,    KC_F15,
        KC_F16,    KC_F17,    KC_F18,
        KC_F19,    KC_F20,    KC_F21,
        KC_F22,    KC_M,    KC_F24 
    )
};

bool process_record_user(uint16_t keycode, keyrecord_t *record) {
    switch (keycode) {
        case KC_M: 
            if (record->event.pressed) {
                if (toggle) {
                uint8_t data[64] = {0};  // Initialize all bytes to 0
                strcpy((char *)data, "mute");  // Copy "mute" into the array
                raw_hid_send(data, 64);

                }
            }
            return false; 
        default:
            return true; 
    }
}
