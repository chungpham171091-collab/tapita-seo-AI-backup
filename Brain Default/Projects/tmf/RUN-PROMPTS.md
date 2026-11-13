# Prompt mẫu cho khách TMF

Dán vào chat của Javis (engine Claude Code). Mỗi workflow chạy từ trang Workflows với đúng một dòng đầu vào; danh sách đầy đủ và đầu vào của từng workflow nằm trong `Projects/CATALOG.md`.

## Prompt 1: cập nhật hồ sơ khách
```
Khách tmf. Cập nhật hồ sơ. Chỉ sửa Projects/tmf/PROJECT.md và Projects/tmf/sources.md. Không đụng khách khác, không sửa projects.csv bằng tay.

Thông tin mới (không biết thì để trống, đừng đoán):
- own_dr (Domain Rating trên Ahrefs):
- branded_keywords (remove hoặc keep):
- KPI và mục tiêu:
- Tone và wording khách yêu cầu:
- Từ cấm hoặc claim cấm:
- Nhóm sản phẩm ưu tiên:
- Link Drive, GSC property, GA4 property ID, Ahrefs project:

Ghi giá trị một dòng vào khối đầu file PROJECT.md; nội dung dài ghi vào mục tương ứng trong thân file. Mục chưa có ghi [CẦN XÁC NHẬN]. Sau đó chạy python tools/seo_ops.py build và python tools/seo_ops.py check, báo kết quả. Chưa commit; đợi tôi duyệt.
```

## Prompt 2: thứ tự chạy dự án đầy đủ đầu tiên
```
Khách tmf. Đọc Projects/SEO-OPS.md, Projects/tmf/PROJECT.md và Projects/CATALOG.md. Chưa chạy gì.
Lập bảng: Thứ tự | Workflow | Dòng đầu vào chính xác (đường dẫn file có thật) | File cần có trước | Đang có chưa | Việc người làm sau workflow.
Theo thứ tự: seo-keyword-seed, seo-keyword-level, seo-keyword-mapping, seo-priority-plan, rồi một collection (seo-content-writing, seo-content-draft, seo-qa-fix), rồi seo-technical-audit.
Với file còn thiếu (Shopify export, export Ahrefs, file nhóm từ khóa, HTML mẫu, own_dr) ghi rõ tên file và thư mục cần đặt. Không bịa số liệu, nguồn, URL. Không dùng thông tin khách khác.
```
