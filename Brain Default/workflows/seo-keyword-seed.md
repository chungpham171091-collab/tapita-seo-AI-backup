---
type: workflow
name: SEO Planning 1 - seed từ khóa
slug: seo-keyword-seed
status: 'off'
description: 'Planning bước 1: lấy dữ liệu trang (H1, meta, mô tả) rồi gợi ý 3 đến 5 seed keyword cho mỗi trang collection và product. Kết thúc để người chạy Ahrefs.'
steps:
- agent: seo-extractor
  task: |-
    Đầu vào: {{input}}
    Đầu vào gồm: slug khách | phạm vi (collection, product hoặc cả hai) | chủ đề run (ví dụ toan-site hoặc tên nhóm sản phẩm) | số trang tối đa (số, hoặc "tất cả").
    Đọc Projects/SEO-OPS.md và Projects/<slug>/PROJECT.md của đúng khách trong đầu vào. Chỉ làm cho khách đó. Thông tin đã có trong PROJECT.md (thị trường, ngôn ngữ, Google domain, tone, từ cấm, skill, đối thủ) thì dùng luôn, không hỏi lại; thiếu thì nói rõ cần điền mục nào vào PROJECT.md.
    Tạo thư mục run bằng lệnh: python tools/seo_ops.py new-run <slug> planning <chủ đề run> seo-keyword-seed (chữ thường, gạch ngang). Không chạy được lệnh thì tạo tay Projects/<slug>/runs/<YYYY-MM-DD>_planning_<chủ đề run>/RUN.md theo Projects/_templates/RUN.md. Mọi file của bước này ghi vào thư mục run đó.
    Lấy danh sách URL theo phạm vi từ Projects/<slug>/data/inputs/site_urls.csv (giữ thứ tự trong file, cắt theo số trang tối đa). Lấy dữ liệu từng trang, chỉ từ file có sẵn: file Shopify export mới nhất trong Projects/<slug>/data/inputs/ (tên shopify_products_YYYY-MM-DD.csv) cho product, và Projects/<slug>/data/inputs/url_list.csv cho mọi URL. Không web fetch ở bước này.
    Ghi pages.csv vào thư mục run, cột: url, page_type, h1, meta_title, meta_description, description (300 ký tự đầu của mô tả, đã bỏ HTML). Trường nào không có trong file thì để trống, không tự điền.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 5 dòng:
    Khách: <slug>
    Run: <đường dẫn thư mục run>
    Trang: <số trang có dữ liệu>/<tổng số trang đã chọn>
    Đã đọc: <các file>
    Thiếu: <file hoặc trường thiếu, hoặc không>
- agent: seo-planner
  task: |-
    Kết quả bước trước: {{prev}}
    Mở pages.csv trong thư mục run nêu ở trên. Với mỗi trang có ít nhất H1 hoặc meta title, gợi ý 3 đến 5 seed keyword dựa trên dữ liệu của trang đó:
    - Viết bằng ngôn ngữ thị trường trong PROJECT.md.
    - Từ khóa sản phẩm phải nêu đặc điểm, đặc tính sát nhất của sản phẩm và dài từ 3 từ trở lên.
    - Từ khóa collection mô tả nhóm sản phẩm của trang.
    - Chỉ dùng thông tin có trong pages.csv; không đoán thông số.
    Trang không có dữ liệu thì bỏ qua và liệt kê ở cuối seed_notes.md.
    Ghi seed_keywords.csv (mỗi từ khóa một dòng; cột: url, page_type, keyword, words, source_field) và seed_for_ahrefs.txt (mỗi dòng một từ khóa, không trùng) vào thư mục run. Với mỗi file .csv vừa ghi, tạo bản .xlsx bằng: python tools/seo_ops.py xlsx <file.csv>. Không tạo được thì giữ .csv và ghi "chưa có xlsx" trong câu trả lời.
    Cập nhật RUN.md: python tools/seo_ops.py set-run <thư mục run> workflow=<slug workflow này> status=waiting "next_step=Người: đưa seed_for_ahrefs.txt vào Ahrefs Keywords Explorer đúng country, tab Matching terms, export và lưu vào Projects/<slug>/data/keywords/ahrefs_<country>_YYYY-MM.csv, rồi chạy seo-keyword-level" (không chạy được lệnh thì sửa tay khối đầu RUN.md), thêm tên file vừa tạo vào mục "File trong run này", rồi chạy python tools/seo_ops.py build.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 4 dòng:
    Khách: <slug>
    Run: <đường dẫn thư mục run>
    Seed: <số từ khóa> từ khóa cho <số trang> trang
    Việc của người: chạy Ahrefs theo next_step trong RUN.md
updated: '2026-11-13'
---

Planning bước 1 trong sheet Working Steps. Hai bước, rồi kết thúc. Người chạy Ahrefs Keywords Explorer (Planning bước 2), lưu export vào data/keywords/, rồi chạy `seo-keyword-level`. Cần có `data/inputs/site_urls.csv` và ít nhất một trong hai file dữ liệu trang (Shopify export hoặc url_list.csv).
