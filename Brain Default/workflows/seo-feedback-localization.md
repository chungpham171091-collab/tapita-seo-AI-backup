---
type: workflow
name: SEO Sửa theo feedback và bản địa hóa
slug: seo-feedback-localization
status: active
description: Sửa bài theo feedback của khách hoặc bản địa hóa sang thị trường đích, rồi kiểm lại.
steps:
- agent: seo-writer
  task: |-
    Đầu vào: {{input}}
    Đầu vào gồm: slug khách | file bài | file feedback hoặc "feedback: <nội dung>" | thị trường đích.
    Đọc Projects/SEO-OPS.md và Projects/<slug>/PROJECT.md của đúng khách trong đầu vào. Chỉ làm cho khách đó.
    Sửa hoặc dịch bài theo feedback. Chỉ sửa chỗ có feedback hoặc cần bản địa hóa, giữ nguyên phần còn lại. Nguồn ưu tiên: thị trường đích, rồi châu Âu, UK, US; link phải mở được; không bịa data. Ghi bản mới thành file cạnh bài gốc với hậu tố _fb hoặc mã thị trường (ví dụ _de-DE). Không ghi đè bản gốc.
    Trả lời đúng 3 dòng:
    Khách: <slug>
    Bài mới: <đường dẫn>
    Feedback chưa xử lý được: <ngắn, hoặc không>
- agent: seo-auditor
  task: |-
    Kết quả bước trước: {{prev}}
    Đọc lại toàn bộ bài mới từ đầu. Kiểm đúng ngôn ngữ thị trường đích, skill compliance của khách (chế độ Audit), harry-reference-check cho link và số liệu, và mọi feedback đã được xử lý. Ghi báo cáo vào Projects/<slug>/outputs/YYYY-MM-DD_review_<chủ-đề>.md.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 3 dòng:
    Khách: <slug>
    Verdict: đạt hoặc không đạt
    Báo cáo: <đường dẫn>
updated: '2026-11-09'
---

Hai bước. Bài tiếng Việt: người sửa wording sau cùng vì giọng AI còn nặng.
