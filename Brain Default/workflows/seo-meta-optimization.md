---
type: workflow
name: SEO Product 2 - chọn từ khóa chính, meta và content sản phẩm
slug: seo-meta-optimization
status: active
description: 'Quick optimization phần sau: ghép search volume từ Ahrefs, chọn từ khóa chính theo luật volume, viết meta và content sản phẩm theo skill. Sau đó chạy seo-qa-fix.'
steps:
- agent: seo-extractor
  task: |-
    Đầu vào: {{input}}
    Đầu vào gồm: slug khách | thư mục run product | file Ahrefs trong run (mặc định ahrefs_volume.csv) | ghi chú chỉnh từ khóa của người (hoặc "không").
    Đọc Projects/SEO-OPS.md và Projects/<slug>/PROJECT.md của đúng khách trong đầu vào. Chỉ làm cho khách đó. Thông tin đã có trong PROJECT.md (thị trường, ngôn ngữ, Google domain, tone, từ cấm, skill, đối thủ) thì dùng luôn, không hỏi lại; thiếu thì nói rõ cần điền mục nào vào PROJECT.md.
    Đọc file Ahrefs (chỉ đọc) và product_keywords.csv trong thư mục run. Ghép search volume theo từ khóa (không phân biệt hoa thường). Ghi product_keywords_sv.csv vào thư mục run, cột: url, keyword, words, search_volume; từ khóa không có trong export thì ghi "không có". Chép nguyên văn ghi chú chỉnh từ khóa của người vào keyword_notes.md trong thư mục run (ghi "không" nếu không có).
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 4 dòng:
    Khách: <slug>
    Run: <đường dẫn thư mục run>
    Đã ghép: <số từ khóa có volume>/<tổng>
    Thiếu: <ngắn, hoặc không>
- agent: seo-writer
  task: |-
    Kết quả bước trước: {{prev}}
    Mở products.csv, product_analysis.md và product_keywords_sv.csv trong thư mục run, và keyword_notes.md (ghi chú chỉnh từ khóa của người; làm theo ghi chú này trước các quy tắc dưới đây nếu hai bên khác nhau).
    Chọn từ khóa cho từng sản phẩm:
    - Từ khóa chính dài 3 đến 4 từ, mô tả sát sản phẩm nhất và có search volume thực (lớn hơn 0). Ngoại lệ: khi từ khóa chính là tên sản phẩm thì được dùng dù không có volume; ghi rõ ở cột Note.
    - Từ khóa chính không trùng từ khóa chính của collection hay sản phẩm khác trong keyword mapping hiện hành (file keyword_mapping_*.csv mới nhất trong Projects/<slug>/deliverables/, nếu có).
    - Từ khóa volume 0 hoặc không có trong export: bỏ. Chỉ giữ làm từ khóa phụ khi là long-tail mô tả sát sản phẩm, và ghi "SV 0" cạnh từ khóa đó.
    - Từ khóa chính đặt dòng đầu, rồi sắp các từ khóa còn lại theo ưu tiên.
    Sau đó dùng skill ghi ở skill_product trong PROJECT.md, chạy phần meta, content và tự kiểm của skill (độ dài meta, cấu trúc content, bảng đầu ra theo đúng skill). Không bịa thông số; thiếu thì ghi theo cách skill quy định.
    Ghi meta_table.csv vào thư mục run với các cột của bảng đầu ra trong skill. Với mỗi file .csv vừa ghi, tạo bản .xlsx bằng: python tools/seo_ops.py xlsx <file.csv>. Không tạo được thì giữ .csv và ghi "chưa có xlsx" trong câu trả lời.
    Cập nhật RUN.md: python tools/seo_ops.py set-run <thư mục run> workflow=<slug workflow này> status=qa "next_step=Chạy seo-qa-fix trên meta_table.csv" (không chạy được lệnh thì sửa tay khối đầu RUN.md), thêm tên file vừa tạo vào mục "File trong run này", rồi chạy python tools/seo_ops.py build.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 4 dòng:
    Khách: <slug>
    Run: <đường dẫn thư mục run>
    Bảng: <đường dẫn meta_table.csv>
    Từ khóa chính không có volume: <số sản phẩm dùng tên sản phẩm, hoặc không>
updated: '2026-11-13'
---

Hai bước, chạy sau khi người đã lấy search volume trên Ahrefs. Bước kế tiếp là `seo-qa-fix` trên meta_table.csv. Luật từ khóa volume 0 nằm ở workflow này vì skill sản phẩm chưa có.
