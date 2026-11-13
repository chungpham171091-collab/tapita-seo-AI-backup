---
type: workflow
name: SEO Trang cạnh tranh từ khóa và internal link
slug: seo-cannibalization-links
status: 'off'
description: 'Từ keyword mapping và GSC query theo trang: liệt kê trang cạnh tranh cùng từ khóa chính và internal link còn thiếu; planner đề xuất cách sửa.'
steps:
- agent: seo-extractor
  task: |-
    Đầu vào: {{input}}
    Đầu vào gồm: slug khách | chủ đề run (ví dụ YYYY-MM) | số nhóm tối đa cần xem (ví dụ 20).
    Đọc Projects/SEO-OPS.md và Projects/<slug>/PROJECT.md của đúng khách trong đầu vào. Chỉ làm cho khách đó. Thông tin đã có trong PROJECT.md (thị trường, ngôn ngữ, Google domain, tone, từ cấm, skill, đối thủ) thì dùng luôn, không hỏi lại; thiếu thì nói rõ cần điền mục nào vào PROJECT.md.
    Tạo thư mục run bằng lệnh: python tools/seo_ops.py new-run <slug> links <chủ đề run> seo-cannibalization-links (chữ thường, gạch ngang). Không chạy được lệnh thì tạo tay Projects/<slug>/runs/<YYYY-MM-DD>_links_<chủ đề run>/RUN.md theo Projects/_templates/RUN.md. Mọi file của bước này ghi vào thư mục run đó.
    Đọc keyword mapping hiện hành (file keyword_mapping_*.csv mới nhất trong Projects/<slug>/deliverables/) và content cluster cùng ngày nếu có. Không có mapping thì dừng và báo.
    Đọc 4 file tuần query_page_*.csv mới nhất trong Projects/<slug>/data/gsc/ (chỉ đọc) và cộng số liệu 4 tuần.
    a) Với mỗi từ khóa chính và từ khóa phụ trong mapping: tìm query trùng hoặc chứa từ khóa đó mà có từ 2 URL của site trở lên có impressions. Ghi: query, url, clicks, impressions, position (trung bình có trọng số impressions), mapped_url (URL được gán trong mapping).
    b) Từ khóa chính bị gán cho 2 URL trở lên trong mapping.
    Ghi competing_pages.csv vào thư mục run, sắp theo tổng impressions giảm dần, tối đa số nhóm trong đầu vào. Không có file query_page thì chỉ làm phần b và ghi rõ.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 4 dòng:
    Khách: <slug>
    Run: <đường dẫn thư mục run>
    Nhóm cạnh tranh: <n> (từ GSC <n>, từ mapping <n>)
    Thiếu: <ngắn, hoặc không>
- agent: seo-auditor
  task: |-
    Kết quả bước trước: {{prev}}
    Mở competing_pages.csv trong thư mục run. Với từng nhóm, mở các URL trong nhóm bằng web fetch (giãn request nếu site chặn; ghi URL không mở được). Ghi cho từng URL: title, H1, chủ đề chính của trang, và trang đó có link tới mapped_url của nhóm không (anchor là gì).
    Thêm phần internal link: với mỗi mapped_url trong các nhóm, xem các trang cùng sub-topic trong content cluster (chỉ những trang đã mở trong lượt này) có link tới mapped_url không.
    Ghi link_check.csv (cột: group_query, from_url, to_url, has_link, anchor, evidence) và pages_seen.md (title, H1, chủ đề của từng URL đã mở) vào thư mục run. Không đề xuất cách sửa.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 3 dòng:
    Khách: <slug>
    Đã mở: <số URL mở được>/<số URL cần mở>
    Link thiếu: <số cặp chưa có link>
- agent: seo-planner
  task: |-
    Kết quả bước trước: {{prev}}
    Mở competing_pages.csv, link_check.csv và pages_seen.md trong thư mục run. Với từng nhóm, đề xuất một cách sửa có bằng chứng: giữ trang đích và đổi hướng trang kia sang từ khóa riêng của nó; gộp nội dung và chuyển hướng 301; canonical; thêm internal link (from_url, to_url, anchor gợi ý, vị trí trong trang); hoặc sửa keyword mapping. Không đề xuất gộp hay chuyển hướng khi bằng chứng chỉ là một tuần dữ liệu hoặc impressions quá nhỏ; ghi "theo dõi thêm".
    Ghi links_plan.csv (cột: group_query, mapped_url, competing_url, fix_type, detail, from_url, to_url, anchor, priority, evidence) và links_plan.md (tóm tắt) vào thư mục run. Với mỗi file .csv vừa ghi, tạo bản .xlsx bằng: python tools/seo_ops.py xlsx <file.csv>. Không tạo được thì giữ .csv và ghi "chưa có xlsx" trong câu trả lời.
    Cập nhật RUN.md: python tools/seo_ops.py set-run <thư mục run> workflow=<slug workflow này> status=waiting "next_step=Người: chọn cách sửa; đổi mapping thì cập nhật file mapping trong deliverables; sửa nội dung hoặc link thì chạy workflow viết hoặc refresh tương ứng" (không chạy được lệnh thì sửa tay khối đầu RUN.md), thêm tên file vừa tạo vào mục "File trong run này", rồi chạy python tools/seo_ops.py build.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 4 dòng:
    Khách: <slug>
    Run: <đường dẫn thư mục run>
    Đề xuất: <số nhóm cần sửa>, <số link cần thêm>
    Việc cần người quyết: <ngắn, hoặc không>
updated: '2026-11-13'
---

Ba bước. Cần keyword mapping đã duyệt trong `deliverables/` và các file tuần `query_page_*.csv` trong `data/gsc/`. Kiểm link chỉ trong các trang đã mở, không thay cho crawl toàn site.
