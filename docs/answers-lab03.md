
# Lab 03 – Câu hỏi thảo luận

## 1. Merge base là gì?

Merge base là commit tổ tiên chung tốt nhất của hai nhánh trong lịch sử Git.
Git sử dụng merge base làm mốc để so sánh các thay đổi trên từng nhánh khi thực hiện merge ba chiều.


## 2. Vì sao master/release/* phải sử dụng revert?

Master và release/* thường là những nhánh đã được chia sẻ hoặc dùng làm baseline của dự án.

Sử dụng reset kết hợp force push có thể viết lại lịch sử và ảnh hưởng đến các thành viên đang sử dụng repository.

Ngược lại, git revert tạo một commit mới để đảo ngược thay đổi của commit trước đó mà không xóa lịch sử.

