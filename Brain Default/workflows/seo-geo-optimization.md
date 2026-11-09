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
    Đọc Projects/SEO-OPS.md và Projects/<slug>/PROJECT.md của đúng khách trong đầu vào. Chỉ làm cho khách đó.
    Đọc Projects/<slug>/data/geo/prompts.csv và citations_YYYY-MM.csv. Tóm tắt: số prompt theo cluster, tỷ lệ prompt có nhắc brand, URL của khách được trích, URL đối thủ được trích, prompt không có brand nào. Ghi vào Projects/<slug>/data/_summary/YYYY-MM_geo.md. Thiếu file thì dừng và báo.
    Trả lời đúng 4 dòng:
    Khách: <slug>
    Tóm tắt: <đường dẫn hoặc không có>
    Tỷ lệ nhắc brand: <số hoặc không có>
    Thiếu: <ngắn, hoặc không>
- agent: seo-auditor
  task: |-
    Kết quả bước trước: {{prev}}
    Mở tóm tắt GEO. Với các prompt mà brand không được nhắc hoặc đối thủ được trích, mở trang tương ứng của khách bằng web fetch và audit vì sao khó được AI trích dẫn (câu trả lời trực tiếp, entity, FAQ, nguồn, schema). Mỗi phát hiện: URL, vấn đề, bằng chứng, mức, cách sửa. Ghi vào Projects/<slug>/outputs/YYYY-MM-DD_audit_geo_<tháng>.md.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 3 dòng:
    Khách: <slug>
    Báo cáo: <đường dẫn>
    Số trang cần sửa: <n>
- agent: seo-planner
  task: |-
    Kết quả bước trước: {{prev}}
    Xếp ưu tiên các trang cần sửa theo số prompt bị ảnh hưởng và công sức. Chọn tối đa 5 trang đầu cho đợt này. Ghi vào Projects/<slug>/outputs/YYYY-MM-DD_plan_geo.md.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 3 dòng:
    Khách: <slug>
    Kế hoạch: <đường dẫn>
    Số trang chọn: <n>
- agent: seo-writer
  task: |-
    Kết quả bước trước: {{prev}}
    Mở kế hoạch và báo cáo audit. Với từng trang đã chọn, đề xuất bản sửa: câu trả lời trực tiếp ở đầu section, entity cần có, FAQ, gợi ý schema. Chỉ dùng thông tin có thật; thiếu thì ghi [CẦN NGUỒN]. Ghi vào Projects/<slug>/outputs/YYYY-MM-DD_draft_geo-fix.md. Không đăng lên site.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 3 dòng:
    Khách: <slug>
    Đề xuất sửa: <đường dẫn>
    Việc cần người duyệt: <ngắn>
updated: '2026-11-09'
---

Bốn bước. Cần có prompts.csv và citations_YYYY-MM.csv (kiểm ChatGPT, Perplexity, Gemini, AI Overviews do người hoặc tool thực hiện). Sau đó chạy `seo-qa-fix` trên file đề xuất trước khi đăng.
