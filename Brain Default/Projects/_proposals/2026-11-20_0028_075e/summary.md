# Đề xuất: workflows/seo-monthly-report--tmf.md (người hỏi: Harry)

File đích chưa có; nhân bản từ workflows/seo-monthly-report.md (bản dùng chung) cho dự án tmf.

## Đổi gì
1. Bước seo-planner: báo cáo thêm mục ngắn "Rủi ro tháng tới", đặt sau kế hoạch tháng tới, tối đa 3 gạch đầu dòng, mỗi gạch dựa trên số liệu trong file tóm tắt và ghi kèm số đó; không có số thì bỏ gạch đó.
2. Frontmatter của bản nhân bản: `slug` đổi thành `seo-monthly-report--tmf` (theo luật slug = tên file). Mọi phần khác giữ nguyên.

## Vì sao
Theo yêu cầu của Harry; ràng buộc "chỉ dựa trên file tóm tắt" khớp luật reviewer đối chiếu số với file tóm tắt.

## Ảnh hưởng
- Chỉ dự án tmf, và chỉ khi stage báo cáo trỏ tới bản copy (qua Projects/tmf/playbook_overrides.json, trang Projects tự tạo khi lưu phạm vi "only this project").
- Số phần "Đầu vào gồm:" giữ nguyên (slug khách | tháng), job type không phải sửa. Job khác và khách khác không đổi.

## Cần kiểm sau khi áp dụng
- Chạy thử một báo cáo tháng của tmf: mục "Rủi ro tháng tới" có tối đa 3 gạch, mỗi gạch có số trong file tóm tắt.
- Template Projects/_templates/report.md chưa có mục này; planner thêm theo task, không sửa template. Muốn mọi khách có thì cần đề xuất riêng.
- Bước 1 vẫn gọi `new-run ... seo-monthly-report` cố định (khi không có run=); với pass_run thì không ảnh hưởng.
