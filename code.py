def calculate_glt(queue_length):
    # Penalty for vehicle categories
    category_penalty = {'A': 0, 'B': 2, 'C': 5}
    
    # Penalty for queue sections
    section_penalty = [0, 5, 10]  # Alpha: 0, Beta: 5, Gamma: 10

    total_time = 0

    # Loop to take inputs for each vehicle in the queue
    for i in range(1, queue_length + 1):
        vehicle_category = input(f"Enter Category of Vehicle {i} (A=2 wheeler, B=Car, C=Bus/Truck): ").upper()

        # Check which section the vehicle is in (Alpha, Beta, or Gamma)
        if i <= 3:
            section_time = section_penalty[0]  # Alpha
        elif 4 <= i <= 7:
            section_time = section_penalty[1]  # Beta
        else:
            section_time = section_penalty[2]  # Gamma
        
        # Calculate time for each vehicle (category penalty + section penalty)
        vehicle_time = category_penalty[vehicle_category] + section_time
        total_time += vehicle_time
    
    # Determine GLT based on the total time
    if total_time < 20:
        return 20  # Minimum green light time
    elif total_time > 40:
        return 40  # Maximum green light time
    else:
        return total_time  # Total time within range

# Main execution
queue_length = int(input("Enter the length of the queue: "))
glt = calculate_glt(queue_length)
print(f"Green Light Time (GLT): {glt} seconds")
