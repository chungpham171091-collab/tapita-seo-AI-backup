---
type: workflow
name: SEO GEO - bộ prompt theo dõi
slug: seo-geo-prompts
status: 'off'
description: 'Soạn bản nháp danh sách prompt cần theo dõi trên các công cụ AI, từ keyword mapping, content cluster và hồ sơ khách. Người duyệt rồi mới dùng.'
steps:
- agent: seo-planner
  task: |-
    Đầu vào: {{input}}
    Đầu vào gồm: slug khách | chủ đề run (ví dụ YYYY-MM) | số prompt mong muốn (ví dụ 30).
    Đọc Projects/SEO-OPS.md và Projects/<slug>/PROJECT.md của đúng khách trong đầu vào. Chỉ làm cho khách đó. Thông tin đã có trong PROJECT.md (thị trường, ngôn ngữ, Google domain, tone, từ cấm, skill, đối thủ) thì dùng luôn, không hỏi lại; thiếu thì nói rõ cần điền mục nào vào PROJECT.md.
    Thư mục run: nếu đầu vào kết thúc bằng phần `run=<đường dẫn>` thì đó là thư mục run của việc này (đã có RUN.md); dùng đúng thư mục đó, không tạo thư mục mới. Nếu không có phần đó thì tạo bằng lệnh: python tools/seo_ops.py new-run <slug> geo-prompts <chủ đề run> seo-geo-prompts (chữ thường, gạch ngang); không chạy được lệnh thì tạo tay Projects/<slug>/runs/<YYYY-MM-DD>_geo-prompts_<chủ đề run>/RUN.md theo Projects/_templates/RUN.md. Mọi file của bước này ghi vào thư mục run đó.
    Đọc keyword mapping và content cluster hiện hành (file keyword_mapping_*.csv, content_cluster_*.csv mới nhất trong Projects/<slug>/deliverables/), mục Nhóm sản phẩm ưu tiên và Đối thủ chính trong PROJECT.md, và Projects/<slug>/data/geo/prompts.csv nếu đã có. Không có mapping thì dùng nhóm sản phẩm ưu tiên trong PROJECT.md và ghi rõ.
    Soạn prompt như người thật hỏi công cụ AI, bằng ngôn ngữ thị trường của khách, trải đều các nhóm sản phẩm ưu tiên và các loại: tìm hiểu (how, what), so sánh và lựa chọn (best, vs), mua ở đâu, và câu hỏi có nêu tên thương hiệu của khách. Mỗi prompt gắn với một từ khóa chính hoặc sub-topic có thật trong mapping. Giữ prompt_id cũ cho prompt đã có; prompt mới đánh số tiếp. Không đưa số liệu hay khẳng định về khách vào prompt.
    Ghi vào thư mục run: prompts_draft.csv (cột: prompt_id, prompt, intent, cluster, priority, source_keyword, status với giá trị cũ hoặc mới) và prompts_notes.md (cách chọn, nhóm nào còn ít prompt, câu hỏi cho người).
    Cập nhật RUN.md: python tools/seo_ops.py set-run <thư mục run> workflow=<slug workflow này> status=waiting "next_step=Người: xem và sửa prompts_draft.csv rồi duyệt; bản duyệt thay cho data/geo/prompts.csv" (không chạy được lệnh thì sửa tay khối đầu RUN.md), thêm tên file vừa tạo vào mục "File trong run này", rồi chạy python tools/seo_ops.py build.
    Dòng đầu tiên của câu trả lời luôn là `Khách: <slug>`.
    Trả lời đúng 4 dòng:
    Khách: <slug>
    Run: <đường dẫn thư mục run>
    Prompt: <tổng số> (mới <n>, giữ lại <n>)
    Câu hỏi cho người: <ngắn, hoặc không>
updated: '2026-11-13'
---

Một bước, kết thúc để người duyệt. Bản duyệt trở thành `data/geo/prompts.csv`, là danh sách người hoặc tool dùng để kiểm các công cụ AI hằng tháng.
