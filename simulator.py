import time

def run_simulation(path):
    for step, pos in enumerate(path):
        print(f"Step {step}: Car at {pos}")
        time.sleep(0.2)
