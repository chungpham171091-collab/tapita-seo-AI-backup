---
type: workflow
name: SEO Viết nội dung (giai đoạn 1)
slug: seo-content-writing
status: active
description: Chạy skill viết của khách đến điểm dừng duyệt đầu tiên (strategy và outline), ghi file và dừng chờ người duyệt.
steps:
- agent: seo-writer
  task: |-
    Đầu vào: {{input}}
    Đầu vào gồm: slug khách | loại (blog hoặc collection) | từ khóa chính | URL collection hoặc chủ đề | file brief (nếu có, hoặc "không").
    Đọc Projects/SEO-OPS.md và Projects/<slug>/PROJECT.md của đúng khách trong đầu vào. Chỉ làm cho khách đó.
    Chọn skill theo bảng mục 3 của SEO-OPS.md và cột content_skill hoặc PROJECT.md. Collection của TMF dùng shopify-collection-seo-tmf. Chạy skill đến ĐIỂM DỪNG DUYỆT ĐẦU TIÊN của nó (collection: hết strategy report và outline; blog: hết bước 1 nghiên cứu title). KHÔNG viết bài hoàn chỉnh ở bước này. Với collection TMF: thực hiện Gate 1 bằng cách mở trang collection và trang sản phẩm thật, lập Product Fact Sheet. Danh sách URL lấy từ Projects/<slug>/data/inputs/site_urls.csv; thiếu thì lấy từ sitemap công khai của site và lưu lại file đó. Ghi kết quả vào Projects/<slug>/outputs/YYYY-MM-DD_outline_<chủ-đề>.md.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 4 dòng:
    Khách: <slug>
    File: <đường dẫn>
    Đang dừng ở: <bước nào của skill>
    Câu hỏi cần người duyệt: <ngắn>
updated: '2026-11-09'
---

Một bước. Workflow dừng ở điểm duyệt đầu tiên vì skill yêu cầu người duyệt. Người đọc file outline, sửa nếu cần, rồi chạy `seo-content-draft` với ghi chú duyệt.
