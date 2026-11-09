---
type: workflow
name: SEO Audit kỹ thuật
slug: seo-technical-audit
status: active
description: 'Audit kỹ thuật từ file crawl đã export: tóm tắt, báo lỗi theo mức độ, xếp ưu tiên sửa.'
steps:
- agent: seo-extractor
  task: |-
    Đầu vào: {{input}}
    Đầu vào gồm: slug khách | file crawl (mặc định file mới nhất trong Projects/<slug>/data/crawl/).
    Đọc Projects/SEO-OPS.md và Projects/<slug>/PROJECT.md của đúng khách trong đầu vào. Chỉ làm cho khách đó.
    Đọc file crawl (chỉ đọc). Tóm tắt: số URL theo status_code, URL không index được, title hoặc H1 thiếu hoặc trùng, canonical lệch, word_count rất thấp, chuỗi redirect nếu có cột. Ghi vào Projects/<slug>/data/_summary/YYYY-MM_crawl.md. Không có file crawl thì dừng và báo.
    Trả lời đúng 4 dòng:
    Khách: <slug>
    Tóm tắt: <đường dẫn hoặc không có>
    File crawl: <tên, kỳ>
    Thiếu: <ngắn, hoặc không>
- agent: seo-auditor
  task: |-
    Kết quả bước trước: {{prev}}
    Mở file tóm tắt và các dòng crawl liên quan. Báo lỗi kỹ thuật: mỗi phát hiện gồm URL hoặc nhóm URL, vấn đề, bằng chứng (file, dòng hoặc số đếm), mức P0 đến P3, cách sửa. Không suy đoán ngoài dữ liệu. Ghi vào Projects/<slug>/outputs/YYYY-MM-DD_audit_tech_<chủ-đề>.md.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 3 dòng:
    Khách: <slug>
    Báo cáo: <đường dẫn>
    Số lỗi: P0=<n>, P1=<n>, P2=<n>, P3=<n>
- agent: seo-planner
  task: |-
    Kết quả bước trước: {{prev}}
    Đọc báo cáo audit và xếp ưu tiên sửa theo tác động và công sức; mỗi mục trỏ về phát hiện trong báo cáo. Ghi danh sách ưu tiên vào Projects/<slug>/outputs/YYYY-MM-DD_plan_tech-fix.md.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 3 dòng:
    Khách: <slug>
    Danh sách ưu tiên: <đường dẫn>
    Việc cần người quyết: <ngắn, hoặc không>
updated: '2026-11-09'
---

Ba bước. Cần crawl export (Screaming Frog hoặc tương đương) đặt sẵn trong data/crawl/. Workflow không tự crawl.
