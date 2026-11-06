Lab 01 – Câu hỏi thảo luận

1. Vì sao dùng git mv?
git mv thực hiện thao tác đổi vị trí/đổi tên tệp và cập nhật trạng thái trong working tree/staging. Git vẫn lưu lịch sử theo commit; khi xem bằng git log --follow -- <file>, Git có thể nhận diện nội dung tệp được chuyển sang đường dẫn mới. Về bản chất, Git phát hiện rename dựa trên độ tương đồng nội dung khi so sánh commit, nên git mv không tạo ra một loại đối tượng lịch sử đặc biệt; nó giúp thao tác rõ ràng và giảm nguy cơ quên git add đường dẫn mới/xóa đường dẫn cũ.

2. release/lab01 có phải baseline?
Có, đây là một trạng thái mã nguồn đã được đóng băng và thống nhất để nộp bài.

3. Vì sao không commit thẳng master dù làm một mình?
Pull Request lưu mục đích, phạm vi thay đổi và bằng chứng kiểm thử; nó cũng cho cơ hội xem diff trước khi hợp nhất. Quy tắc một đường vào master giúp quy trình có thể kiểm toán và giữ nhất quán khi sau này có thêm cộng tác viên. Khi làm một mình, có thể đặt số approval bắt buộc là 0 nhưng vẫn đi qua PR.
