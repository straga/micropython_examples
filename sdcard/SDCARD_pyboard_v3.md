SDCARD STM32 pyboard v3 clone


![1c85370bdda8c98296b312073a906704.png](./_resources/2a8f104dea9b4c89b40d23852b50707f.png)

SD card  128MB
1. Make portion: for example fdisk (Linux)
![b8b70295fd779deeac898277e58ebac6.png](./_resources/82320f5af4884118a6183a5f96a3a5f1.png)

3. git clone repo micropython and install toolchain for STM32 (Linux)

4. Copy: micropython/ports/stm32/boards/PYBV3 to micropython/ports/stm32/boards/PYBV3_green
5. Change: micropython/ports/stm32/boards/PYBV3_green/mpconfigboard.h
FROM
// SD card detect switch
`#define MICROPY_HW_SDCARD_DETECT_PIN        (pin_C13)`
`#define MICROPY_HW_SDCARD_DETECT_PULL       (GPIO_PULLDOWN)`
`#define MICROPY_HW_SDCARD_DETECT_PRESENT    (GPIO_PIN_SET)`
TO
// SD card detect switch
`#define MICROPY_HW_SDCARD_DETECT_PIN        (pin_C13)`
`#define MICROPY_HW_SDCARD_DETECT_PULL       (GPIO_PULLUP)`
`#define MICROPY_HW_SDCARD_DETECT_PRESENT    (GPIO_PIN_RESET)`
6.  make BOARD=PYBV3_green
7. Flash dfu
8. Insert SD in STM32 and connect USB. Now usb drive it is SDCARD on stm32
![14f678ed8717538f451b2c29344587d7.png](./_resources/a4e4ad70557d4e159ca4608bbc51f767.png)
