---
type: workflow
name: SEO Planning 2 - lọc và xếp level từ khóa
slug: seo-keyword-level
status: 'off'
description: 'Planning bước 2: từ export Ahrefs, bỏ từ khóa branded và local, xếp level theo lowest DR so với DR của site, ghi file cho công cụ nhóm từ khóa.'
steps:
- agent: seo-extractor
  task: |-
    Đầu vào: {{input}}
    Đầu vào gồm: slug khách | thư mục run planning | file export Ahrefs (hoặc "mới nhất" để lấy file ahrefs_<country>_*.csv mới nhất trong Projects/<slug>/data/keywords/).
    Đọc Projects/SEO-OPS.md và Projects/<slug>/PROJECT.md của đúng khách trong đầu vào. Chỉ làm cho khách đó. Thông tin đã có trong PROJECT.md (thị trường, ngôn ngữ, Google domain, tone, từ cấm, skill, đối thủ) thì dùng luôn, không hỏi lại; thiếu thì nói rõ cần điền mục nào vào PROJECT.md.
    Mã country là phần sau dấu gạch của market trong PROJECT.md, viết thường (en-US thành us). DR của site lấy ở dòng own_dr của PROJECT.md.
    Đọc file export (chỉ đọc). Tìm các cột từ khóa, search volume, lowest DR và intent. Export có các cột intent dạng đúng/sai (Informational, Navigational, Commercial, Transactional, Branded, Local) thì ghép tên các cột đúng thành một chuỗi. Không tìm được cột nào thì dừng và nêu tên cột còn thiếu.
    Lọc: bỏ dòng có intent Local. Bỏ dòng có intent Branded, trừ khi PROJECT.md ghi branded_keywords: keep. Ghi các dòng đã bỏ vào removed_<country>.csv (keyword, search_volume, reason).
    Level theo lowest DR so với own_dr: easy khi lowest DR không quá own_dr + 10; medium khi cao hơn own_dr + 10 đến own_dr + 25; difficult khi cao hơn own_dr + 25. own_dr trống hoặc ô lowest DR trống thì để level trống và ghi [CẦN SỐ LIỆU].
    Ghi vào thư mục run:
    - keywords_<country>.csv, mỗi từ khóa một dòng, cột: keyword, search_volume, lowest_dr, level, intent. Sắp theo level (easy, medium, difficult, trống) rồi search volume giảm dần.
    - for_grouping_<country>.csv, cột: keyword, search_volume. Quá 2.500 dòng thì tách thành for_grouping_<country>_part1.csv, _part2.csv..., mỗi file tối đa 2.500 dòng (giới hạn một tài khoản của công cụ nhóm).
    Với mỗi file .csv vừa ghi, tạo bản .xlsx bằng: python tools/seo_ops.py xlsx <file.csv>. Không tạo được thì giữ .csv và ghi "chưa có xlsx" trong câu trả lời.
    Cập nhật RUN.md: python tools/seo_ops.py set-run <thư mục run> workflow=<slug workflow này> status=waiting "next_step=Người: đưa for_grouping_<country>.csv vào công cụ nhóm từ khóa của team, export kết quả (nhóm, keyword chính, keyword phụ, search volume, tổng search volume nhóm) và lưu thành groups_<country>.csv trong thư mục run, rồi chạy seo-keyword-mapping" (không chạy được lệnh thì sửa tay khối đầu RUN.md), thêm tên file vừa tạo vào mục "File trong run này", rồi chạy python tools/seo_ops.py build.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 5 dòng:
    Khách: <slug>
    Run: <đường dẫn thư mục run>
    Giữ: <số từ khóa> (easy <n>, medium <n>, difficult <n>, chưa có level <n>)
    Đã bỏ: <số dòng> (local <n>, branded <n>)
    Thiếu: <own_dr, cột hoặc file thiếu, hoặc không>
updated: '2026-11-13'
---

Một bước, chạy sau khi người đã export Ahrefs. Kết thúc để người chạy công cụ nhóm từ khóa của team (Planning bước 3). Lưu ý: sheet để trống khoảng chênh 25 đến 30 điểm DR; workflow tạm xếp phần này vào difficult.
