---
name: SEO-Ops điều phối dự án
description: Tình hình mọi dự án SEO khách, job đang chờ ai, tạo job và chạy bước AI qua tool seo_projects, không cần mở từng project.
group: Vận hành
---

# SEO-Ops: điều phối dự án khách từ chat chính

## Khi nào dùng
- "Tình hình các dự án thế nào", "khách nào đang chờ duyệt", "tuần này có gì kẹt".
- "Dự án tmf đang tới đâu", "job blog wand glides đang ở bước nào".
- "Tạo job blog cho tmf, từ khóa wand glides", "chạy tiếp bước AI của job đó".
- "Có những loại job nào, cần điền gì".

## Chuẩn bị
- Đọc Projects/SEO-OPS.md một lần nếu chưa đọc trong phiên này (luật chung của SEO-Ops).
- Tool `seo_projects` có trong mọi engine. Không thấy tool thì plugin SEO Projects chưa bật: nói rõ, không tự đọc file thay để tạo job.

## Cách chạy
Gọi tool `seo_projects` với `op`:
- `overview`: toàn bộ dự án: job đang mở, mỗi job đang ở bước nào, chờ ai (dòng có WAITING FOR là đang chờ người), dữ liệu thiếu hoặc quá hạn. Dùng cho mọi câu hỏi tình hình chung.
- `project` + `slug`: một dự án chi tiết (hồ sơ chính, job, dữ liệu, deliverables mới nhất).
- `job` + `slug` + `run`: các bước của một job, file đã có, việc cần làm ở bước hiện tại.
- `job_types` + `slug`: các loại job, từng field và nó đi vào bước nào. Đọc TRƯỚC khi tạo job.
- `create_job` + `slug` + `playbook` + `values` (+ `start: true` để chạy luôn bước AI đầu) + `by` (tên người đang chat).
- `run_stage` + `slug` + `run`: chạy bước AI hiện tại của job.

## Quy trình
1. Câu hỏi tình hình: `overview`, rồi trả lời ngắn: việc đang chờ người (ai, job nào, bước nào) trước, rồi dữ liệu thiếu, rồi phần còn lại. Cần chi tiết một dự án thì `project`.
2. Tạo job: `job_types` của đúng khách, đối chiếu yêu cầu với các field. Thiếu field bắt buộc mà không đoán an toàn được thì hỏi lại đúng field đó. Field có mặc định thì để tool tự điền. Tạo xong báo tên job và bước tiếp theo.
3. Chạy bước AI chỉ khi người dùng bảo chạy. Kết quả hiện trên trang Projects > <khách> > Jobs; không hứa sẽ tự báo lại.
4. Duyệt, xuất bản, gửi khách là việc của người trên trang Projects. Tool không làm, đừng nói là đã làm.

## Bẫy
- Mỗi lần làm nội dung cho khách chỉ dùng thông tin của đúng khách đó. So sánh nhiều khách chỉ cho báo cáo nội bộ.
- Không ghi dữ liệu khách vào memory/ hay wiki/ (CLAUDE.md của vault, mục 9).
- Không bịa số liệu. Thiếu dữ liệu thì nói thiếu file nào (dòng Data của overview).
- Dự án có TEST DATA là dữ liệu giả định: nói rõ khi báo cáo, không coi là số thật.
