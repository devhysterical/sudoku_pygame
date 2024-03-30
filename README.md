# Hướng dẫn cài đặt Sudoku Game

## Giới thiệu

Sudoku Game là một trò chơi Sudoku cổ điển được viết bằng ngôn ngữ lập trình Python, sử dụng thư viện Pygame để tạo giao diện đồ họa.

## Yêu cầu hệ thống

- Python 3.x đã được cài đặt trên máy tính của bạn.
- Thư viện Pygame đã được cài đặt.

## Cài đặt

1. **Cài đặt Python**: Nếu bạn chưa cài đặt Python, bạn có thể tải xuống từ trang web chính thức của Python theo đường dẫn [python.org](https://www.python.org/downloads/) và làm theo hướng dẫn cài đặt.
2. **Cài đặt Pygame**: Bạn có thể cài đặt Pygame bằng cách mở cửa sổ dòng lệnh/terminal và chạy lệnh sau:

   ```
   pip install pygame
   ```

   Hoặc nếu bạn sử dụng `pip3`:

   ```
   pip3 install pygame
   ```

## Chạy trò chơi

1. Tải mã nguồn từ repository GitHub của Sudoku Game.
2. Mở terminal/command prompt và điều hướng đến thư mục chứa mã nguồn của trò chơi Sudoku.
3. Chạy file `sudoku_game.py` bằng cách gõ lệnh sau:

   ```
   python sudoku_game.py
   ```

   Hoặc nếu bạn sử dụng Python 3:

   ```
   python3 sudoku_game.py
   ```

4. Trò chơi Sudoku sẽ mở trong cửa sổ mới và bạn có thể bắt đầu chơi.

## Hướng dẫn một vài tính năng của trò chơi

- Nhấn phím `1` đến `9` để chọn giá trị cần điền vào ô trống.
- Nhấn phím `Delete` hoặc `Backspace` để xóa giá trị trong ô trống.
- Nhấn phím `Enter` để thực hiện tự động giải Sudoku.

## Lưu ý

- Sau khi cài đặt mã nguồn về máy, hãy mở file `game.py` và tìm đến dòng số 121 để thay đổi đường dẫn của file `game_result.txt` thành đường dẫn tuyệt đối trên máy của bạn.
- File `game_result.txt` sẽ chứa kết quả của người chơi sau khi chơi xong. Nếu không thay đổi đường dẫn, file này sẽ được lưu trong thư mục chứa mã nguồn của trò chơi Sudoku.

## Good luck & Have fun!
