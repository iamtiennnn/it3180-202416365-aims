
# Lab 04 – Câu hỏi thảo luận

## 1. Vì sao release/* không merge ngược vào master?

Trong Release Flow của học phần, master là nhánh phát triển chính, còn release/* dùng để lưu và bảo trì các phiên bản đã phát hành.

Những thay đổi riêng trên release, chẳng hạn cập nhật phiên bản hoặc hotfix, không nên merge toàn bộ ngược vào master vì có thể đưa những thay đổi không phù hợp vào dòng phát triển chính.

Nếu cần lan truyền bản sửa lỗi, có thể sử dụng cherry-pick để chọn đúng commit cần thiết.

## 2. So sánh Release Flow và GitFlow

Release Flow sử dụng master làm nhánh phát triển chính. Các nhánh feature, bugfix và topic được tích hợp vào master thông qua Pull Request.

Nhánh release được tạo từ master để đóng băng và bảo trì phiên bản phát hành.

GitFlow có cấu trúc phức tạp hơn, thường sử dụng main và develop làm hai nhánh dài hạn.

Feature branch thường được tích hợp vào develop, trong khi release và hotfix được quản lý theo quy trình riêng.

Release Flow đơn giản hơn và phù hợp với việc phát hành theo từng mốc ngắn.

## 3. Vì sao phát hành 1.0.0 thay vì 0.4.0?

Theo Semantic Versioning, các phiên bản 0.y.z thường được sử dụng trong giai đoạn phát triển ban đầu, khi phần mềm chưa được xem là ổn định.

Phiên bản 1.0.0 đánh dấu mốc công bố giao diện và chức năng chính thức của phần mềm.

Vì vậy, việc tăng lên 1.0.0 thể hiện mốc phát hành chính thức, thay vì chỉ tăng phiên bản phát triển lên 0.4.0.
