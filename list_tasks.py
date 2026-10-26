def directions():
    steps = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return steps


def movements():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path
def run_task2():
    print("Moving")
    steps = movements()
    print(f"{direction()} for {steps}")


