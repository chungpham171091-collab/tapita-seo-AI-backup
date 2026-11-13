---
type: workflow
name: SEO Refresh 1 - tìm trang mất click và đề xuất
slug: seo-content-refresh
status: 'off'
description: 'Tìm trang mất click (4 tuần gần nhất so với 4 tuần trước, từ tóm tắt GSC), mở trang và SERP thật, đề xuất làm mới hay để nguyên. Người quyết định.'
steps:
- agent: seo-planner
  task: |-
    Đầu vào: {{input}}
    Đầu vào gồm: slug khách | số trang tối đa cần xem (ví dụ 10) | ghi chú của người (hoặc "không").
    Đọc Projects/SEO-OPS.md và Projects/<slug>/PROJECT.md của đúng khách trong đầu vào. Chỉ làm cho khách đó. Thông tin đã có trong PROJECT.md (thị trường, ngôn ngữ, Google domain, tone, từ cấm, skill, đối thủ) thì dùng luôn, không hỏi lại; thiếu thì nói rõ cần điền mục nào vào PROJECT.md.
    Đọc latest_gsc.md trong Projects/<slug>/data/_summary/. Không có file, hoặc file tạo cách hôm nay quá 14 ngày, thì dừng và nói chạy seo-data-summary cho gsc trước. Không đọc file GSC thô.
    Tạo thư mục run bằng lệnh: python tools/seo_ops.py new-run <slug> refresh <ngày cuối của cửa sổ 4 tuần trong latest_gsc.md> seo-content-refresh (chữ thường, gạch ngang). Không chạy được lệnh thì tạo tay Projects/<slug>/runs/<YYYY-MM-DD>_refresh_<ngày cuối của cửa sổ 4 tuần trong latest_gsc.md>/RUN.md theo Projects/_templates/RUN.md. Mọi file của bước này ghi vào thư mục run đó.
    Lấy các trang giảm click trong latest_gsc.md (4 tuần gần nhất so với 4 tuần trước), sắp theo số click mất, lấy tối đa số trang trong đầu vào. Với từng trang: từ khóa chính theo keyword mapping hiện hành (file keyword_mapping_*.csv mới nhất trong Projects/<slug>/deliverables/; không có thì dùng query lớn nhất của trang trong latest_gsc.md và ghi rõ), mở trang bằng web fetch, kiểm SERP thật của từ khóa chính. SERP phải là thật: làm bằng web search trên Google domain của khách và ghi danh sách URL đã mở vào file. Web search lỗi thì ghi rõ và gắn cờ "CHƯA CÓ SERP THẬT" ở đầu file; không mô tả SERP từ trí nhớ.
    Đề xuất cho từng trang, mỗi đề xuất có bằng chứng:
    - refresh: nội dung lỗi thời, lệch intent so với SERP hiện tại, mỏng hơn các trang đang xếp trên, mất đoạn trích hoặc vị trí giảm rõ.
    - để nguyên: giảm theo mùa hoặc theo tổng nhu cầu, vị trí ổn nhưng CTR giảm vì SERP thêm tính năng, số click quá nhỏ để kết luận, nghi lỗi đo lường.
    - cần người xem: bằng chứng không đủ.
    Ghi refresh_candidates.csv (cột: url, page_type, main_keyword, clicks_prev_4w, clicks_last_4w, change, position_prev, position_last, recommendation, reason, evidence) và refresh_notes.md (URL trang và SERP đã mở, giả định) vào thư mục run. Với mỗi file .csv vừa ghi, tạo bản .xlsx bằng: python tools/seo_ops.py xlsx <file.csv>. Không tạo được thì giữ .csv và ghi "chưa có xlsx" trong câu trả lời.
    Cập nhật RUN.md: python tools/seo_ops.py set-run <thư mục run> workflow=<slug workflow này> status=waiting "next_step=Người: chọn trang cần làm mới; với mỗi trang chạy seo-content-refresh-update với thư mục run này" (không chạy được lệnh thì sửa tay khối đầu RUN.md), thêm tên file vừa tạo vào mục "File trong run này", rồi chạy python tools/seo_ops.py build.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 4 dòng:
    Khách: <slug>
    Run: <đường dẫn thư mục run>
    Đề xuất: refresh <n>, để nguyên <n>, cần người xem <n>
    Thiếu: <ngắn, hoặc không>
updated: '2026-11-13'
---

Một bước, kết thúc để người chọn trang. Cần `latest_gsc.md` do `seo-data-summary` ghi (đủ 8 file tuần để so 4 tuần với 4 tuần). Bước kế tiếp cho từng trang được chọn là `seo-content-refresh-update`.
