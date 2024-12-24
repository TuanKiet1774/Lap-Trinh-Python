import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Hàm vẽ mảng số dưới dạng ô vuông
def draw_array_as_squares(array, ax=None, highlight=None, positions=None, y_positions=None):
    ax.clear()
    ax.set_xlim(-1, len(array))
    ax.set_ylim(-2, 4)
    ax.axis('off')  # Ẩn trục
    for i, value in enumerate(array):
        x = positions[i]
        y = y_positions[i]
        # Tô màu các số đang di chuyển thành màu đỏ
        color = 'red' if highlight and i in highlight else 'blue'
        rect = patches.Rectangle((x, y), 1, 1, edgecolor='black', facecolor=color)
        ax.add_patch(rect)
        ax.text(x + 0.5, y + 0.5, str(value), ha='center', va='center', fontsize=14, color='white')
        ax.text(positions[i] + 0.5, y_positions[i] - 0.2, f"({positions[i]:.2f}, {y_positions[i]:.2f})", ha='center', va='center', fontsize=8, color='black')

# Hàm hợp nhất hai mảng con
def merge(array, start, mid, end, ax, positions, y_positions):
    left = array[start:mid + 1]
    right = array[mid + 1:end + 1]

    l_idx = 0
    r_idx = 0
    sorted_idx = start

    # Tăng vị trí y của mảng con để hiển thị rõ các bước hợp nhất
    for i in range(start, end + 1):
        y_positions[i] -= 1

    draw_array_as_squares(array, ax=ax, positions=positions, y_positions=y_positions)
    plt.pause(0.5)

    # Hợp nhất hai mảng con
    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] <= right[r_idx]:
            array[sorted_idx] = left[l_idx]
            highlight = [sorted_idx]  # Highlight phần tử đang được đưa vào vị trí mới
            l_idx += 1
        else:
            array[sorted_idx] = right[r_idx]
            highlight = [sorted_idx]  # Highlight phần tử đang được đưa vào vị trí mới
            r_idx += 1

        # Cập nhật y_positions cho cả hai phần tử đang so sánh
        y_positions[sorted_idx] += 1
        draw_array_as_squares(array, ax=ax, highlight=highlight, positions=positions, y_positions=y_positions)
        plt.pause(0.5)
        sorted_idx += 1

    # Copy phần còn lại của mảng con bên trái
    while l_idx < len(left):
        array[sorted_idx] = left[l_idx]
        y_positions[sorted_idx] += 1  # Đưa giá trị hợp nhất lên hàng trên
        highlight = [sorted_idx]
        draw_array_as_squares(array, ax=ax, highlight=highlight, positions=positions, y_positions=y_positions)
        plt.pause(0.5)
        l_idx += 1
        sorted_idx += 1

    # Copy phần còn lại của mảng con bên phải
    while r_idx < len(right):
        array[sorted_idx] = right[r_idx]
        y_positions[sorted_idx] += 1  # Đưa giá trị lên hàng trên
        highlight = [sorted_idx]
        draw_array_as_squares(array, ax=ax, highlight=highlight, positions=positions, y_positions=y_positions)
        plt.pause(0.5)
        r_idx += 1
        sorted_idx += 1

# Hàm đệ quy cho Merge Sort
def merge_sort_recursive(array, start, end, ax, positions, y_positions):
    if start < end:
        mid = (int)((start + end) / 2)

        # Tách mảng con bên trái
        merge_sort_recursive(array, start, mid, ax, positions, y_positions)

        # Tách mảng con bên phải
        merge_sort_recursive(array, mid + 1, end, ax, positions, y_positions)

        # Hợp nhất hai mảng con
        merge(array, start, mid, end, ax, positions, y_positions)

# Hàm trực quan hóa Merge Sort
def merge_sort_visualize(array):
    fig, ax = plt.subplots(figsize=(12, 8))
    positions = list(range(len(array)))  # Vị trí x của các phần tử
    y_positions = [0] * len(array)  # Vị trí y ban đầu

    draw_array_as_squares(array, ax=ax, positions=positions, y_positions=y_positions)
    plt.pause(0.5)

    merge_sort_recursive(array, 0, len(array) - 1, ax, positions, y_positions)

    draw_array_as_squares(array, ax=ax, positions=positions, y_positions=y_positions)
    plt.show()

if __name__ == '__main__':
    array = [1, 5, 3, 9, 4, 7, 6]
    merge_sort_visualize(array)
