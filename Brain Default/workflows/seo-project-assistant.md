---
type: workflow
name: SEO Trợ lý dự án
slug: seo-project-assistant
status: active
description: 'Trợ lý của MỘT dự án: trả lời câu hỏi về dự án hoặc một run, sửa file theo góp ý thành bản mới. Không duyệt, không đăng, không chạy cả một công đoạn.'
steps:
- agent: seo-lead
  task: |-
    Đầu vào: {{input}}
    Đầu vào gồm: slug khách | thư mục run (hoặc "không") | tên người hỏi | yêu cầu.
    Đọc Projects/SEO-OPS.md và Projects/<slug>/PROJECT.md của đúng khách trong đầu vào. Chỉ làm cho khách đó. Thông tin đã có trong PROJECT.md (thị trường, ngôn ngữ, Google domain, tone, từ cấm, skill, đối thủ) thì dùng luôn, không hỏi lại; thiếu thì nói rõ cần điền mục nào vào PROJECT.md.
    Đọc 60 dòng cuối của Projects/<slug>/assistant-log.md nếu có, để nắm các trao đổi trước. Nếu có thư mục run: đọc RUN.md, job.json và các file liên quan tới yêu cầu trong thư mục đó.
    Làm đúng yêu cầu, trong các giới hạn của agent seo-lead:
    - Hỏi về tình trạng, lý do, nội dung một file: trả lời dựa trên file, nêu đường dẫn file đã đọc.
    - Góp ý sửa một file trong thư mục run: ghi bản mới cạnh bản cũ (hậu tố _v2, _v3...), không ghi đè; chỉ sửa đúng chỗ được góp ý; không thêm số liệu, nguồn hay khẳng định mới.
    - Yêu cầu là cả một công đoạn (viết bài, audit, lập mapping...): không tự làm; nói rõ nên chạy công đoạn nào ở tab Jobs.
    - Yêu cầu đụng tới PROJECT.md, deliverables, dữ liệu trong data hoặc khách khác: không làm; nêu việc người cần tự làm.
    Trả lời tối đa 15 dòng, bằng ngôn ngữ của người hỏi, gồm: câu trả lời; "File đã ghi:" kèm đường dẫn (hoặc không); "Việc nên làm tiếp:" một dòng.
updated: '2026-11-13'
---

Một bước, do agent seo-lead làm. Dùng từ ô Assistant của trang Projects; trang đó ghi câu hỏi và câu trả lời vào `assistant-log.md` của khách. Trợ lý không thay cho công đoạn của playbook và không thay người duyệt.
