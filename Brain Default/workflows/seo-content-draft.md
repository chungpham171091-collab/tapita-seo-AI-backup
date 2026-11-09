---
type: workflow
name: SEO Viết nội dung (giai đoạn 2)
slug: seo-content-draft
status: active
description: Viết bản hoàn chỉnh từ outline đã được người duyệt, rồi ghi draft. Sau đó chạy seo-qa-fix.
steps:
- agent: seo-writer
  task: |-
    Đầu vào: {{input}}
    Đầu vào gồm: slug khách | file outline đã duyệt | ghi chú duyệt của người (hoặc "duyệt nguyên bản").
    Đọc Projects/SEO-OPS.md và Projects/<slug>/PROJECT.md của đúng khách trong đầu vào. Chỉ làm cho khách đó.
    Mở file outline đã duyệt và làm đúng ghi chú duyệt. Chạy tiếp các bước còn lại của skill đến hết bản viết (và optimization nếu skill có). Nếu skill còn điểm dừng duyệt thứ hai, dừng ở đó và nói rõ. Không bịa số liệu, nguồn; thiếu nguồn ghi [CẦN NGUỒN]. Với collection TMF: không giao bài chưa qua Gate 3. Ghi draft vào Projects/<slug>/outputs/YYYY-MM-DD_draft_<chủ-đề>.md.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 4 dòng:
    Khách: <slug>
    Bài: <đường dẫn>
    Từ khóa chính: <từ khóa>
    Việc còn mở: <ngắn, hoặc không>
updated: '2026-11-09'
---

Một bước. Bước kế tiếp luôn là `seo-qa-fix` trên file draft vừa ghi.
