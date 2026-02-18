# Traffic Light Optimizer 🚦

A Python-based algorithm that calculates optimal green light timing for traffic signals based on real-time queue analysis...

## 📋 Overview

This project addresses the common problem of inefficient traffic light timing in modern cities. Instead of using fixed time intervals, this algorithm dynamically calculates green light duration based on:
- Number of vehicles in queue
- Vehicle types (2-wheelers, cars, buses/trucks)
- Queue position (distance from intersection)

## 🎯 Problem Statement

In today's fast-paced world, waiting at traffic lights with inefficient timing is a major inconvenience. Traditional traffic signals use fixed timers that don't account for actual traffic flow, leading to:
- Unnecessary waiting when traffic is light
- Insufficient clearing time during heavy traffic
- Poor optimization across all four terminals of an intersection

## 💡 Solution

This algorithm uses a penalty-based system to calculate the optimal **Green Light Time (GLT)**:

### Vehicle Categories
- **Category A** (2-wheelers): 0 seconds penalty
- **Category B** (Cars): 2 seconds penalty  
- **Category C** (Buses/Trucks): 5 seconds penalty

### Queue Sections
The waiting area is divided into three sections based on distance from the zebra crossing:
- **Alpha** (positions 1-3): 0 seconds penalty
- **Beta** (positions 4-7): 5 seconds penalty
- **Gamma** (positions 8+): 10 seconds penalty

### GLT Calculation
```
GLT = Sum of (Vehicle Category Penalty + Queue Section Penalty) for all vehicles
```

**Constraints:**
- Minimum GLT: 20 seconds (even with no traffic)
- Maximum GLT: 40 seconds (prevents indefinite waiting)

## 🚀 Features

- **Single Lane Mode**: Calculate GLT for one traffic lane
- **Multiple Lane Mode**: Calculate GLT for multiple lanes and determine the maximum required time
- **User-friendly CLI**: Simple command-line interface for input

## 📁 Files

- `code.py` - Single lane traffic light calculator
- `Multiple_Lane.py` - Extended version supporting multiple lanes
- `README.md` - Project documentation

## 🛠️ Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/traffic-light-optimizer.git
cd traffic-light-optimizer
```

2. Ensure you have Python 3.x installed:
```bash
python --version
```

## 📖 Usage

### Single Lane Mode
```bash
python code.py
```

**Example:**
```
Enter the length of the queue: 5
Enter Category of Vehicle 1 (A=2 wheeler, B=Car, C=Bus/Truck): B
Enter Category of Vehicle 2 (A=2 wheeler, B=Car, C=Bus/Truck): A
Enter Category of Vehicle 3 (A=2 wheeler, B=Car, C=Bus/Truck): C
Enter Category of Vehicle 4 (A=2 wheeler, B=Car, C=Bus/Truck): B
Enter Category of Vehicle 5 (A=2 wheeler, B=Car, C=Bus/Truck): A
Green Light Time (GLT): 24 seconds
```

### Multiple Lane Mode
```bash
python Multiple_Lane.py
```

**Example:**
```
Enter the number of lanes: 2
Calculating for Lane 1:
Enter the length of the queue for Lane 1: 3
...
Overall Green Light Time (GLT): 25 seconds
```

## 🧮 Algorithm Logic

The algorithm follows these steps:

1. Accept queue length input
2. For each vehicle in the queue:
   - Get vehicle category (A, B, or C)
   - Determine queue section based on position
   - Calculate penalty: `category_penalty + section_penalty`
3. Sum all penalties to get total time
4. Apply constraints (min: 20s, max: 40s)
5. Return Green Light Time (GLT)

For multiple lanes, the system calculates GLT for each lane and uses the maximum value to ensure all lanes clear optimally.

## 🎓 Learning Outcomes

This project demonstrates:
- Python fundamentals (functions, loops, conditionals)
- Algorithm design and optimization
- Real-world problem solving
- CLI input/output handling
- Code organization and documentation

## 🔮 Future Enhancements

- Integration with camera/sensor data for automatic vehicle detection
- Machine learning model to predict traffic flow patterns
- Real-time adjustment based on pedestrian crossing times
- Support for emergency vehicle priority
- Data visualization of traffic patterns

## 🤝 Contributing

This is a college project created for learning purposes. Feel free to fork and experiment!

## 📝 License

MIT License - Feel free to use this code for educational purposes.

## 👨‍💻 Author

Created as a first-year college project exploring traffic optimization algorithms.

---

**Note:** The penalty values and time constraints used in this project are assumptions. In a real-world implementation, these would be calibrated using actual traffic data and vehicle clearance times.
