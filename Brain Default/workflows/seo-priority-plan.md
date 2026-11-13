---
type: workflow
name: SEO Planning 6 - bản nháp kế hoạch ưu tiên
slug: seo-priority-plan
status: 'off'
description: 'Planning bước 6: AI lập bản nháp thứ tự ưu tiên và timeline theo nhóm sản phẩm từ mapping và cluster. Người quyết định.'
steps:
- agent: seo-planner
  task: |-
    Đầu vào: {{input}}
    Đầu vào gồm: slug khách | thư mục run planning | số tháng của kế hoạch | ghi chú của người (hoặc "không").
    Đọc Projects/SEO-OPS.md và Projects/<slug>/PROJECT.md của đúng khách trong đầu vào. Chỉ làm cho khách đó. Thông tin đã có trong PROJECT.md (thị trường, ngôn ngữ, Google domain, tone, từ cấm, skill, đối thủ) thì dùng luôn, không hỏi lại; thiếu thì nói rõ cần điền mục nào vào PROJECT.md.
    Mở keyword_mapping_<country>.csv và content_cluster_<country>.csv trong thư mục run (người có thể đã sửa). Đọc mục Mục tiêu và KPI, Nhóm sản phẩm ưu tiên trong PROJECT.md, và latest_gsc.md trong Projects/<slug>/data/_summary/ nếu có.
    Xếp ưu tiên theo nhóm sản phẩm: khả năng cạnh tranh (level, easy trước rồi medium) và tiềm năng (tổng search volume). Kiểm sơ bộ SERP thật cho tối đa 10 nhóm đứng đầu. SERP phải là thật: làm bằng web search trên Google domain của khách và ghi danh sách URL đã mở vào file. Web search lỗi thì ghi rõ và gắn cờ "CHƯA CÓ SERP THẬT" ở đầu file; không mô tả SERP từ trí nhớ.
    Với mỗi nhóm: thứ tự ưu tiên, lý do, các URL, loại việc (collection long-form, product quick optimization, blog, trang mới), số đầu việc ước tính, tháng đề xuất. Nếu khó đạt mục tiêu traffic chỉ bằng collection và product, đề xuất thêm từ khóa blog level easy của các nhóm khác.
    Ghi priority_plan.csv (cột: priority, product_group, reason, urls, task_type, items, proposed_month, main_keywords) và priority_plan.md (tóm tắt, giả định, URL SERP đã mở, câu hỏi cho người) vào thư mục run. Với mỗi file .csv vừa ghi, tạo bản .xlsx bằng: python tools/seo_ops.py xlsx <file.csv>. Không tạo được thì giữ .csv và ghi "chưa có xlsx" trong câu trả lời.
    Đây là bản nháp; không ghi như kế hoạch đã chốt.
    Cập nhật RUN.md: python tools/seo_ops.py set-run <thư mục run> workflow=<slug workflow này> status=waiting "next_step=Người: quyết định ưu tiên và timeline. Duyệt thì chép keyword_mapping, content_cluster, priority_plan (csv và xlsx) vào Projects/<slug>/deliverables/ và đặt status=approved" (không chạy được lệnh thì sửa tay khối đầu RUN.md), thêm tên file vừa tạo vào mục "File trong run này", rồi chạy python tools/seo_ops.py build.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 4 dòng:
    Khách: <slug>
    Run: <đường dẫn thư mục run>
    Kế hoạch nháp: <số nhóm> nhóm, <số đầu việc> đầu việc trong <số tháng> tháng
    Câu hỏi cho người: <ngắn, hoặc không>
updated: '2026-11-13'
---

Một bước, kết thúc để người quyết định. Bản keyword mapping đã duyệt trong `deliverables/` là mapping hiện hành mà các tác vụ khác đọc.
