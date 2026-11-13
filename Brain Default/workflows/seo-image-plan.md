---
type: workflow
name: SEO Kế hoạch ảnh blog
slug: seo-image-plan
status: active
description: 'Tạo bảng kế hoạch ảnh cho một bài blog hoàn chỉnh: vị trí, tên file, alt, prompt tạo ảnh.'
steps:
- agent: seo-writer
  task: |-
    Đầu vào: {{input}}
    Đầu vào gồm: slug khách | thư mục run blog | file blog hoàn chỉnh trong run.
    Đọc Projects/SEO-OPS.md và Projects/<slug>/PROJECT.md của đúng khách trong đầu vào. Chỉ làm cho khách đó. Thông tin đã có trong PROJECT.md (thị trường, ngôn ngữ, Google domain, tone, từ cấm, skill, đối thủ) thì dùng luôn, không hỏi lại; thiếu thì nói rõ cần điền mục nào vào PROJECT.md.
    Đọc toàn bộ bài. Lập bảng kế hoạch ảnh: vị trí (sau heading nào), tên file (chữ thường, gạch ngang), thẻ alt, prompt tạo ảnh. Không tạo ảnh. Alt chỉ mô tả những gì sẽ có trong ảnh, không chèn từ khóa gượng. Ghi imageplan.md vào thư mục run và thêm tên file vào mục "File trong run này" của RUN.md.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 3 dòng:
    Khách: <slug>
    Kế hoạch ảnh: <đường dẫn>
    Số ảnh: <n>
updated: '2026-11-13'
---

Một bước. Ảnh được tạo bên ngoài (ví dụ Gemini) rồi người chèn vào bài.
