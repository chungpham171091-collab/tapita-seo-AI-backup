---
type: workflow
name: SEO Viết nội dung (giai đoạn 1)
slug: seo-content-writing
status: active
description: 'Blog: nghiên cứu SERP và đề xuất 3 đến 5 title, dừng chờ chọn title. Collection: chạy skill đến strategy report và outline, dừng chờ duyệt outline.'
steps:
- agent: seo-writer
  task: |-
    Đầu vào: {{input}}
    Đầu vào gồm: slug khách | loại (blog hoặc collection) | từ khóa chính | từ khóa phụ (cách nhau bằng dấu phẩy, hoặc "không") | URL collection hoặc chủ đề blog | thư mục run có sẵn (ví dụ đã có brief) hoặc "mới" | ghi chú (intent, file top sellers, hoặc "không").
    Đọc Projects/SEO-OPS.md và Projects/<slug>/PROJECT.md của đúng khách trong đầu vào. Chỉ làm cho khách đó. Thông tin đã có trong PROJECT.md (thị trường, ngôn ngữ, Google domain, tone, từ cấm, skill, đối thủ) thì dùng luôn, không hỏi lại; thiếu thì nói rõ cần điền mục nào vào PROJECT.md.
    Nếu là "mới": Tạo thư mục run bằng lệnh: python tools/seo_ops.py new-run <slug> <loại> <chủ đề hoặc handle collection> seo-content-writing (chữ thường, gạch ngang). Không chạy được lệnh thì tạo tay Projects/<slug>/runs/<YYYY-MM-DD>_<loại>_<chủ đề hoặc handle collection>/RUN.md theo Projects/_templates/RUN.md. Mọi file của bước này ghi vào thư mục run đó. Nếu đã có thư mục run: ghi tiếp vào đó; có brief.md thì bám theo brief (brief là tùy chọn).
    Kiểm từ khóa chính với keyword mapping hiện hành (file keyword_mapping_*.csv mới nhất trong Projects/<slug>/deliverables/, nếu có): nếu là từ khóa chính của URL khác thì ghi cảnh báo TRÙNG ở đầu file kết quả, vẫn làm tiếp.
    Blog: dùng skill ghi ở skill_blog trong PROJECT.md. Đầu vào bước 1 của skill lấy từ PROJECT.md (thị trường, ngôn ngữ, Google domain, tone) và từ dòng đầu vào (từ khóa chính, từ khóa phụ, intent trong ghi chú; không có intent thì xác định từ SERP thật và ghi rõ). Chạy hết bước 1 của skill (SERP, PAA, competitor gap, bảng 3 đến 5 title kèm meta và slug) rồi DỪNG. Ghi titles.md.
    Collection: dùng skill ghi ở skill_collection trong PROJECT.md. Đầu vào của skill: URL collection, từ khóa chính và phụ, brand (tên khách trong PROJECT.md), danh sách URL nội bộ và blog từ Projects/<slug>/data/inputs/site_urls.csv, danh sách sản phẩm và top sellers từ file nêu trong ghi chú (không có thì skill tự lấy từ trang collection và ghi rõ là lấy từ trang). Chạy skill đến hết strategy report và outline (kể cả các gate trước khi viết nếu skill có) rồi DỪNG. Ghi outline.md.
    SERP phải là thật: làm bằng web search trên Google domain của khách và ghi danh sách URL đã mở vào file. Web search lỗi thì ghi rõ và gắn cờ "CHƯA CÓ SERP THẬT" ở đầu file; không mô tả SERP từ trí nhớ.
    Không viết bài hoàn chỉnh ở workflow này.
    Cập nhật RUN.md: python tools/seo_ops.py set-run <thư mục run> workflow=<slug workflow này> status=waiting "next_step=Blog: người chọn title trong titles.md rồi chạy seo-blog-outline. Collection: người duyệt outline.md rồi chạy seo-content-draft" (không chạy được lệnh thì sửa tay khối đầu RUN.md), thêm tên file vừa tạo vào mục "File trong run này", rồi chạy python tools/seo_ops.py build.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 5 dòng:
    Khách: <slug>
    Run: <đường dẫn thư mục run>
    File: <titles.md hoặc outline.md>
    Đang dừng ở: <bước nào của skill>
    Câu hỏi cần người duyệt: <ngắn>
updated: '2026-11-13'
---

Một bước, kết thúc ở điểm duyệt đầu tiên của skill. Blog: người chọn title rồi chạy `seo-blog-outline`. Collection: người duyệt outline rồi chạy `seo-content-draft`. Brief (`seo-content-brief`) là tùy chọn; nếu đã chạy thì đưa thư mục run của brief vào đầu vào.
