---
type: workflow
name: SEO Audit on-page
slug: seo-onpage-audit
status: active
description: 'Audit on-page cho danh sách URL: dữ liệu từ extractor, audit theo QRG, reviewer kiểm bằng chứng.'
steps:
- agent: seo-extractor
  task: |-
    Đầu vào: {{input}}
    Đầu vào gồm: slug khách | file hoặc danh sách URL cần audit | từ khóa chính (nếu có).
    Đọc Projects/SEO-OPS.md và Projects/<slug>/PROJECT.md của đúng khách trong đầu vào. Chỉ làm cho khách đó.
    Với các URL đã nêu, lấy dòng tương ứng từ Projects/<slug>/data/crawl/, data/gsc/ (pages, queries), data/rank/. Ghi tóm tắt vào Projects/<slug>/data/_summary/YYYY-MM_onpage_input.md. Nêu rõ URL nào không có dữ liệu.
    Trả lời đúng 4 dòng:
    Khách: <slug>
    Tóm tắt: <đường dẫn>
    Số URL có dữ liệu: <n>/<tổng>
    Thiếu: <file hoặc URL thiếu>
- agent: seo-auditor
  task: |-
    Kết quả bước trước: {{prev}}
    Mở file tóm tắt, rồi mở từng URL bằng web fetch. Audit on-page theo tapita-eeat-check và checklist: title, meta, H1 và cấu trúc heading, intent so với từ khóa, nội dung mỏng hoặc trùng, internal link, canonical. Mỗi phát hiện ghi: URL, vấn đề, bằng chứng, mức P0 đến P3, cách sửa. Ghi vào Projects/<slug>/outputs/YYYY-MM-DD_audit_onpage_<chủ-đề>.md. Không đoán khi thiếu dữ liệu.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 3 dòng:
    Khách: <slug>
    Báo cáo: <đường dẫn>
    Số lỗi: P0=<n>, P1=<n>, P2=<n>, P3=<n>
- agent: seo-reviewer
  task: |-
    Kết quả bước trước: {{prev}}
    Mở báo cáo audit. Kiểm mỗi phát hiện có bằng chứng truy được và mức độ hợp lý; đánh dấu phát hiện thiếu bằng chứng hoặc có vẻ suy đoán. Ghi nhận xét vào Projects/<slug>/outputs/YYYY-MM-DD_review_onpage_<chủ-đề>.md.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 3 dòng:
    Khách: <slug>
    Quyết định: đạt hoặc sửa
    Nhận xét: <đường dẫn>
updated: '2026-11-09'
---

Ba bước. Audit chỉ báo lỗi và cách sửa; người hoặc `seo-writer` thực hiện sửa trong việc riêng.
