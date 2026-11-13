---
type: workflow
name: SEO Sửa theo feedback và bản địa hóa
slug: seo-feedback-localization
status: active
description: 'Sửa bài theo feedback của khách hoặc bản địa hóa sang thị trường đích trong thư mục run của bài, rồi kiểm lại.'
steps:
- agent: seo-writer
  task: |-
    Đầu vào: {{input}}
    Đầu vào gồm: slug khách | thư mục run của bài | file bài | file feedback hoặc "feedback: <nội dung>" | thị trường đích.
    Đọc Projects/SEO-OPS.md và Projects/<slug>/PROJECT.md của đúng khách trong đầu vào. Chỉ làm cho khách đó. Thông tin đã có trong PROJECT.md (thị trường, ngôn ngữ, Google domain, tone, từ cấm, skill, đối thủ) thì dùng luôn, không hỏi lại; thiếu thì nói rõ cần điền mục nào vào PROJECT.md.
    Sửa hoặc dịch bài theo feedback. Chỉ sửa chỗ có feedback hoặc cần bản địa hóa, giữ nguyên phần còn lại. Nguồn ưu tiên: thị trường đích, rồi châu Âu, UK, US; link phải mở được; không bịa data. Ghi bản mới vào thư mục run với hậu tố _fb hoặc mã thị trường (ví dụ _de-DE). Không ghi đè bản gốc.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 3 dòng:
    Khách: <slug>
    Bài mới: <đường dẫn>
    Feedback chưa xử lý được: <ngắn, hoặc không>
- agent: seo-auditor
  task: |-
    Kết quả bước trước: {{prev}}
    Đọc lại toàn bộ bài mới từ đầu. Kiểm đúng ngôn ngữ thị trường đích, harry-reference-check cho link và số liệu (chạy trước), skill compliance của khách (chế độ Audit), và mọi feedback đã được xử lý. Ghi review_fb.md vào thư mục run.
    Cập nhật RUN.md: python tools/seo_ops.py set-run <thư mục run> workflow=<slug workflow này> status=waiting "next_step=Người: duyệt bản mới; duyệt thì chép vào Projects/<slug>/deliverables/ và đặt status=approved" (không chạy được lệnh thì sửa tay khối đầu RUN.md), thêm tên file vừa tạo vào mục "File trong run này", rồi chạy python tools/seo_ops.py build.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 3 dòng:
    Khách: <slug>
    Verdict: đạt hoặc không đạt
    Báo cáo: <đường dẫn>
updated: '2026-11-13'
---

Hai bước. Bài tiếng Việt: người sửa wording sau cùng vì giọng AI còn nặng.
