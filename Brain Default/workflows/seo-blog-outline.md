---
type: workflow
name: SEO Blog outline (giai đoạn 1b)
slug: seo-blog-outline
status: 'off'
description: 'Blog: từ title người đã chọn, chạy bước outline của skill blog, dừng chờ duyệt outline.'
steps:
- agent: seo-writer
  task: |-
    Đầu vào: {{input}}
    Đầu vào gồm: slug khách | thư mục run blog | title đã chọn (số thứ tự trong titles.md hoặc nguyên văn) | ghi chú chỉnh của người (hoặc "không").
    Đọc Projects/SEO-OPS.md và Projects/<slug>/PROJECT.md của đúng khách trong đầu vào. Chỉ làm cho khách đó. Thông tin đã có trong PROJECT.md (thị trường, ngôn ngữ, Google domain, tone, từ cấm, skill, đối thủ) thì dùng luôn, không hỏi lại; thiếu thì nói rõ cần điền mục nào vào PROJECT.md.
    Mở titles.md trong thư mục run. Dùng skill ghi ở skill_blog trong PROJECT.md, chạy bước outline của skill với đúng title đã chọn và ghi chú chỉnh, rồi DỪNG. Không viết bài.
    Ghi outline.md vào thư mục run.
    Cập nhật RUN.md: python tools/seo_ops.py set-run <thư mục run> workflow=<slug workflow này> status=waiting "next_step=Người: duyệt hoặc sửa outline.md rồi chạy seo-content-draft" (không chạy được lệnh thì sửa tay khối đầu RUN.md), thêm tên file vừa tạo vào mục "File trong run này", rồi chạy python tools/seo_ops.py build.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 4 dòng:
    Khách: <slug>
    Run: <đường dẫn thư mục run>
    Outline: <đường dẫn outline.md>
    Câu hỏi cần người duyệt: <ngắn, hoặc không>
updated: '2026-11-13'
---

Một bước, kết thúc để người duyệt outline. Bước kế tiếp là `seo-content-draft`.
