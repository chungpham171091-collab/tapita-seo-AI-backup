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
    Đầu vào gồm: slug khách | file blog hoàn chỉnh.
    Đọc Projects/SEO-OPS.md và Projects/<slug>/PROJECT.md của đúng khách trong đầu vào. Chỉ làm cho khách đó.
    Đọc toàn bộ bài. Lập bảng kế hoạch ảnh: vị trí (sau heading nào), tên file (chữ thường, gạch ngang), thẻ alt, prompt tạo ảnh. Không tạo ảnh. Alt chỉ mô tả những gì sẽ có trong ảnh, không chèn từ khóa gượng. Ghi vào Projects/<slug>/outputs/YYYY-MM-DD_imageplan_<chủ-đề>.md.
    Trả lời đúng 3 dòng:
    Khách: <slug>
    Kế hoạch ảnh: <đường dẫn>
    Số ảnh: <n>
updated: '2026-11-09'
---

Một bước. Ảnh được tạo bên ngoài (ví dụ Gemini) rồi người chèn vào bài.
