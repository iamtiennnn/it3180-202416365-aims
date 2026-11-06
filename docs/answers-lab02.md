
# Lab 02 – Câu hỏi thảo luận

## 1. Vì sao phải đồng bộ master trước khi tạo PR?

Việc đồng bộ master giúp nhánh tính năng nhận được những thay đổi mới nhất của dự án, từ đó phát hiện xung đột sớm và kiểm tra khả năng tương thích trước khi tích hợp.

## 2. Khi nào không được rebase?

Không nên rebase những commit đã chia sẻ khi việc viết lại lịch sử có thể ảnh hưởng đến những người đang sử dụng các commit đó.

Rebase tạo lại các commit với SHA mới. Nếu rebase rồi force push một nhánh dùng chung, những người khác có thể gặp khó khăn khi đồng bộ lịch sử.

Rebase phù hợp hơn với các commit chưa chia sẻ hoặc khi các cộng tác viên đã thống nhất việc viết lại lịch sử.

## 3. Feature branch khác Topic branch như thế nào?

Feature branch chủ yếu được sử dụng để phát triển chức năng mới của phần mềm, ví dụ:

- feature/cart-print
- feature/search-by-title

Topic branch được sử dụng cho một công việc hoặc chủ đề cụ thể, không nhất thiết liên quan đến tính năng của chương trình, ví dụ:

- topic/pr-template
- topic/use-case-diagram

