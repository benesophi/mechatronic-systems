# mechatronic-systems

Trabalho da disciplina SEM0541 - Projeto de Sistemas Mecatrônicos I (2026)

O projeto consiste no desenvolvimento de um manipulador RRR com uma garra no *end-effector*. O objetivo é levantar uma massa de 200 g por meio de uma teleoperação utilizando um *joystick*.

### **Requisitos**

- ESP 32 WiFi + Bluetooth
- *Joystick* com Bluetooth

## Compilação e Execução

Instale a extensão "*Remote Explorer*" no VS Code. Em seguida, clone o repositório e abra o *workspace* utilizando o VS Code. O container será automaticamente construído.

Para permitir janelas gráficas, rode o seguinte comando num terminal do *host*:

```bash
xhost +local:docker
```