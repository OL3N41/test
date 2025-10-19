import time

print("Powershell cmd working!")


try:
    print("Pausing for 3 seconds...")
    time.sleep(3)  # Pause for 3 seconds
    print("Resuming execution.")
except KeyboardInterrupt:
    print("\nProgram interrupted by user.")
