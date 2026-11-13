---
type: workflow
name: SEO Product 1 - phân tích sản phẩm và bộ từ khóa
slug: seo-product-keywords
status: 'off'
description: 'Quick optimization phần đầu: lấy dữ liệu sản phẩm từ Shopify export, phân tích và tạo bộ từ khóa theo skill sản phẩm. Kết thúc để người lấy search volume trên Ahrefs.'
steps:
- agent: seo-extractor
  task: |-
    Đầu vào: {{input}}
    Đầu vào gồm: slug khách | file Shopify export (hoặc "mới nhất" để lấy file shopify_products_*.csv mới nhất trong Projects/<slug>/data/inputs/) | danh sách URL hoặc handle sản phẩm, cách nhau bằng dấu phẩy | chủ đề run (ví dụ tên nhóm sản phẩm).
    Đọc Projects/SEO-OPS.md và Projects/<slug>/PROJECT.md của đúng khách trong đầu vào. Chỉ làm cho khách đó. Thông tin đã có trong PROJECT.md (thị trường, ngôn ngữ, Google domain, tone, từ cấm, skill, đối thủ) thì dùng luôn, không hỏi lại; thiếu thì nói rõ cần điền mục nào vào PROJECT.md.
    Tạo thư mục run bằng lệnh: python tools/seo_ops.py new-run <slug> product <chủ đề run> seo-product-keywords (chữ thường, gạch ngang). Không chạy được lệnh thì tạo tay Projects/<slug>/runs/<YYYY-MM-DD>_product_<chủ đề run>/RUN.md theo Projects/_templates/RUN.md. Mọi file của bước này ghi vào thư mục run đó.
    Đọc file Shopify export (chỉ đọc). Shopify ghi nhiều dòng cho một sản phẩm (biến thể, ảnh): gộp theo Handle. Với từng sản phẩm trong danh sách, ghi một dòng vào products.csv trong thư mục run, cột: url (canonical_url trong PROJECT.md + products/ + handle), handle, title, meta_title, meta_description, content (body đã bỏ HTML), product_type, vendor, tags, options_variants, collection. Trường không có trong export (ví dụ collection) thì để trống, không tự điền. Sản phẩm không tìm thấy thì liệt kê.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 4 dòng:
    Khách: <slug>
    Run: <đường dẫn thư mục run>
    Sản phẩm: <số có dữ liệu>/<số yêu cầu>
    Thiếu: <sản phẩm hoặc trường thiếu, hoặc không>
- agent: seo-writer
  task: |-
    Kết quả bước trước: {{prev}}
    Mở products.csv trong thư mục run. Dùng skill ghi ở skill_product trong PROJECT.md, chỉ chạy phần phân tích sản phẩm và tạo bộ từ khóa của skill (chưa viết meta, chưa viết content). Chỉ dùng thông tin có trong products.csv. Ngôn ngữ từ khóa theo thị trường trong PROJECT.md. Không dừng ở điểm xác nhận của skill; người xem bảng phân tích cùng lúc với lấy search volume.
    Ghi vào thư mục run: product_analysis.md (bảng thuộc tính từng sản phẩm), product_keywords.csv (cột: url, keyword, words) và keywords_for_ahrefs.txt (mỗi dòng một từ khóa, không trùng).
    Cập nhật RUN.md: python tools/seo_ops.py set-run <thư mục run> workflow=<slug workflow này> status=waiting "next_step=Người: xem product_analysis.md; đưa keywords_for_ahrefs.txt vào Ahrefs Keywords Explorer đúng country, export search volume và lưu thành ahrefs_volume.csv trong thư mục run, rồi chạy seo-meta-optimization" (không chạy được lệnh thì sửa tay khối đầu RUN.md), thêm tên file vừa tạo vào mục "File trong run này", rồi chạy python tools/seo_ops.py build.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 4 dòng:
    Khách: <slug>
    Run: <đường dẫn thư mục run>
    Từ khóa: <tổng số> cho <số sản phẩm> sản phẩm
    Việc của người: xem phân tích, lấy search volume trên Ahrefs
updated: '2026-11-13'
---

Hai bước, kết thúc ở bước Ahrefs giữa quy trình. Đầu vào là Shopify product export đặt trong `data/inputs/`. Bước kế tiếp là `seo-meta-optimization`.
