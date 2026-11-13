---
type: workflow
name: SEO Planning 4-5 - keyword mapping và content cluster
slug: seo-keyword-mapping
status: 'off'
description: 'Planning bước 4 và 5: ghép nhóm từ khóa với URL collection và product (mỗi URL một từ khóa chính), rồi chia topic và sub-topic.'
steps:
- agent: seo-extractor
  task: |-
    Đầu vào: {{input}}
    Đầu vào gồm: slug khách | thư mục run planning | file nhóm từ khóa trong run (mặc định groups_<country>.csv).
    Đọc Projects/SEO-OPS.md và Projects/<slug>/PROJECT.md của đúng khách trong đầu vào. Chỉ làm cho khách đó. Thông tin đã có trong PROJECT.md (thị trường, ngôn ngữ, Google domain, tone, từ cấm, skill, đối thủ) thì dùng luôn, không hỏi lại; thiếu thì nói rõ cần điền mục nào vào PROJECT.md.
    Đọc file nhóm (kết quả công cụ nhóm của team) và keywords_<country>.csv trong thư mục run. Nhận diện cột nhóm, keyword chính, keyword phụ, search volume, tổng search volume nhóm theo header; không nhận diện được thì dừng và nêu header đang có.
    Ghi groups_joined.csv vào thư mục run, mỗi nhóm một dòng: group_id, main_keyword, sub_keywords (cách nhau bằng dấu chấm phẩy), main_sv, total_sv, level, intent (level và intent lấy theo keyword chính từ keywords_<country>.csv; không có thì để trống).
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 4 dòng:
    Khách: <slug>
    Run: <đường dẫn thư mục run>
    Nhóm: <số nhóm>
    Thiếu: <ngắn, hoặc không>
- agent: seo-planner
  task: |-
    Kết quả bước trước: {{prev}}
    Mở groups_joined.csv và pages.csv trong thư mục run, và danh sách URL collection và product trong Projects/<slug>/data/inputs/site_urls.csv.
    Keyword mapping: gán keyword chính của từng nhóm cho URL phù hợp nhất, rồi ghép keyword phụ, search volume và level của nhóm. Quy tắc:
    - Mỗi URL chỉ một keyword chính, và keyword chính của các URL phải khác nhau.
    - Một nhóm hợp với hai URL, hoặc hai nhóm cùng nhắm một URL: chọn phương án hợp nhất và ghi rõ ở cột note bằng chữ "TRÙNG" kèm URL còn lại.
    - Nhóm không có URL phù hợp: không gán; để sang content cluster với "new page".
    - Chỉ dùng URL có trong site_urls.csv.
    Nếu Projects/<slug>/deliverables/ đã có keyword_mapping_*.csv, ghi ở cột note các URL đổi keyword chính so với bản đó.
    Ghi keyword_mapping_<country>.csv vào thư mục run, cột: url, page_type, main_keyword, sub_keywords, search_volume, level, intent, note.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 4 dòng:
    Khách: <slug>
    Run: <đường dẫn thư mục run>
    Mapping: <số URL đã gán>, trùng <n>, nhóm chưa có trang <n>
    Câu hỏi cho người: <ngắn, hoặc không>
- agent: seo-planner
  task: |-
    Kết quả bước trước: {{prev}}
    Mở groups_joined.csv và keyword_mapping_<country>.csv trong thư mục run. Chia các nhóm theo topic và sub-topic phù hợp.
    Ghi content_cluster_<country>.csv vào thư mục run, mỗi nhóm một dòng, cột: topic, sub_topic, group_main_keyword, total_volume, level, mapped_url (ghi "new page" nếu nhóm chưa có trang), page_type (collection, product, blog hoặc page; với "new page" là loại trang đề xuất).
    Với mỗi file .csv vừa ghi, tạo bản .xlsx bằng: python tools/seo_ops.py xlsx <file.csv>. Không tạo được thì giữ .csv và ghi "chưa có xlsx" trong câu trả lời. Áp dụng cho keyword_mapping_<country>.csv và content_cluster_<country>.csv.
    Cập nhật RUN.md: python tools/seo_ops.py set-run <thư mục run> workflow=<slug workflow này> status=waiting "next_step=Người: xem keyword mapping và content cluster, sửa trực tiếp nếu cần, rồi chạy seo-priority-plan" (không chạy được lệnh thì sửa tay khối đầu RUN.md), thêm tên file vừa tạo vào mục "File trong run này", rồi chạy python tools/seo_ops.py build.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 4 dòng:
    Khách: <slug>
    Run: <đường dẫn thư mục run>
    Cluster: <số topic> topic, <số sub-topic> sub-topic, <số new page> new page
    Việc của người: xem 2 file rồi chạy seo-priority-plan
updated: '2026-11-13'
---

Ba bước, chạy sau khi người đã nhóm từ khóa bằng công cụ của team và lưu groups_<country>.csv vào thư mục run. Kết thúc để người xem mapping và cluster.
