import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Hàm vẽ mảng số dưới dạng ô vuông và hiển thị tọa độ
def draw_array_as_squares(array, highlight=None, ax=None, positions=None, y_positions=None):
    ax.clear()
    ax.set_xlim(-1, len(array))
    ax.set_ylim(-2, 4)
    ax.axis('off')  # Ẩn trục
    for i, value in enumerate(array):
        # Vẽ hình chữ nhật
        color = 'red' if highlight and i in highlight else 'blue'
        rect = patches.Rectangle((positions[i], y_positions[i]), 1, 1, edgecolor='black', facecolor=color)
        ax.add_patch(rect)
        # Vẽ giá trị bên trong ô
        ax.text(positions[i] + 0.5, y_positions[i] + 0.5, str(value), ha='center', va='center', fontsize=14, color='white')
        # Vẽ tọa độ (x, y) của ô
        ax.text(positions[i] + 0.5, y_positions[i] - 0.2, f"({positions[i]:.2f}, {y_positions[i]:.2f})", ha='center', va='center', fontsize=8, color='black')

# Hàm tạo hiệu ứng hoán đổi
# Hàm tạo hiệu ứng hoán đổi (sửa lỗi)
def swap_animation_insertion(array, i, j, ax):
    n_frames = 30  # Số khung hình cho hoạt ảnh
    positions = list(range(len(array)))
    y_positions = [0] * len(array)

    # Bước 1: Di chuyển lên/xuống (trục y) để tránh đè lên nhau
    for frame in range(n_frames // 2):
        y_positions[i] = frame / 15  # Di chuyển ô i lên
        y_positions[j] = -frame / 15  # Di chuyển ô j xuống
        draw_array_as_squares(array, highlight=[i, j], ax=ax, positions=positions, y_positions=y_positions)
        plt.pause(0.05)

    # Bước 2: Di chuyển ngang (trục x) để đổi chỗ
    x_distance = positions[j] - positions[i]  # Khoảng cách trên trục x
    step = x_distance / (n_frames // 2)  # Khoảng cách di chuyển mỗi khung hình
    for frame in range(n_frames // 2):
        positions[i] += step
        positions[j] -= step
        draw_array_as_squares(array, highlight=[i, j], ax=ax, positions=positions, y_positions=y_positions)
        plt.pause(0.05)

    # Bước 3: Trở về trục X (y = 0)
    for frame in range(n_frames // 2):
        y_positions[i] = max(0, y_positions[i] - 1 / 15)  # Di chuyển dần xuống
        y_positions[j] = min(0, y_positions[j] + 1 / 15)  # Di chuyển dần lên
        draw_array_as_squares(array, highlight=[i, j], ax=ax, positions=positions, y_positions=y_positions)
        plt.pause(0.05)

    # Bước 4: Cập nhật giá trị hoán đổi trong mảng
    array[i], array[j] = array[j], array[i]



# Hàm trực quan hóa thuật toán insertion sort
def insertion_sort_visualize(array):
    fig, ax = plt.subplots(figsize=(10, 4))
    positions = list(range(len(array)))  # Vị trí ban đầu trên trục X
    y_positions = [0] * len(array)  # Vị trí trên trục Y (mặc định là 0)

    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        # Di chuyển các phần tử lớn hơn key lên một vị trí
        while j >= 0 and array[j] > key:
            swap_animation_insertion(array, j + 1, j, ax)
            j -= 1

        # Cập nhật vị trí mới cho key
        array[j + 1] = key

    # Vẽ lại toàn bộ mảng sau khi sắp xếp xong
    draw_array_as_squares(array, ax=ax, positions=positions, y_positions=y_positions)
    plt.show()

    

if __name__ == '__main__':
    array = [8, 5, 2, 7, 3, 1, 4]
    insertion_sort_visualize(array)
    
