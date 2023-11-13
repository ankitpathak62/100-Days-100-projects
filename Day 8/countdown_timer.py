import time

def countdown_timer(seconds):
    while seconds > 0:
        print(f"Time remaining: {seconds} seconds")
        time.sleep(1)  # Delay for 1 second
        seconds -= 1

    print("Time's up!")

def main():
    try:
        seconds = int(input("Enter the countdown time in seconds: "))
        countdown_timer(seconds)
    except ValueError:
        print("Invalid input. Please enter a valid number of seconds.")

if __name__ == "__main__":
    main() 