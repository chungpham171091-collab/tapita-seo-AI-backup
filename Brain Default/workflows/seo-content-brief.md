---
type: workflow
name: SEO Content brief
slug: seo-content-brief
status: active
description: 'Tùy chọn: tạo brief cho một trang (blog hoặc collection) theo template trong thư mục run mới, rồi reviewer kiểm tra brief đủ mục.'
steps:
- agent: seo-planner
  task: |-
    Đầu vào: {{input}}
    Đầu vào gồm: slug khách | URL đích hoặc chủ đề | từ khóa chính | loại (blog hoặc collection).
    Đọc Projects/SEO-OPS.md và Projects/<slug>/PROJECT.md của đúng khách trong đầu vào. Chỉ làm cho khách đó. Thông tin đã có trong PROJECT.md (thị trường, ngôn ngữ, Google domain, tone, từ cấm, skill, đối thủ) thì dùng luôn, không hỏi lại; thiếu thì nói rõ cần điền mục nào vào PROJECT.md.
    Tạo thư mục run bằng lệnh: python tools/seo_ops.py new-run <slug> <loại> <chủ đề hoặc handle collection> seo-content-brief (chữ thường, gạch ngang). Không chạy được lệnh thì tạo tay Projects/<slug>/runs/<YYYY-MM-DD>_<loại>_<chủ đề hoặc handle collection>/RUN.md theo Projects/_templates/RUN.md. Mọi file của bước này ghi vào thư mục run đó.
    Lập brief theo Projects/_templates/brief.md. Từ khóa phụ lấy từ keyword mapping hiện hành (file keyword_mapping_*.csv mới nhất trong Projects/<slug>/deliverables/), không có thì lấy từ Projects/<slug>/data/keywords/clusters.csv. Làm SERP top 10 cho thị trường của khách. SERP phải là thật: làm bằng web search trên Google domain của khách và ghi danh sách URL đã mở vào file. Web search lỗi thì ghi rõ và gắn cờ "CHƯA CÓ SERP THẬT" ở đầu file; không mô tả SERP từ trí nhớ. Nếu loại là collection, mở trang collection thật và liệt kê URL sub-collection, sản phẩm lấy từ data/inputs/site_urls.csv (không tự bịa URL). Ghi brief.md vào thư mục run.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 4 dòng:
    Khách: <slug>
    Run: <đường dẫn thư mục run>
    Brief: <đường dẫn brief.md>
    Thiếu input: <danh sách, hoặc không>
- agent: seo-reviewer
  task: |-
    Kết quả bước trước: {{prev}}
    Mở brief.md. Kiểm đủ mục theo Projects/_templates/brief.md, claim cấm khớp PROJECT.md, từ khóa và intent khớp SERP đã ghi, có danh sách URL SERP đã mở, không có URL bịa. Ghi nhận xét vào review_brief.md trong thư mục run.
    Cập nhật RUN.md: python tools/seo_ops.py set-run <thư mục run> workflow=<slug workflow này> status=waiting "next_step=Người: duyệt brief.md rồi chạy seo-content-writing với thư mục run này" (không chạy được lệnh thì sửa tay khối đầu RUN.md), thêm tên file vừa tạo vào mục "File trong run này", rồi chạy python tools/seo_ops.py build.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 3 dòng:
    Khách: <slug>
    Quyết định: đạt hoặc sửa
    Nhận xét: <đường dẫn file>
updated: '2026-11-13'
---

Brief là tùy chọn, không bắt buộc trước khi viết. Nếu dùng, người duyệt brief rồi chạy `seo-content-writing` với thư mục run của brief.
