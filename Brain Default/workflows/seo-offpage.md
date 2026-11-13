---
type: workflow
name: SEO Off-page - hồ sơ backlink, link gap, outreach nháp
slug: seo-offpage
status: 'off'
description: 'Từ export backlink Ahrefs: tóm tắt hồ sơ, link gap so với đối thủ trong PROJECT.md, đề xuất mục tiêu và góc digital PR, viết nháp outreach. Người gửi.'
steps:
- agent: seo-extractor
  task: |-
    Đầu vào: {{input}}
    Đầu vào gồm: slug khách | chủ đề run (ví dụ YYYY-MM) | file backlink (hoặc "mới nhất") | file link gap (hoặc "mới nhất", hoặc "không").
    Đọc Projects/SEO-OPS.md và Projects/<slug>/PROJECT.md của đúng khách trong đầu vào. Chỉ làm cho khách đó. Thông tin đã có trong PROJECT.md (thị trường, ngôn ngữ, Google domain, tone, từ cấm, skill, đối thủ) thì dùng luôn, không hỏi lại; thiếu thì nói rõ cần điền mục nào vào PROJECT.md.
    Tạo thư mục run bằng lệnh: python tools/seo_ops.py new-run <slug> offpage <chủ đề run> seo-offpage (chữ thường, gạch ngang). Không chạy được lệnh thì tạo tay Projects/<slug>/runs/<YYYY-MM-DD>_offpage_<chủ đề run>/RUN.md theo Projects/_templates/RUN.md. Mọi file của bước này ghi vào thư mục run đó.
    Đọc trong Projects/<slug>/data/backlinks/ (chỉ đọc): file backlink của khách (ahrefs_backlinks_*.csv) và file link gap (link_intersect_*.csv). Tóm tắt hồ sơ: số backlink, số referring domain, phân bố DR theo nhóm (0-9, 10-29, 30-49, 50-69, 70+), tỷ lệ dofollow, phân bố anchor (anchor chứa tên khách trong PROJECT.md, anchor là URL, anchor khác; ghi 20 anchor nhiều nhất), 20 trang được link nhiều nhất, 20 referring domain DR cao nhất, link mới và mất nếu export có cột.
    Link gap: domain có link tới ít nhất một đối thủ trong mục Đối thủ chính của PROJECT.md nhưng chưa link tới khách. Ghi domain, DR, các đối thủ được link, traffic nếu có cột. Đối thủ trong file khác danh sách PROJECT.md thì ghi rõ.
    Ghi offpage_profile.md và link_gap.csv vào thư mục run. Không khuyến nghị.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 5 dòng:
    Khách: <slug>
    Run: <đường dẫn thư mục run>
    Hồ sơ: <số referring domain>, DR trung vị <n>
    Link gap: <số domain>
    Thiếu: <ngắn, hoặc không>
- agent: seo-planner
  task: |-
    Kết quả bước trước: {{prev}}
    Mở offpage_profile.md và link_gap.csv trong thư mục run. Mở bằng web fetch tối đa 20 domain gap đứng đầu (theo DR và số đối thủ được link) để xác định loại: nhà sản xuất hoặc trang đại lý, hiệp hội ngành, diễn đàn hoặc cộng đồng, báo hoặc blog ngành, trang tài nguyên, thư mục. Ghi URL đã mở; không mở được thì ghi rõ, không đoán loại.
    Đề xuất danh sách mục tiêu (target_domain, loại, lý do liên quan, trang của khách nên được link, cách tiếp cận, ưu tiên) và 3 đến 5 góc digital PR dựa trên tài sản có thật của khách trong PROJECT.md (ví dụ video, diễn đàn, đào tạo). Góc PR cần số liệu mà khách chưa có thì ghi [CẦN SỐ LIỆU]; không bịa nghiên cứu hay số liệu. Không ghi email hay tên người liên hệ không có trong trang đã mở.
    Ghi offpage_plan.csv và offpage_plan.md vào thư mục run. Với mỗi file .csv vừa ghi, tạo bản .xlsx bằng: python tools/seo_ops.py xlsx <file.csv>. Không tạo được thì giữ .csv và ghi "chưa có xlsx" trong câu trả lời.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 4 dòng:
    Khách: <slug>
    Kế hoạch: <đường dẫn offpage_plan.md>
    Mục tiêu: <số domain>, góc PR: <n>
    Đã mở: <số domain mở được>/<số cần mở>
- agent: seo-writer
  task: |-
    Kết quả bước trước: {{prev}}
    Mở offpage_plan.md và offpage_plan.csv. Viết nháp outreach bằng ngôn ngữ thị trường trong PROJECT.md: một mẫu cho mỗi loại mục tiêu (subject và body), và câu mở đầu riêng cho tối đa 10 mục tiêu ưu tiên cao, chỉ dùng thông tin có trong trang đã mở. Chỗ cần người điền ghi [TÊN NGƯỜI NHẬN], [EMAIL]. Không hứa trả tiền, không hứa đặt link đổi, không nêu số liệu không có nguồn.
    Ghi outreach_drafts.md vào thư mục run. Đầu file ghi: "Nháp. Người duyệt, tìm liên hệ và tự gửi. Không gửi tự động."
    Cập nhật RUN.md: python tools/seo_ops.py set-run <thư mục run> workflow=<slug workflow này> status=waiting "next_step=Người: duyệt mục tiêu và nháp, tìm liên hệ, tự gửi; ghi đã gửi cho ai, ngày nào vào RUN.md" (không chạy được lệnh thì sửa tay khối đầu RUN.md), thêm tên file vừa tạo vào mục "File trong run này", rồi chạy python tools/seo_ops.py build.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 3 dòng:
    Khách: <slug>
    Nháp: <đường dẫn outreach_drafts.md>
    Số mẫu: <n> mẫu, <n> câu mở đầu riêng
updated: '2026-11-13'
---

Ba bước. Cần export backlink của khách và export Link Intersect (khách so với các đối thủ trong PROJECT.md) từ Ahrefs trong `data/backlinks/`. Workflow không gửi email và không tự liên hệ ai.
