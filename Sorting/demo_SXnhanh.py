import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Hàm vẽ mảng số dưới dạng ô vuông và hiển thị tọa độ
def draw_array_quick(array, highlight=None, pivot=None, ax=None, positions=None, y_positions=None):
    ax.clear()
    ax.set_xlim(-1, len(array))
    ax.set_ylim(-2, 4)
    ax.axis('off')  # Ẩn trục
    for i, value in enumerate(array):
        # Vẽ hình chữ nhật
        if pivot is not None and i == pivot:
            color = 'yellow'  # Pivot có màu vàng
        elif highlight and i in highlight:
            color = 'red'  # Đổi chỗ có màu đỏ
        else:
            color = 'blue'  # Bình thường có màu xanh
        rect = patches.Rectangle((positions[i], y_positions[i]), 1, 1, edgecolor='black', facecolor=color)
        ax.add_patch(rect)
        # Vẽ giá trị bên trong ô
        ax.text(positions[i] + 0.5, y_positions[i] + 0.5, str(value), ha='center', va='center', fontsize=14, color='white')
        # Vẽ tọa độ (x, y) của ô
        ax.text(positions[i] + 0.5, y_positions[i] - 0.2, f"({positions[i]:.2f}, {y_positions[i]:.2f})", ha='center', va='center', fontsize=8, color='black')

# Hàm tạo hiệu ứng hoán đổi
def swap_animation_quick(array, i, j, ax, pivot):
    n_frames = 30  # Số khung hình cho hoạt ảnh
    positions = list(range(len(array)))
    y_positions = [0] * len(array)

    # Bước 1: Di chuyển lên/xuống (trục y) để tránh đè lên nhau
    for frame in range(n_frames // 2):
        y_positions[i] = frame / 10  # Di chuyển ô i lên
        y_positions[j] = -frame / 10  # Di chuyển ô j xuống
        draw_array_quick(array, highlight=[i, j], pivot=pivot, ax=ax, positions=positions, y_positions=y_positions)
        plt.pause(0.05)

    # Bước 2: Di chuyển ngang (trục x) để đổi chỗ
    x_distance = positions[j] - positions[i]  # Khoảng cách trên trục x
    step = x_distance / (n_frames // 2)  # Khoảng cách di chuyển mỗi khung hình
    for frame in range(n_frames // 2):
        positions[i] += step
        positions[j] -= step
        draw_array_quick(array, highlight=[i, j], pivot=pivot, ax=ax, positions=positions, y_positions=y_positions)
        plt.pause(0.05)

    # Bước 3: Trở về trục X (y = 0)
    for frame in range(n_frames // 2):
        y_positions[i] = max(0, y_positions[i] - 1 / 10)  # Di chuyển dần xuống
        y_positions[j] = min(0, y_positions[j] + 1 / 10)  # Di chuyển dần lên
        draw_array_quick(array, highlight=[i, j], pivot=pivot, ax=ax, positions=positions, y_positions=y_positions)
        plt.pause(0.05)

    # Bước 4: Cập nhật giá trị hoán đổi trong mảng
    array[i], array[j] = array[j], array[i]

# Hàm phân hoạch cho thuật toán QuickSort
def quick_sort_partition(array, low, high, ax, positions, y_positions):
    pivot_index = (low + high) // 2
    pivot = array[pivot_index]
    left = low
    right = high

    while left <= right:
        draw_array_quick(array, highlight=None, pivot=pivot_index, ax=ax, positions=positions, y_positions=y_positions)
        plt.pause(0.05)
        while array[left] < pivot:
            left += 1
        while array[right] > pivot:
            right -= 1
        if left <= right:
            swap_animation_quick(array, left, right, ax, pivot=pivot_index)
            left += 1
            right -= 1
    return left

# Hàm sắp xếp QuickSort trực quan
def quick_sort(array, low, high, ax, positions, y_positions):
    if low < high:
        pivot_index = quick_sort_partition(array, low, high, ax, positions, y_positions)
        quick_sort(array, low, pivot_index - 1, ax, positions, y_positions)
        quick_sort(array, pivot_index, high, ax, positions, y_positions)
    
    draw_array_quick(array, ax=ax, positions=positions, y_positions=y_positions)
    plt.pause(0.05)

# Hàm gọi thuật toán QuickSort và hiển thị kết quả
def quick_sort_visualize(array):
    fig, ax = plt.subplots(figsize=(10, 4))
    positions = list(range(len(array)))  # Vị trí ban đầu trên trục X
    y_positions = [0] * len(array)  # Vị trí trên trục Y (mặc định là 0)

    quick_sort(array, 0, len(array) - 1, ax, positions, y_positions)
    plt.show()

if __name__ == '__main__':
    array = [8, 7, 2, 1, 5, 3, 6, 4]
    quick_sort_visualize(array)
