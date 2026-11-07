
# Lab 05 – Câu hỏi thảo luận

## 1. Ưu và nhược điểm của upstream-first so với release-first

Upstream-first là cách sửa lỗi trước trên nhánh phát triển chính (master), sau đó cherry-pick bản sửa sang các nhánh release bị ảnh hưởng.

Ưu điểm:
- Bảo đảm dòng phát triển chính nhận được bản sửa sớm.
- Giảm nguy cơ lỗi cũ tiếp tục tồn tại trên master.
- Thuận tiện khi nhiều bản release cần nhận cùng bản sửa.

Nhược điểm:
- Bản sửa trên master có thể phụ thuộc vào các tính năng mới.
- Khi cherry-pick sang release cũ, có thể cần điều chỉnh
  để phù hợp với mã nguồn của phiên bản đó.

Release-first là cách sửa trực tiếp trên nhánh release đang bị ảnh hưởng, sau đó lan truyền bản sửa về master và các release khác.

## 2. Nếu quên lan truyền bản sửa sang release/lab05, lệnh nào có thể phát hiện?

Có thể sử dụng:

`git cherry -v origin/release/lab05 origin/release/lab04`

Lệnh này so sánh các commit trên release/lab04 với release/lab05.

Nếu commit sửa lỗi trên release/lab04 có dấu (+), điều đó cho biết Git chưa tìm thấy bản vá tương đương trên release/lab05.

Ngoài ra, cần kiểm tra hành vi thực tế trên v1.1.0 bằng Unit Test hoặc lệnh chạy search_by_title() để xác nhận bản sửa đã hoạt động.
