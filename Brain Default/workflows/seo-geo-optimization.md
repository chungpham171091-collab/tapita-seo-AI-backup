---
type: workflow
name: SEO Tối ưu GEO
slug: seo-geo-optimization
status: active
description: 'Dựa vào prompts và citations đã theo dõi: tóm tắt, audit trang, xếp ưu tiên, đề xuất bản sửa answer-first.'
steps:
- agent: seo-extractor
  task: |-
    Đầu vào: {{input}}
    Đầu vào gồm: slug khách | tháng YYYY-MM.
    Đọc Projects/SEO-OPS.md và Projects/<slug>/PROJECT.md của đúng khách trong đầu vào. Chỉ làm cho khách đó. Thông tin đã có trong PROJECT.md (thị trường, ngôn ngữ, Google domain, tone, từ cấm, skill, đối thủ) thì dùng luôn, không hỏi lại; thiếu thì nói rõ cần điền mục nào vào PROJECT.md.
    Tạo thư mục run bằng lệnh: python tools/seo_ops.py new-run <slug> geo <YYYY-MM> seo-geo-optimization (chữ thường, gạch ngang). Không chạy được lệnh thì tạo tay Projects/<slug>/runs/<YYYY-MM-DD>_geo_<YYYY-MM>/RUN.md theo Projects/_templates/RUN.md. Mọi file của bước này ghi vào thư mục run đó.
    Đọc Projects/<slug>/data/geo/prompts.csv và file citations của tháng trong data/geo/. Tóm tắt: số prompt theo cluster, tỷ lệ prompt có nhắc brand, URL của khách được trích, URL đối thủ được trích, prompt không có brand nào. Ghi vào Projects/<slug>/data/_summary/<YYYY-MM>_geo.md và ghi đè latest_geo.md trong cùng thư mục. Thiếu file thì dừng và báo.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 5 dòng:
    Khách: <slug>
    Run: <đường dẫn thư mục run>
    Tóm tắt: <đường dẫn hoặc không có>
    Tỷ lệ nhắc brand: <số hoặc không có>
    Thiếu: <ngắn, hoặc không>
- agent: seo-auditor
  task: |-
    Kết quả bước trước: {{prev}}
    Mở latest_geo.md. Với các prompt mà brand không được nhắc hoặc đối thủ được trích, mở trang tương ứng của khách bằng web fetch và audit vì sao khó được AI trích dẫn (câu trả lời trực tiếp, entity, FAQ, nguồn, schema). Mỗi phát hiện: URL, vấn đề, bằng chứng, mức, cách sửa. Ghi audit_geo.md vào thư mục run.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 3 dòng:
    Khách: <slug>
    Báo cáo: <đường dẫn>
    Số trang cần sửa: <n>
- agent: seo-planner
  task: |-
    Kết quả bước trước: {{prev}}
    Xếp ưu tiên các trang cần sửa theo số prompt bị ảnh hưởng và công sức. Chọn tối đa 5 trang đầu cho đợt này. Ghi plan_geo.md vào thư mục run.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 3 dòng:
    Khách: <slug>
    Kế hoạch: <đường dẫn>
    Số trang chọn: <n>
- agent: seo-writer
  task: |-
    Kết quả bước trước: {{prev}}
    Mở kế hoạch và báo cáo audit. Với từng trang đã chọn, đề xuất bản sửa: câu trả lời trực tiếp ở đầu section, entity cần có, FAQ, gợi ý schema. Chỉ dùng thông tin có thật; thiếu thì ghi [CẦN NGUỒN]. Ghi draft_geo-fix.md vào thư mục run. Không đăng lên site.
    Cập nhật RUN.md: python tools/seo_ops.py set-run <thư mục run> workflow=<slug workflow này> status=waiting "next_step=Người: duyệt đề xuất, rồi chạy seo-qa-fix trên draft_geo-fix.md" (không chạy được lệnh thì sửa tay khối đầu RUN.md), thêm tên file vừa tạo vào mục "File trong run này", rồi chạy python tools/seo_ops.py build.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 3 dòng:
    Khách: <slug>
    Đề xuất sửa: <đường dẫn>
    Việc cần người duyệt: <ngắn>
updated: '2026-11-13'
---

Bốn bước. Cần có prompts.csv và file citations của tháng (kiểm ChatGPT, Perplexity, Gemini, AI Overviews do người hoặc tool thực hiện). Sau đó chạy `seo-qa-fix` trên file đề xuất trước khi đăng.
