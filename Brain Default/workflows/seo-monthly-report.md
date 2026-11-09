---
type: workflow
name: SEO Báo cáo tháng
slug: seo-monthly-report
status: active
description: 'Báo cáo tháng theo template: tóm tắt số liệu từ GSC, GA4, rank, citations, viết báo cáo, reviewer kiểm số liệu, ghi một dòng portfolio_kpi.'
steps:
- agent: seo-extractor
  task: |-
    Đầu vào: {{input}}
    Đầu vào gồm: slug khách | tháng YYYY-MM.
    Đọc Projects/SEO-OPS.md và Projects/<slug>/PROJECT.md của đúng khách trong đầu vào. Chỉ làm cho khách đó.
    Đọc file của tháng và tháng trước trong Projects/<slug>/data/: gsc, ga4, rank, geo/citations. Ghi tóm tắt từng nguồn (KPI tháng, so với tháng trước và cùng kỳ nếu có dữ liệu, top tăng và giảm) vào Projects/<slug>/data/_summary/YYYY-MM_<nguồn>.md. Nêu nguồn nào thiếu.
    Trả lời đúng 4 dòng:
    Khách: <slug>
    Tóm tắt: <các đường dẫn>
    Nguồn thiếu: <danh sách, hoặc không>
    Tháng: <YYYY-MM>
- agent: seo-planner
  task: |-
    Kết quả bước trước: {{prev}}
    Mở các file tóm tắt. Viết báo cáo theo Projects/_templates/report.md: tóm tắt 3 dòng, KPI so với tháng trước và cùng kỳ, top tăng và giảm, tình hình GEO, việc đã làm (từ outputs/ của tháng), kế hoạch tháng tới. Mọi số phải lấy từ file tóm tắt; nguồn thiếu thì ghi [CẦN SỐ LIỆU]. Ghi vào Projects/<slug>/outputs/YYYY-MM-DD_report_<YYYY-MM>.md.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 3 dòng:
    Khách: <slug>
    Báo cáo: <đường dẫn>
    Tháng: <YYYY-MM>
- agent: seo-reviewer
  task: |-
    Kết quả bước trước: {{prev}}
    Mở báo cáo và các file tóm tắt. Đối chiếu từng con số trong báo cáo với file tóm tắt; số không truy được là lỗi. Kiểm theo Projects/_templates/review.md. Ghi nhận xét vào Projects/<slug>/outputs/YYYY-MM-DD_review_report_<YYYY-MM>.md.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 5 dòng:
    Khách: <slug>
    Tháng: <YYYY-MM>
    Quyết định: đạt hoặc sửa
    Số lỗi số liệu: <n>
    Nhận xét: <đường dẫn>
- agent: seo-extractor
  task: |-
    Kết quả bước trước: {{prev}}
    Chỉ làm nếu quyết định là "đạt". Nếu "sửa" thì không làm gì và trả lời "Bỏ qua: báo cáo chưa đạt".
    Nếu đạt: thêm đúng MỘT dòng cho khách và tháng này vào Projects/_registry/portfolio_kpi.csv (cột month, slug, clicks, impressions, avg_position, sessions, conversions, revenue, keywords_top10, geo_mention_rate, pages_published, issues_open). Chỉ dùng số có trong file tóm tắt; ô không có số thì để trống. Không sửa dòng của khách khác. Nếu đã có dòng của khách và tháng này thì không thêm.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 2 dòng:
    Khách: <slug>
    Kết quả: <đã thêm, đã có sẵn, hoặc bỏ qua>
updated: '2026-11-09'
---

Bốn bước. `portfolio_kpi.csv` là file duy nhất dùng chung giữa các khách và chỉ chứa số tổng hợp.
