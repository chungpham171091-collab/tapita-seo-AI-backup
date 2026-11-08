---
type: workflow
name: SEO QA và sửa
slug: seo-qa-fix
status: active
description: Audit một bài đã viết, sửa lỗi P0 và P1, rồi kiểm lại. Chạy một vòng; cần vòng hai thì chạy lại với file _v2.
steps:
- agent: seo-auditor
  task: |-
    Audit nội dung theo đầu vào sau: {{input}}

    Đầu vào gồm: slug khách | đường dẫn file bài | từ khóa chính | thị trường.
    Đọc Projects/SEO-OPS.md và Projects/<slug>/PROJECT.md, rồi làm đúng như agent seo-auditor mô tả.
    Ghi báo cáo vào Projects/<slug>/outputs/ và trả lời đúng 3 dòng:
    Bài: <đường dẫn file bài>
    Báo cáo: <đường dẫn file báo cáo>
    Số lỗi: P0=<n>, P1=<n>, P2=<n>, P3=<n>
- agent: seo-writer
  task: |-
    Đây là kết quả bước audit trước: {{prev}}

    Mở file báo cáo và file bài nêu trong kết quả đó. Sửa mọi lỗi P0 và P1. Chỉ sửa chỗ có lỗi, giữ nguyên phần còn lại. Ghi bản sửa thành file mới có hậu tố _v2 cạnh file bài. Không thêm số liệu hoặc nguồn không có.
    Trả lời đúng 3 dòng:
    Bài sửa: <đường dẫn file _v2>
    Báo cáo: <đường dẫn file báo cáo>
    Đã sửa: <số lỗi P0 và P1 đã xử lý>/<tổng số P0 và P1>
- agent: seo-auditor
  task: |-
    Đây là kết quả bước sửa trước: {{prev}}

    Đọc lại toàn bộ file _v2 từ đầu. Kiểm lại từng lỗi P0 và P1 trong báo cáo cũ và quét lỗi mới phát sinh. Ghi kết quả thành mục "Kiểm lại" ở cuối file báo cáo.
    Trả lời đúng 3 dòng:
    Verdict: đạt hoặc không đạt
    Lỗi còn lại: <danh sách ngắn, hoặc không>
    Bản cuối: <đường dẫn file _v2>
updated: '2026-11-08'
---

Workflow dùng chung cho blog, long-form collection và meta. Mỗi bước chỉ truyền 3 dòng kết quả sang bước sau (đường dẫn file), không dán lại cả báo cáo, để token không tăng theo từng bước.
