---
type: workflow
name: SEO Viết nội dung (giai đoạn 2)
slug: seo-content-draft
status: active
description: 'Viết bản hoàn chỉnh từ outline đã được người duyệt (blog hoặc collection), ghi draft.md trong thư mục run. Sau đó chạy seo-qa-fix.'
steps:
- agent: seo-writer
  task: |-
    Đầu vào: {{input}}
    Đầu vào gồm: slug khách | thư mục run | ghi chú duyệt outline của người (hoặc "duyệt nguyên bản").
    Đọc Projects/SEO-OPS.md và Projects/<slug>/PROJECT.md của đúng khách trong đầu vào. Chỉ làm cho khách đó. Thông tin đã có trong PROJECT.md (thị trường, ngôn ngữ, Google domain, tone, từ cấm, skill, đối thủ) thì dùng luôn, không hỏi lại; thiếu thì nói rõ cần điền mục nào vào PROJECT.md.
    Mở RUN.md và outline.md trong thư mục run (loại trang là dòng task trong RUN.md) và làm đúng ghi chú duyệt. Dùng skill của loại trang ghi trong PROJECT.md (blog: skill_blog; collection: skill_collection) và chạy tiếp các bước còn lại của skill đến hết bản viết, kể cả bước tối ưu và bước tự kiểm mà skill yêu cầu. Nếu skill còn điểm dừng duyệt khác, dừng ở đó và nói rõ.
    Không bịa số liệu, nguồn; thiếu nguồn ghi [CẦN NGUỒN]. Link nội bộ chỉ lấy từ Projects/<slug>/data/inputs/site_urls.csv.
    Ghi draft.md vào thư mục run, gồm bài và gói meta theo skill.
    Cập nhật RUN.md: python tools/seo_ops.py set-run <thư mục run> workflow=<slug workflow này> status=qa "next_step=Chạy seo-qa-fix trên draft.md" (không chạy được lệnh thì sửa tay khối đầu RUN.md), thêm tên file vừa tạo vào mục "File trong run này", rồi chạy python tools/seo_ops.py build.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 4 dòng:
    Khách: <slug>
    Run: <đường dẫn thư mục run>
    Bài: <đường dẫn draft.md>
    Việc còn mở: <ngắn, hoặc không>
updated: '2026-11-13'
---

Một bước. Bước kế tiếp luôn là `seo-qa-fix` trên draft.md.
