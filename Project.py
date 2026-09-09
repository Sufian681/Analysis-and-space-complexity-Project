def binary_search_recursive(seats, target, low, high):
    if low > high: return -1
    mid = (low + high) // 2
    if seats[mid] == target: return mid
    if seats[mid] < target: return binary_search_recursive(seats, target, mid + 1, high)
    return binary_search_recursive(seats, target, low, mid - 1)

train_seats = [12, 25, 34, 48, 55, 67, 89, 101, 115]
target_seat = 55

print("Recursive Index:", binary_search_recursive(train_seats, target_seat, 0, len(train_seats) - 1))