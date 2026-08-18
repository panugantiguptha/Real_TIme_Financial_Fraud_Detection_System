import subprocess

def main():
    print("🎯 Starting Real-Time Fraud Detection System...")
    subprocess.run(["python", "train_model.py"])
    subprocess.run(["python", "stream_simulator.py"])

if __name__ == "__main__":
    main()
