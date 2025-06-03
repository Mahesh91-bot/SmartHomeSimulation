# Smart Home Simulation (Python OOP Project)

This project simulates a **Smart Home System** using Object-Oriented Programming (OOP) principles in Python. It demonstrates the use of **abstraction, encapsulation, inheritance, and polymorphism** through smart devices like lights, fans, and air conditioners.

## 📌 Features

- **Abstract Class**: `SmartDevice` defines a common interface for all smart devices.
- **Encapsulation**: All internal states (like brightness, speed, and temperature) are private.
- **Inheritance**: `SmartLight`, `SmartFan`, and `SmartAC` inherit from `SmartDevice`.
- **Polymorphism**: Each device implements its own version of the `operate()` method.
- **Safe Access**: Getters and setters are used to access and modify private attributes.

## 🔧 Devices & Defaults

| Device      | Action          | Default Setting        |
|-------------|------------------|-------------------------|
| Smart Light | Brightness       | 70%                     |
| Smart Fan   | Speed            | Medium (`Low/Medium/High`) |
| Smart AC    | Temperature      | 24°C (Range: 16–30°C)   |

## 🚀 How to Run

1. Clone or download the repository.
2. Run the script using Python:

```bash
python classic_smart_home.py
