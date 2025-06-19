#include <iostream>
#include <cstring>

// State struct
struct State {
    char color[20];
    int duration;
};

// Abstract base class
class TrafficLightController {
protected:
    State* states;
    int numStates;
    int currentState;
public:
    TrafficLightController(State* s, int n) : numStates(n), currentState(0) {
        states = new State[numStates];
        for (int i = 0; i < numStates; ++i) {
            strcpy(states[i].color, s[i].color);
            states[i].duration = s[i].duration;
        }
    }
    virtual ~TrafficLightController() {
        delete[] states;
    }
    virtual void cycleStates() = 0;
};

// Basic traffic light controller
class BasicController : public TrafficLightController {
public:
    BasicController(State* s, int n) : TrafficLightController(s, n) {}
    void cycleStates() override {
        std::cout << "BasicController: ";
        State* ptr = states + currentState;
        std::cout << ptr->color << " for " << ptr->duration << "s\n";
        currentState = (currentState + 1) % numStates;
    }
};

// Pedestrian traffic light controller
class PedestrianController : public TrafficLightController {
public:
    PedestrianController(State* s, int n) : TrafficLightController(s, n) {}
    void cycleStates() override {
        std::cout << "PedestrianController: ";
        State* ptr = states + currentState;
        std::cout << ptr->color << " for " << ptr->duration << "s\n";
        currentState = (currentState + 1) % numStates;
    }
};

// Dynamic array of controllers
class ControllerManager {
    TrafficLightController** controllers;
    int count;
public:
    ControllerManager() : controllers(nullptr), count(0) {}
    ~ControllerManager() {
        for (int i = 0; i < count; ++i)
            delete controllers[i];
        delete[] controllers;
    }
    void addController(TrafficLightController* ctrl) {
        TrafficLightController** newArr = new TrafficLightController*[count + 1];
        for (int i = 0; i < count; ++i)
            newArr[i] = controllers[i];
        newArr[count] = ctrl;
        delete[] controllers;
        controllers = newArr;
        ++count;
    }
    void removeController(int index) {
        if (index < 0 || index >= count) return;
        delete controllers[index];
        TrafficLightController** newArr = new TrafficLightController*[count - 1];
        for (int i = 0, j = 0; i < count; ++i) {
            if (i != index)
                newArr[j++] = controllers[i];
        }
        delete[] controllers;
        controllers = newArr;
        --count;
    }
    void cycleAll() {
        for (int i = 0; i < count; ++i)
            controllers[i]->cycleStates();
    }
    int getCount() const { return count; }
};

// Example usage
int main() {
    // Define states for basic and pedestrian controllers
    State basicStates[] = { {"Red", 5}, {"Green", 3}, {"Yellow", 2} };
    State pedStates[] = { {"Walk", 4}, {"Don't Walk", 6} };

    ControllerManager manager;
    manager.addController(new BasicController(basicStates, 3));
    manager.addController(new PedestrianController(pedStates, 2));

    // Simulate cycles
    for (int i = 0; i < 4; ++i) {
        std::cout << "Cycle " << i + 1 << ":\n";
        manager.cycleAll();
        std::cout << std::endl;
    }

    // Remove the first controller
    manager.removeController(0);

    // Cycle again
    std::cout << "After removing first controller:\n";
    manager.cycleAll();

    return 0;
}
