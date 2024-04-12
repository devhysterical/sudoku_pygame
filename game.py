import pygame
import sys
import random
import time

# Khởi tạo Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 540, 590
GRID_SIZE = 9
CELL_SIZE = WIDTH // GRID_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.SysFont("comicsans", 40)
TIMER_FONT = pygame.font.SysFont("comicsans", 30)
TIMER_DURATION = (
    120  # Tùy chỉnh bộ đếm thời gian cho trò chơi theo sở thích của người chơi
)

# Khởi tạo bảng Sudoku
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

# Tạo một bảng sao lưu ban đầu để kiểm tra kết quả
original_board = [row[:] for row in board]

# Khởi tạo cửa sổ Pygame
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Game")
clock = pygame.time.Clock()

# Định vị ô đang được chọn
selected = None

# Biến thời gian
start_time = time.time()
timer_running = True

# Biến để điều khiển việc hiển thị tự giải
auto_solve_visualization = True


# Hàm kiểm tra nếu một số là hợp lệ trong ô đã chọn
def is_valid(num, pos):
    row, col = pos
    # Kiểm tra hàng
    if num in board[row]:
        return False
    # Kiểm tra cột
    if num in [board[i][col] for i in range(GRID_SIZE)]:
        return False
    # Kiểm tra ô 3x3
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    if num in [
        board[i][j]
        for i in range(start_row, start_row + 3)
        for j in range(start_col, start_col + 3)
    ]:
        return False
    return True


# Hàm giải bảng Sudoku bằng phương pháp backtracking
def solve_board():
    empty_cell = find_empty()
    if not empty_cell:
        return True
    row, col = empty_cell
    for num in range(1, 10):
        if is_valid(num, (row, col)):
            board[row][col] = num
            if auto_solve_visualization:
                draw_board()
                pygame.display.update()
                pygame.time.delay(100)
            if solve_board():
                return True
            board[row][col] = 0
            if auto_solve_visualization:
                draw_board()
                pygame.display.update()
                pygame.time.delay(100)
    # Dừng bộ đếm thời gian nếu tìm được lời giải
    global timer_running
    timer_running = False
    return False


# Hàm tìm ô trống tiếp theo trên bảng
def find_empty():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if board[i][j] == 0:
                return i, j
    return None


# Hiển thị thông báo trên màn hình
def display_message(message):
    pygame.time.delay(1000)
    window.fill(WHITE)
    text = FONT.render(message, True, BLACK)
    window.blit(
        text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2)
    )
    pygame.display.update()
    pygame.time.delay(3000)


# Ghi lại kết quả vào file text
def record_game_result(result):
    with open("D:\TriTueNhanTao_AI\sudoku_pygame\game_result.txt", "a") as file:
        file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}, {result}\n")


# Hàm để vẽ bảng Sudoku
def draw_board():
    window.fill(WHITE)
    # Vẽ các đường kẻ trên bảng
    for i in range(1, GRID_SIZE + 1):
        line_width = 7 if i % 3 == 0 else 1
        if i == GRID_SIZE:
            pygame.draw.line(
                window, BLACK, (0, HEIGHT - 50), (WIDTH, HEIGHT - 50), 3
            )  # Đường ngang cho bộ đếm thời gian
        else:
            pygame.draw.line(
                window,
                BLACK,
                (i * CELL_SIZE, 0),
                (i * CELL_SIZE, HEIGHT),
                line_width,
            )
            pygame.draw.line(
                window,
                BLACK,
                (0, i * CELL_SIZE),
                (WIDTH, i * CELL_SIZE),
                line_width,
            )

    # Đánh dấu ô đang được chọn
    if selected is not None:
        pygame.draw.rect(
            window,
            (200, 200, 255),
            (selected[1] * CELL_SIZE, selected[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE),
        )

    # Khởi tạo các số trên bảng
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if board[i][j] != 0:
                num = str(board[i][j])
                font = pygame.font.Font(None, 36)
                text = font.render(num, True, BLACK)
                text_rect = text.get_rect(
                    center=(
                        j * CELL_SIZE + CELL_SIZE // 2,
                        i * CELL_SIZE + CELL_SIZE // 2,
                    )
                )
                window.blit(text, text_rect)

    # Vẽ bộ đếm thời gian
    elapsed_time = int(time.time() - start_time)
    remaining_time = max(0, TIMER_DURATION - elapsed_time)
    minutes = remaining_time // 60
    seconds = remaining_time % 60
    timer_text = TIMER_FONT.render(f"Time: {minutes:02}:{seconds:02}", True, BLACK)
    timer_text_rect = timer_text.get_rect(center=(WIDTH // 2, HEIGHT - 25))
    window.blit(timer_text, timer_text_rect)


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if selected is not None:
                if event.key in range(pygame.K_1, pygame.K_9 + 1):
                    num = event.key - pygame.K_0
                    if (
                        is_valid(num, selected)
                        and original_board[selected[0]][selected[1]] == 0
                    ):
                        board[selected[0]][selected[1]] = num
                        selected = None
                        if all(all(cell != 0 for cell in row) for row in board):
                            display_message("Congratulations!")
                            record_game_result("Win")
                            board = [row[:] for row in original_board]
                elif event.key == pygame.K_RETURN:
                    selected = None
                    if solve_board():
                        display_message("Solution Found!")
                        record_game_result("Solved")
                elif event.key == pygame.K_BACKSPACE:
                    if (
                        selected is not None
                        and original_board[selected[0]][selected[1]] == 0
                    ):
                        board[selected[0]][selected[1]] = 0
                elif event.key == pygame.K_s:
                    selected = None
                    auto_solve_visualization = False

            elif event.key == pygame.K_RETURN:
                selected = None
                auto_solve_visualization = True
                solve_board()
            elif event.key == pygame.K_BACKSPACE:
                if (
                    selected is not None
                    and original_board[selected[0]][selected[1]] == 0
                ):
                    board[selected[0]][selected[1]] = 0
                    auto_solve_visualization = False
            elif event.key == pygame.K_s:
                auto_solve_visualization = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            selected = (pos[1] // CELL_SIZE, pos[0] // CELL_SIZE)

    # Kiểm tra xem thời gian đã hết chưa
    elapsed_time = int(time.time() - start_time)
    if elapsed_time >= TIMER_DURATION:
        display_message("Time's up! You lose.")
        record_game_result("Lose")
        board = [row[:] for row in original_board]
        start_time = time.time()
        selected = None

    draw_board()
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
