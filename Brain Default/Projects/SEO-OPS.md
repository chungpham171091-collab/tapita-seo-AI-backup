# SEO-Ops: luật chung

> Đọc file này trước khi làm bất kỳ việc SEO nào cho khách. Mỗi phiên làm cho đúng MỘT khách.

## 1. Bắt đầu một việc
1. Xác định `<slug>` của khách. Đọc dòng của khách trong `Projects/_registry/projects.csv` (market, content_skill, compliance).
2. Đọc `Projects/<slug>/PROJECT.md` và `Projects/<slug>/sources.md`. Không mở thư mục của khách khác.
3. Chọn skill theo bảng ở mục 3. Skill có điểm dừng chờ duyệt thì dừng và hỏi người, không tự chạy tiếp.
4. Ghi kết quả vào `Projects/<slug>/outputs/`, rồi báo lại tối đa 5 dòng kèm đường dẫn file.

## 2. Phân vai
- `seo-writer` viết và sửa. `seo-auditor` chỉ kiểm tra và báo lỗi, không viết lại. Hai việc do hai agent khác nhau; auditor đọc lại toàn bộ bài từ đầu.
- Việc cần phán đoán (chọn hướng, duyệt cuối) để người quyết định.

## 3. Skill theo tác vụ

| Tác vụ | Agent | Skill |
|---|---|---|
| Blog SEO | seo-writer | harry-content; dự án của Cindy: cindy-seo-content |
| Long-form collection Shopify | seo-writer | shopify-collection-seo; TMF: shopify-collection-seo-tmf |
| Meta title, meta description, content product | seo-writer | harry-optimization |
| Audit nội dung | seo-auditor | tapita-eeat-check; skill compliance của khách (cột compliance); harry-reference-check khi bài có nguồn |
| Sửa theo feedback, dịch, bản địa hóa | seo-writer rồi seo-auditor | skill compliance của khách; harry-reference-check |

Audit rồi sửa chạy bằng workflow `seo-qa-fix`.

## 4. Luật nội dung
- Content giao khách viết theo ngôn ngữ thị trường trong registry (en-GB, de-DE...). Tiếng Việt chỉ dùng cho chat và báo cáo nội bộ.
- Không bịa số liệu, nguồn, trích dẫn. Link nguồn phải mở được. Thiếu nguồn ghi [CẦN NGUỒN].
- Tuân thủ từ cấm và claim cấm trong PROJECT.md và skill compliance của khách.
- Meta title 40 đến 60 ký tự, meta description 140 đến 160 ký tự (tính cả khoảng trắng).
- Blog 1.500 đến 4.000 từ. Long-form collection không có H1.
- Bài tiếng Việt: Claude còn nặng giọng AI, người sửa wording sau khi viết.

## 5. Dữ liệu và Drive
- Drive giữ file khách gửi, raw export và bài đã duyệt. Brain giữ ngữ cảnh và bản nháp. Link Drive của từng khách nằm trong `sources.md`.
- Khi đang làm cho một khách, không đưa tên, domain, số liệu, từ khóa, đối thủ hay bất kỳ thông tin nào của khách khác vào bài viết, meta, báo cáo hay đề xuất của khách đó. Nếu người dùng yêu cầu làm việc cho khách khác, đề nghị mở phiên mới cho khách đó.
- Không chép dữ liệu giữa các khách. Không ghi mật khẩu hay token vào bất kỳ file nào.
- Không đưa nội dung trong `Projects/` vào `wiki/` hay `memory/`.

## 6. Đặt tên
- slug: chữ thường, gạch ngang, không dấu (ví dụ `tmf`, `dream-dresses`).
- File ra: `YYYY-MM-DD_<loại>_<chủ-đề>.md`, loại gồm draft, review, meta, report.

## 7. Skill
Chỉ dùng các skill trong `.claude/skills/`. Không tự tạo hoặc cài skill mới; đề xuất kèm lý do và chờ duyệt.
