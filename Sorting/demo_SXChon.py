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
def swap_animation_selection(array, i, j, ax):
    n_frames = 30  # Số khung hình cho hoạt ảnh
    positions = list(range(len(array)))
    y_positions = [0] * len(array)


    # Di chuyển lên/xuống (trục y) để tránh đè lên nhau
    for frame in range(n_frames // 2):
        y_positions[i] = frame / 10  # Di chuyển lên
        y_positions[j] = -frame / 10  # Di chuyển xuống
        
        draw_array_as_squares(array, highlight=[i, j], ax=ax, positions=positions, y_positions=y_positions)
        plt.pause(0.05)
    


    # Di chuyển ngang từng bước để tránh đè lên nhau
    while positions[i] < positions[j]:
        distance = positions[j] - positions[i]  # Tính khoảng cách giữa hai ô
        dis = 0.05  # Di chuyển mỗi lần 0.05 đơn vị
        # Di chuyển dần dần cho tới khi di chuyển đủ khoảng cách
        while distance > 0:
            if distance < dis:
                dis = distance  # Nếu khoảng cách nhỏ hơn 0.05, chỉ di chuyển đủ khoảng cách còn lại
            positions[i] += dis  # Di chuyển ô i qua phải
            positions[j] -= dis  # Di chuyển ô j qua trái
            distance -= dis  # Cập nhật khoảng cách còn lại
            draw_array_as_squares(array, highlight=[i, j], ax=ax, positions=positions, y_positions=y_positions)
            plt.pause(0.05)
            
    #Di chuyển về vị trí mới
    for frame in range(n_frames):
        # Di chuyển ô i xuống (trở về trục x nếu ô i ở trên)
        if y_positions[i] > 0:
            y_positions[i] -= 0.1  # Di chuyển xuống từng bước nhỏ đến 0
            if y_positions[i] < 0:  # Đảm bảo không đi quá trục x
                y_positions[i] = 0
        
        # Di chuyển ô j lên (trở về trục x nếu ô j ở dưới)
        if y_positions[j] < 0:
            y_positions[j] += 0.1  # Di chuyển lên từng bước nhỏ đến 0
            if y_positions[j] > 0:  # Đảm bảo không đi quá trục x
                y_positions[j] = 0
        
        draw_array_as_squares(array, highlight=[i, j], ax=ax, positions=positions, y_positions=y_positions)
        plt.pause(0.05)


    
    # Hoán đổi vị trí các ô theo đúng vị trí của nhau
    target_pos_i, target_pos_j = positions[j], positions[i]
    positions[i] = target_pos_j
    positions[j] = target_pos_i

    # Hoán đổi giá trị sau khi các ô đã di chuyển đúng vị trí
    array[i], array[j] = array[j], array[i]

def selection_sort_visualize(array):
    fig, ax = plt.subplots(figsize=(10, 4))
    for i in range(len(array)):
        min_idx = i
        # Tìm phần tử nhỏ nhất trong mảng còn lại
        for j in range(i + 1, len(array)):
            draw_array_as_squares(array, highlight=[i, j], ax=ax, positions=list(range(len(array))), y_positions=[0] * len(array))
            plt.pause(0.5)
            if array[j] < array[min_idx]:
                min_idx = j
        # Hoán đổi phần tử nhỏ nhất với phần tử đầu tiên
        if min_idx != i:
            swap_animation_selection(array, i, min_idx, ax)
        draw_array_as_squares(array, highlight=[], ax=ax, positions=list(range(len(array))), y_positions=[0] * len(array))
    plt.show()

if __name__ == '__main__':
    array = [8, 5, 2, 7, 3, 1, 4]
    selection_sort_visualize(array)