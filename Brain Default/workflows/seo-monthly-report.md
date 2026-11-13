---
type: workflow
name: SEO Báo cáo tháng
slug: seo-monthly-report
status: active
description: 'Báo cáo tháng theo template: extractor tóm tắt GSC, GA4, rank, citations của tháng; planner viết; reviewer kiểm số liệu; ghi một dòng portfolio_kpi.'
steps:
- agent: seo-extractor
  task: |-
    Đầu vào: {{input}}
    Đầu vào gồm: slug khách | tháng YYYY-MM.
    Đọc Projects/SEO-OPS.md và Projects/<slug>/PROJECT.md của đúng khách trong đầu vào. Chỉ làm cho khách đó. Thông tin đã có trong PROJECT.md (thị trường, ngôn ngữ, Google domain, tone, từ cấm, skill, đối thủ) thì dùng luôn, không hỏi lại; thiếu thì nói rõ cần điền mục nào vào PROJECT.md.
    Tạo thư mục run bằng lệnh: python tools/seo_ops.py new-run <slug> report <YYYY-MM> seo-monthly-report (chữ thường, gạch ngang). Không chạy được lệnh thì tạo tay Projects/<slug>/runs/<YYYY-MM-DD>_report_<YYYY-MM>/RUN.md theo Projects/_templates/RUN.md. Mọi file của bước này ghi vào thư mục run đó.
    Đọc trong Projects/<slug>/data/: các file tuần gsc và rank có ngày thuộc tháng này và tháng trước, file ga4 của tháng này và tháng trước, file citations của tháng trong geo/ (chỉ đọc). Tính KPI theo tháng, so với tháng trước và cùng kỳ năm trước nếu có dữ liệu; top trang và query tăng, giảm. Ghi vào Projects/<slug>/data/_summary/<YYYY-MM>_report-data.md. Nêu nguồn nào thiếu và tuần nào thiếu.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 5 dòng:
    Khách: <slug>
    Run: <đường dẫn thư mục run>
    Tóm tắt: <đường dẫn>
    Nguồn thiếu: <danh sách, hoặc không>
    Tháng: <YYYY-MM>
- agent: seo-planner
  task: |-
    Kết quả bước trước: {{prev}}
    Mở file tóm tắt. Viết báo cáo theo Projects/_templates/report.md: tóm tắt 3 dòng, KPI so với tháng trước và cùng kỳ, top tăng và giảm, tình hình GEO, việc đã làm (lấy từ các RUN.md trong Projects/<slug>/runs/ có updated thuộc tháng), kế hoạch tháng tới. Mọi số phải lấy từ file tóm tắt; nguồn thiếu thì ghi [CẦN SỐ LIỆU]. Ghi report.md vào thư mục run.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 3 dòng:
    Khách: <slug>
    Báo cáo: <đường dẫn>
    Tháng: <YYYY-MM>
- agent: seo-reviewer
  task: |-
    Kết quả bước trước: {{prev}}
    Mở báo cáo và file tóm tắt. Đối chiếu từng con số trong báo cáo với file tóm tắt; số không truy được là lỗi. Kiểm theo Projects/_templates/review.md. Ghi review_report.md vào thư mục run.
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
    Chỉ làm nếu quyết định là "đạt". Nếu "sửa" thì chỉ cập nhật RUN.md (status=waiting, next_step=sửa báo cáo theo nhận xét) và trả lời "Bỏ qua: báo cáo chưa đạt".
    Nếu đạt: thêm đúng MỘT dòng cho khách và tháng này vào Projects/_registry/portfolio_kpi.csv (cột month, slug, clicks, impressions, avg_position, sessions, conversions, revenue, keywords_top10, geo_mention_rate, pages_published, issues_open). Chỉ dùng số có trong file tóm tắt; ô không có số thì để trống. Không sửa dòng của khách khác. Nếu đã có dòng của khách và tháng này thì không thêm.
    Cập nhật RUN.md: python tools/seo_ops.py set-run <thư mục run> workflow=<slug workflow này> status=waiting "next_step=Người: duyệt report.md trước khi gửi khách; gửi xong chép vào Projects/<slug>/deliverables/ và đặt status=approved" (không chạy được lệnh thì sửa tay khối đầu RUN.md), thêm tên file vừa tạo vào mục "File trong run này", rồi chạy python tools/seo_ops.py build.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 2 dòng:
    Khách: <slug>
    Kết quả: <đã thêm, đã có sẵn, hoặc bỏ qua>
updated: '2026-11-13'
---

Bốn bước. `portfolio_kpi.csv` là file duy nhất dùng chung giữa các khách và chỉ chứa số tổng hợp. Báo cáo gửi khách theo tháng lịch; các tác vụ khác so cửa sổ 4 tuần.
