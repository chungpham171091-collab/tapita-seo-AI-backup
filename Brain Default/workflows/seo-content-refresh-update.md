---
type: workflow
name: SEO Refresh 2 - làm mới một trang
slug: seo-content-refresh-update
status: 'off'
description: 'Làm mới nội dung một trang người đã chọn, theo skill của loại trang, giữ phần đang tốt. Sau đó chạy seo-qa-fix.'
steps:
- agent: seo-writer
  task: |-
    Đầu vào: {{input}}
    Đầu vào gồm: slug khách | thư mục run refresh | URL trang | từ khóa chính | hướng làm mới của người.
    Đọc Projects/SEO-OPS.md và Projects/<slug>/PROJECT.md của đúng khách trong đầu vào. Chỉ làm cho khách đó. Thông tin đã có trong PROJECT.md (thị trường, ngôn ngữ, Google domain, tone, từ cấm, skill, đối thủ) thì dùng luôn, không hỏi lại; thiếu thì nói rõ cần điền mục nào vào PROJECT.md.
    Mở refresh_candidates.csv và refresh_notes.md trong thư mục run. Loại trang theo Projects/<slug>/data/inputs/site_urls.csv. Lấy nội dung hiện tại: content_current trong data/inputs/url_list.csv, hoặc Shopify export với product, hoặc mở trang bằng web fetch (ghi rõ nguồn). Ghi nguyên văn vào current_<handle>.md trong thư mục run.
    Dùng skill của loại trang ghi trong PROJECT.md (skill_blog, skill_collection hoặc skill_product), làm theo hướng làm mới của người: giữ phần đang đúng và đang tốt, cập nhật phần lỗi thời, bổ sung phần còn thiếu so với SERP đã ghi trong refresh_notes.md. Meta theo quy tắc của skill. Không bịa số liệu, nguồn; thiếu ghi [CẦN NGUỒN].
    Ghi refresh_<handle>.md vào thư mục run: đầu file là bảng thay đổi (phần nào, đổi gì, vì sao), sau đó là bản mới đầy đủ.
    Cập nhật RUN.md: python tools/seo_ops.py set-run <thư mục run> workflow=<slug workflow này> status=qa "next_step=Chạy seo-qa-fix trên refresh_<handle>.md" (không chạy được lệnh thì sửa tay khối đầu RUN.md), thêm tên file vừa tạo vào mục "File trong run này", rồi chạy python tools/seo_ops.py build.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 4 dòng:
    Khách: <slug>
    Run: <đường dẫn thư mục run>
    Bản mới: <đường dẫn refresh_<handle>.md>
    Việc còn mở: <ngắn, hoặc không>
updated: '2026-11-13'
---

Một bước. Bước kế tiếp là `seo-qa-fix` trên file refresh, rồi người duyệt và đăng như mọi bài khác.
