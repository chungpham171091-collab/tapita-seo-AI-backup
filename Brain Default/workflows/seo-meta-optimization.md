---
type: workflow
name: SEO Tối ưu meta và content sản phẩm
slug: seo-meta-optimization
status: active
description: Tối ưu meta title, meta description và content sản phẩm cho một lô URL; auditor đếm ký tự và kiểm compliance.
steps:
- agent: seo-extractor
  task: |-
    Đầu vào: {{input}}
    Đầu vào gồm: slug khách | số URL tối đa cho lô này | file URL (mặc định Projects/<slug>/data/inputs/url_list.csv).
    Đọc Projects/SEO-OPS.md và Projects/<slug>/PROJECT.md của đúng khách trong đầu vào. Chỉ làm cho khách đó.
    Đọc file URL và Projects/<slug>/data/keywords/ahrefs_*.csv (nếu có). Chọn tối đa số URL đã nêu, ưu tiên URL chưa có meta hoặc meta sai độ dài. Ghi lô đã chọn kèm meta hiện tại và từ khóa gợi ý vào Projects/<slug>/data/_summary/YYYY-MM_meta_batch.csv. Nêu file thiếu.
    Trả lời đúng 4 dòng:
    Khách: <slug>
    Lô: <đường dẫn>
    Số URL: <n>
    Thiếu: <danh sách, hoặc không>
- agent: seo-writer
  task: |-
    Kết quả bước trước: {{prev}}
    Mở file lô URL. Chạy skill harry-optimization cho từng URL (chỉ dùng thông tin có thật của sản phẩm, không bịa thông số). Ghi bảng URL, Keywords, Meta Title New, Meta Description New, Content New (nếu là sản phẩm), Note vào Projects/<slug>/outputs/YYYY-MM-DD_meta_<tên-lô>.md. Meta title 40 đến 60 ký tự, description 140 đến 160 ký tự.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 3 dòng:
    Khách: <slug>
    Bảng: <đường dẫn>
    Việc cần người: <ví dụ chỉnh từ khóa, hoặc không>
- agent: seo-auditor
  task: |-
    Kết quả bước trước: {{prev}}
    Mở bảng meta. Đếm ký tự thật của từng meta title và description. Kiểm claim cấm theo PROJECT.md và skill compliance của khách, kiểm thông số không có nguồn. Ghi báo cáo vào Projects/<slug>/outputs/YYYY-MM-DD_review_meta_<tên-lô>.md, nêu từng dòng lỗi.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 4 dòng:
    Khách: <slug>
    Verdict: đạt hoặc không đạt
    Số dòng lỗi: <n>/<tổng>
    Báo cáo: <đường dẫn>
updated: '2026-11-09'
---

Ba bước. Giữa bước 1 và 2, người có thể chỉnh từ khóa chính và phụ của từng URL dựa trên Ahrefs; nếu cần, chạy riêng từng bước. Dòng lỗi thì chạy lại `seo-meta-optimization` với lô nhỏ hơn hoặc nhờ `seo-writer` sửa riêng các dòng đó.
