import matplotlib.pyplot as plt
import matplotlib.patches as patches
import networkx as nx


# Hàm vẽ cây nhị phân
def draw_binary_tree(array, ax, n, highlight_root=None, highlight_swap=None):
    ax.clear()  # Xóa nội dung trước khi vẽ lại
    G = nx.DiGraph()
    positions = {}
    edges = []

    def add_edges_and_positions(index, x, y, level_gap):
        if index >= n:  # Chỉ vẽ các phần tử trong phạm vi heap
            return
        G.add_node(index, value=array[index])
        positions[index] = (x, y)
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        if left_child < n:
            G.add_edge(index, left_child)
            edges.append((index, left_child))
            add_edges_and_positions(left_child, x - level_gap, y - 1, level_gap / 2)
        if right_child < n:
            G.add_edge(index, right_child)
            edges.append((index, right_child))
            add_edges_and_positions(right_child, x + level_gap, y - 1, level_gap / 2)

    add_edges_and_positions(0, 0, 0, 0.7)

    # Đảm bảo nút gốc luôn có màu đỏ và làm nổi bật các nút đổi chỗ
    node_colors = []
    for node in G.nodes():
        if highlight_root is not None and node == highlight_root:
            node_colors.append('red')  # Nút gốc màu đỏ
        elif highlight_swap is not None and (node == highlight_swap[0] or node == highlight_swap[1]):
            node_colors.append('yellow')  # Nút đang đổi chỗ màu vàng
        else:
            node_colors.append('skyblue')

    # Vẽ cây mà không thay đổi các đường nối
    nx.draw(G, pos=positions, ax=ax, with_labels=False, node_size=1000, node_color=node_colors, edgelist=edges)
    labels = {node: G.nodes[node]['value'] for node in G.nodes()}
    nx.draw_networkx_labels(G, pos=positions, labels=labels, ax=ax, font_size=8, font_color='black')

# Hàm di chuyển các nút
def move_node(array, i, j, ax_tree, ax_array, n):
    positions = {}
    G = nx.DiGraph()
    edges = []

    # Xây dựng cây nhị phân
    def add_edges_and_positions(index, x, y, level_gap):
        if index >= n:
            return
        G.add_node(index, value=array[index])
        positions[index] = (x, y)
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        if left_child < n:
            G.add_edge(index, left_child)
            edges.append((index, left_child))
            add_edges_and_positions(left_child, x - level_gap, y - 1, level_gap / 2)
        if right_child < n:
            G.add_edge(index, right_child)
            edges.append((index, right_child))
            add_edges_and_positions(right_child, x + level_gap, y - 1, level_gap / 2)

    add_edges_and_positions(0, 0, 0, 0.7)

    # Tạo hiệu ứng di chuyển giữa các nút
    steps = 20
    x1, y1 = positions[i]
    x2, y2 = positions[j]

    for step in range(steps + 1):
        alpha = step / steps
        x = (1 - alpha) * x1 + alpha * x2
        y = (1 - alpha) * y1 + alpha * y2

        positions[i] = (x, y)
        positions[j] = (x2 - alpha * (x2 - x1), y2 - alpha * (y2 - y1))

        node_colors = ['red' if node == i or node == j else 'skyblue' for node in G.nodes()]
        ax_tree.clear()  # Xóa cây trước khi vẽ lại
        nx.draw(G, pos=positions, ax=ax_tree, with_labels=False, node_size=1000, node_color=node_colors, edgelist=edges)
        labels = {node: G.nodes[node]['value'] for node in G.nodes()}
        nx.draw_networkx_labels(G, pos=positions, labels=labels, ax=ax_tree, font_size=8, font_color='black')

        draw_array(array, n, ax_array)
        plt.pause(0.05)  # Thời gian tạm dừng giữa mỗi bước di chuyển

# Hàm vẽ dãy số
def draw_array(array, n, ax):
    ax.clear()  # Xóa nội dung trước khi vẽ lại
    ax.set_xlim(-1, len(array))
    ax.set_ylim(-1, 2)
    ax.axis('off')

    for i in range(len(array)):
        color = 'red' if i >= n else 'blue'  # Đánh dấu phần tử đã sắp xếp
        rect = patches.Rectangle((i, 0), 1, 1, edgecolor='black', facecolor=color)
        ax.add_patch(rect)
        ax.text(i + 0.5, 0.5, str(array[i]), ha='center', va='center', fontsize=10, color='white')

# Hàm heapify với hiệu ứng di chuyển
def heapify(array, n, i, ax_tree, ax_array):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and array[left] > array[largest]:
        largest = left

    if right < n and array[right] > array[largest]:
        largest = right

    if largest != i:
        # Hiển thị các nút đổi chỗ với hiệu ứng di chuyển
        move_node(array, i, largest, ax_tree, ax_array, n)
        array[i], array[largest] = array[largest], array[i]
        draw_binary_tree(array, ax_tree, n, highlight_root=i, highlight_swap=(i, largest))
        draw_array(array, n, ax_array)
        plt.pause(1)  # Thời gian tạm dừng sau mỗi bước heapify
        heapify(array, n, largest, ax_tree, ax_array)

# Hàm heap sort với hiển thị trực quan
def heap_sort_visualize(array):
    fig, (ax_tree, ax_array) = plt.subplots(2, 1, figsize=(12, 8))  # Giảm kích thước cửa sổ figure
    n = len(array)

    # Thay đổi kích thước cửa sổ thủ công
    fig.set_size_inches(14, 10)  # Kích thước lớn hơn, có thể thay đổi theo ý muốn

    # Xây dựng heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i, ax_tree, ax_array)

    # Trích xuất từng phần tử từ heap và đặt vào cuối dãy
    for i in range(n - 1, 0, -1):
        # Hoán đổi phần tử gốc với phần tử cuối cùng
        array[0], array[i] = array[i], array[0]
        draw_binary_tree(array, ax_tree, i, highlight_root=0)  # Chỉ vẽ phần còn lại trong heap
        draw_array(array, i, ax_array)  # Vẽ mảng sau khi hoán đổi
        plt.pause(1)  # Thời gian tạm dừng sau mỗi hoán đổi

        # Chờ 1 giây sau khi cập nhật cây heap trước khi cho phần tử vào mảng
        plt.pause(1)  # Chờ 1 giây
        draw_array(array, n, ax_array)  # Vẽ lại mảng với phần tử gốc đã được hoán đổi

        heapify(array, i, 0, ax_tree, ax_array)

    draw_binary_tree([], ax_tree, 0)  # Vẽ cây trống khi hoàn thành
    draw_array(array, 0, ax_array)
    plt.show()

if __name__ == '__main__':
    array = [3, 7, 6, 2, 4, 9, 1, 0]
    heap_sort_visualize(array)
