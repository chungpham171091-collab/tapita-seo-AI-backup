---
type: workflow
name: Audit website SEO + GEO
slug: audit-website-seo-geo
status: active
description: Audit toàn diện website về SEO, hiệu năng, đo lường, GEO/AEO và AI agent, ra báo cáo việc ưu tiên có bằng chứng.
steps:
- agent: agency-marketing-seo-specialist
  task: 'Audit SEO nền tảng cho website sau: {{input}}


    Kiểm: crawl và index, robots, sitemap, canonical, cấu trúc URL, title và meta, heading, liên kết nội bộ, khoảng trống nội dung so với từ khóa mục tiêu, tín hiệu backlink. Mỗi phát hiện ghi URL làm bằng chứng, mức độ (cao/trung/thấp) và cách sửa. Chưa kiểm được mục nào thì ghi "chưa xác minh" kèm lý do. Đầu ra: mục "## 1. SEO nền tảng" theo dạng bảng phát hiện, cuối mục có điểm 0-10.'
- agent: agency-testing-performance-benchmarker
  task: 'Audit hiệu năng cho website trong đầu vào gốc. Đây là báo cáo các bước trước:


    {{prev}}


    Giữ nguyên toàn bộ báo cáo trên, rồi thêm mục "## 2. Hiệu năng": Core Web Vitals (LCP, INP, CLS), tốc độ tải, render JavaScript, trang nặng nhất. Nêu số đo thật và công cụ đã dùng; không đo được thì nói rõ, không ước đoán. Mỗi phát hiện có mức độ và cách sửa. Cuối mục có điểm 0-10.'
- agent: agency-paid-media-tracking-specialist
  task: 'Audit đo lường cho website trong đầu vào gốc. Đây là báo cáo các bước trước:


    {{prev}}


    Giữ nguyên toàn bộ báo cáo trên, rồi thêm mục "## 3. Đo lường": GA4, Search Console, thẻ và sự kiện chuyển đổi, khả năng tách traffic đến từ AI (chatgpt.com, perplexity.ai, gemini...). Nếu thiếu quyền truy cập thì nêu rõ cần gì và chỉ đánh giá phần quan sát được từ phía trang. Cuối mục có điểm 0-10.'
- agent: agency-marketing-aeo-foundations
  task: 'Audit nền tảng GEO/AEO phía website trong đầu vào gốc. Đây là báo cáo các bước trước:


    {{prev}}


    Giữ nguyên toàn bộ báo cáo trên, rồi thêm mục "## 4. GEO phía website": schema markup, entity và thông tin thương hiệu nhất quán, llms.txt, robots.txt có chặn bot AI không (GPTBot, ClaudeBot, PerplexityBot, Google-Extended), nội dung có cấu trúc dễ trích dẫn. Mỗi phát hiện kèm URL hoặc đoạn mã làm bằng chứng, mức độ và cách sửa. Cuối mục có điểm 0-10.'
- agent: agency-marketing-ai-citation-strategist
  task: 'Đo độ hiện diện thực tế của website trong câu trả lời AI. Đây là báo cáo các bước trước:


    {{prev}}


    Giữ nguyên toàn bộ báo cáo trên, rồi thêm mục "## 5. GEO thực tế". Chạy một bộ truy vấn đại diện (khoảng 10-15, gồm truy vấn thương hiệu, truy vấn danh mục, truy vấn so sánh) trên càng nhiều nền tảng càng tốt (ChatGPT, Claude, Gemini, Perplexity). Với mỗi truy vấn ghi: nền tảng, câu hỏi, thương hiệu có được nhắc không, đối thủ nào được nhắc và vì sao. Không chạy được nền tảng nào thì nói rõ. Nhắc rằng đây là ảnh chụp tại một thời điểm. Cuối mục có điểm 0-10 và các sửa nội dung để được trích dẫn.'
- agent: agency-marketing-agentic-search-optimizer
  task: 'Audit khả năng AI agent hoàn thành việc trên website trong đầu vào gốc. Đây là báo cáo các bước trước:


    {{prev}}


    Giữ nguyên toàn bộ báo cáo trên, rồi thêm mục "## 6. Sẵn sàng cho AI agent": chọn 3-5 việc quan trọng (đặt lịch, mua, đăng ký, liên hệ), kiểm xem agent có làm được không, form và nút có máy đọc được không, có cần WebMCP không. Nêu chỗ kẹt cụ thể và cách sửa. Cuối mục có điểm 0-10.'
- agent: agency-agents-orchestrator
  task: 'Tổng hợp báo cáo audit cuối cùng. Đây là toàn bộ báo cáo 6 mảng:


    {{prev}}


    Việc cần làm: (1) bắt mâu thuẫn giữa các mảng và nêu rõ; (2) loại hoặc đánh dấu "chưa xác minh" mọi phát hiện không có bằng chứng; (3) gộp thành danh sách việc ưu tiên, xếp theo tác động / công sức, mỗi việc có người phụ trách đề xuất và mức độ; (4) viết tóm tắt điều hành 5-7 dòng. Đầu ra theo thứ tự: Tóm tắt điều hành, bảng điểm 6 mảng, Top việc ưu tiên, Mâu thuẫn hoặc chưa xác minh, rồi đính kèm nguyên 6 mục chi tiết. Viết tiếng Việt, không dùng em dash.'
updated: '2026-11-04'
---

Audit toàn diện website: SEO nền tảng, hiệu năng, đo lường, GEO phía website, GEO đo thực tế, sẵn sàng cho AI agent. Bước cuối tổng hợp, kiểm chứng bằng chứng và xếp việc ưu tiên. Đầu vào: URL website và mục tiêu (ngành, từ khóa, đối thủ nếu có).
