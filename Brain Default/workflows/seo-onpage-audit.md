---
type: workflow
name: SEO Audit on-page
slug: seo-onpage-audit
status: active
description: 'Audit on-page cho danh sách URL: extractor lấy số liệu GSC và rank của các URL, auditor mở trang và audit, reviewer kiểm bằng chứng.'
steps:
- agent: seo-extractor
  task: |-
    Đầu vào: {{input}}
    Đầu vào gồm: slug khách | file hoặc danh sách URL cần audit | từ khóa chính (nếu có) | chủ đề run.
    Đọc Projects/SEO-OPS.md và Projects/<slug>/PROJECT.md của đúng khách trong đầu vào. Chỉ làm cho khách đó. Thông tin đã có trong PROJECT.md (thị trường, ngôn ngữ, Google domain, tone, từ cấm, skill, đối thủ) thì dùng luôn, không hỏi lại; thiếu thì nói rõ cần điền mục nào vào PROJECT.md.
    Tạo thư mục run bằng lệnh: python tools/seo_ops.py new-run <slug> onpage <chủ đề run> seo-onpage-audit (chữ thường, gạch ngang). Không chạy được lệnh thì tạo tay Projects/<slug>/runs/<YYYY-MM-DD>_onpage_<chủ đề run>/RUN.md theo Projects/_templates/RUN.md. Mọi file của bước này ghi vào thư mục run đó.
    Với các URL đã nêu, lấy số liệu từ 4 file tuần gần nhất trong Projects/<slug>/data/gsc/ (pages và queries) và Projects/<slug>/data/rank/, cùng từ khóa chính trong keyword mapping hiện hành (deliverables/). Ghi onpage_input.md vào thư mục run. Nêu rõ URL nào không có dữ liệu.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 4 dòng:
    Khách: <slug>
    Run: <đường dẫn thư mục run>
    Số URL có dữ liệu: <n>/<tổng>
    Thiếu: <file hoặc URL thiếu>
- agent: seo-auditor
  task: |-
    Kết quả bước trước: {{prev}}
    Mở onpage_input.md trong thư mục run, rồi mở từng URL bằng web fetch (giãn request nếu site chặn; ghi URL không mở được). Audit on-page theo tapita-eeat-check và checklist: title, meta, H1 và cấu trúc heading, intent so với từ khóa, nội dung mỏng hoặc trùng, internal link, canonical. Độ dài meta theo skill của loại trang ghi trong PROJECT.md. Mỗi phát hiện ghi: URL, vấn đề, bằng chứng, mức P0 đến P3, cách sửa. Ghi audit_onpage.md vào thư mục run. Không đoán khi thiếu dữ liệu.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 3 dòng:
    Khách: <slug>
    Báo cáo: <đường dẫn>
    Số lỗi: P0=<n>, P1=<n>, P2=<n>, P3=<n>
- agent: seo-reviewer
  task: |-
    Kết quả bước trước: {{prev}}
    Mở báo cáo audit. Kiểm mỗi phát hiện có bằng chứng truy được và mức độ hợp lý; đánh dấu phát hiện thiếu bằng chứng hoặc có vẻ suy đoán. Ghi nhận xét vào review_onpage.md trong thư mục run.
    Cập nhật RUN.md: python tools/seo_ops.py set-run <thư mục run> workflow=<slug workflow này> status=waiting "next_step=Người: chọn lỗi cần sửa; sửa nội dung thì chạy workflow viết hoặc refresh tương ứng" (không chạy được lệnh thì sửa tay khối đầu RUN.md), thêm tên file vừa tạo vào mục "File trong run này", rồi chạy python tools/seo_ops.py build.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 3 dòng:
    Khách: <slug>
    Quyết định: đạt hoặc sửa
    Nhận xét: <đường dẫn>
updated: '2026-11-13'
---

Ba bước. Audit chỉ báo lỗi và cách sửa; người hoặc `seo-writer` sửa trong việc riêng.
