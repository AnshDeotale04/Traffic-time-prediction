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

def calculate_glt_for_multiple_lanes(num_lanes):
    max_glt = 0  # Track the highest GLT among all lanes
    
    # Loop through each lane and calculate the GLT
    for lane in range(1, num_lanes + 1):
        print(f"\nCalculating for Lane {lane}:")
        queue_length = int(input(f"Enter the length of the queue for Lane {lane}: "))
        lane_glt = calculate_glt(queue_length)
        print(f"GLT for Lane {lane}: {lane_glt} seconds")
        
        # Track the maximum GLT across all lanes
        if lane_glt > max_glt:
            max_glt = lane_glt
    
    return max_glt

# Main execution
num_lanes = int(input("Enter the number of lanes: "))
overall_glt = calculate_glt_for_multiple_lanes(num_lanes)
print(f"\nOverall Green Light Time (GLT): {overall_glt} seconds")
