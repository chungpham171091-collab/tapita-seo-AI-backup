---
type: workflow
name: SEO Trợ lý cấu hình
slug: seo-config-assistant
status: active
description: 'Soạn bản nháp thay đổi một file cấu hình SEO-Ops (job type, workflow, data source, team) theo yêu cầu bằng lời. Người xem và bấm Apply ở trang Projects.'
group: SEO-Ops
steps:
- agent: seo-config
  task: |-
    Đầu vào: {{input}}
    Đầu vào gồm: config | file đích | file gốc để bắt đầu | thư mục đề xuất | tên người hỏi | yêu cầu.
    Đọc Projects/HOW-IT-WORKS.md. Đọc file gốc để bắt đầu (nếu file đích chưa có, file gốc là bản dùng chung để nhân bản). Đọc thêm file nó trỏ tới nếu cần (workflow mà job type gọi, agent mà workflow gọi).
    Viết vào thư mục đề xuất:
    - proposed với đúng đuôi của file đích (ví dụ proposed.json, proposed.md, proposed.csv): TOÀN BỘ nội dung mới của file đích, đã áp dụng yêu cầu, giữ nguyên mọi phần còn lại.
    - summary.md: đổi gì (từng ý), vì sao, ảnh hưởng tới job nào hoặc dự án nào, điều người cần kiểm sau khi áp dụng.
    Không sửa file đích hay file nào ngoài thư mục đề xuất. Yêu cầu chưa rõ: chỉ viết summary.md với câu hỏi, không viết proposed.
    Trả lời tối đa 8 dòng, bằng ngôn ngữ của người hỏi: tóm tắt thay đổi; "Đề xuất:" kèm đường dẫn; hoặc câu hỏi cần người trả lời.
updated: '2026-11-20'
---

Một bước, do agent seo-config làm. Gọi từ nút "Change with AI" ở trang Projects (trình sửa job type và workflow). Không có gì được áp dụng cho tới khi người bấm Apply; trang Projects lưu bản cũ để quay lại.
