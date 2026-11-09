---
type: workflow
name: SEO Content brief
slug: seo-content-brief
status: active
description: Tạo brief cho một trang (blog hoặc collection) theo template, rồi reviewer kiểm tra brief đủ mục.
steps:
- agent: seo-planner
  task: |-
    Đầu vào: {{input}}
    Đầu vào gồm: slug khách | URL đích hoặc tên cluster | từ khóa chính | loại (blog hoặc collection).
    Đọc Projects/SEO-OPS.md và Projects/<slug>/PROJECT.md của đúng khách trong đầu vào. Chỉ làm cho khách đó.
    Lập brief theo Projects/_templates/brief.md. Lấy từ khóa phụ từ Projects/<slug>/data/keywords/clusters.csv. Làm SERP top 10 bằng web search cho thị trường của khách; ghi URL đã mở. Nếu loại là collection, mở trang collection thật và liệt kê URL sub-collection, sản phẩm lấy từ data/inputs/site_urls.csv (không tự bịa URL). Ghi brief vào Projects/<slug>/outputs/YYYY-MM-DD_brief_<chủ-đề>.md.
    Trả lời đúng 3 dòng:
    Khách: <slug>
    Brief: <đường dẫn>
    Thiếu input: <danh sách, hoặc không>
- agent: seo-reviewer
  task: |-
    Kết quả bước trước: {{prev}}
    Mở file brief. Kiểm tra đủ mục theo Projects/_templates/brief.md, claim cấm khớp PROJECT.md, từ khóa và intent khớp SERP đã ghi, không có URL bịa. Ghi nhận xét vào Projects/<slug>/outputs/YYYY-MM-DD_review_brief_<chủ-đề>.md.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 3 dòng:
    Khách: <slug>
    Quyết định: đạt hoặc sửa
    Nhận xét: <đường dẫn file>
updated: '2026-11-09'
---

Người đọc brief và duyệt trước khi chạy `seo-content-writing`. Brief không đạt thì chạy lại với ghi chú sửa.
