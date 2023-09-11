import time
import threading

def sender():
    frame_to_send = 0
    while True:
        # Send the frame
        print("Sender: Sending frame", frame_to_send)
        time.sleep(1)  # Simulated transmission delay
        
        # Wait for acknowledgment
        print("Sender: Waiting for acknowledgment...")
        time.sleep(1)  # Simulated transmission delay
        
        # Receive acknowledgment
        print("Sender: Frame", frame_to_send, "acknowledged")
        
        frame_to_send += 1

def receiver():
    expected_frame = 0
    while True:
        # Wait for frame
        print("Receiver: Waiting for frame...")
        time.sleep(1)  # Simulated transmission delay
        
        # Receive frame
        print("Receiver: Frame received:", expected_frame)
        time.sleep(1)  # Simulated transmission delay
        
        # Send acknowledgment
        print("Receiver: Sending acknowledgment for frame", expected_frame)
        
        expected_frame += 1
    
# Start sender and receiver processes
sender_thread = threading.Thread(target=sender)
receiver_thread = threading.Thread(target=receiver)

sender_thread.start()
receiver_thread.start()

sender_thread.join()
receiver_thread.join()
