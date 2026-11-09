# SEO-Ops: luật chung

> Đọc file này trước khi làm bất kỳ việc SEO nào cho khách. Mỗi phiên làm cho đúng MỘT khách.

## 1. Bắt đầu một việc
1. Xác định `<slug>` của khách. Đọc dòng của khách trong `Projects/_registry/projects.csv` (market, content_skill, compliance).
2. Đọc `Projects/<slug>/PROJECT.md` và `Projects/<slug>/sources.md`. Không mở thư mục của khách khác.
3. Chọn workflow hoặc skill theo mục 3. Skill có điểm dừng chờ duyệt thì dừng và hỏi người, không tự chạy tiếp.
4. Ghi kết quả vào `Projects/<slug>/outputs/`, rồi báo lại tối đa 5 dòng kèm đường dẫn file.
5. Khi đang làm cho một khách, không đưa tên, domain, số liệu, từ khóa, đối thủ hay thông tin của khách khác vào bài, meta, báo cáo hay đề xuất. Người dùng yêu cầu làm việc cho khách khác thì đề nghị mở phiên mới cho khách đó, kể cả khi thông tin khách kia đã có trong chat.

## 2. Phân vai và model

| Agent | Việc | Model nên đặt |
|---|---|---|
| seo-planner | Cluster từ khóa, brief, run sheet, xếp ưu tiên | Opus |
| seo-reviewer | Chấm điểm và quyết định đạt hoặc sửa trước khi giao | Opus |
| seo-writer | Viết, sửa, meta, feedback, kế hoạch ảnh, bản sửa GEO | Sonnet |
| seo-auditor | Audit nội dung, on-page, technical, GEO. Chỉ báo lỗi | Sonnet |
| seo-extractor | Đọc file lớn, lọc, đếm, tóm tắt. Không khuyến nghị | Haiku |

- Viết và audit do hai agent khác nhau. Auditor đọc lại toàn bộ từ đầu.
- Chỉ extractor đọc file thô lớn; agent khác dùng bản tóm tắt trong `data/_summary/`.
- Việc cần phán đoán (chọn hướng, duyệt cuối) để người quyết định.

## 3. Workflow theo tác vụ
Mỗi workflow nhận MỘT dòng đầu vào, các phần cách nhau bằng dấu `|`.

| Tác vụ | Workflow | Đầu vào | Dừng chờ người |
|---|---|---|---|
| Nghiên cứu và cluster từ khóa | seo-keyword-research | slug \| chủ đề hoặc seed \| thị trường | Chốt từ khóa chính và phụ |
| Brief | seo-content-brief | slug \| URL hoặc cluster \| từ khóa chính \| blog hoặc collection | Duyệt brief |
| Viết, giai đoạn 1 (strategy, outline) | seo-content-writing | slug \| loại \| từ khóa chính \| URL hoặc chủ đề \| file brief hoặc "không" | Duyệt outline |
| Viết, giai đoạn 2 (bản hoàn chỉnh) | seo-content-draft | slug \| file outline đã duyệt \| ghi chú duyệt | Sau đó chạy seo-qa-fix |
| Audit rồi sửa bài | seo-qa-fix | slug \| file bài \| từ khóa chính \| thị trường | Duyệt bản _v2 |
| Meta và content sản phẩm | seo-meta-optimization | slug \| số URL tối đa \| file URL (mặc định data/inputs/url_list.csv) | Chỉnh từ khóa, duyệt bảng |
| Sửa theo feedback, bản địa hóa | seo-feedback-localization | slug \| file bài \| feedback \| thị trường đích | Duyệt bản mới |
| Kế hoạch ảnh blog | seo-image-plan | slug \| file blog hoàn chỉnh | Người tạo ảnh |
| Audit on-page | seo-onpage-audit | slug \| URL hoặc file URL \| từ khóa chính | Chọn lỗi cần sửa |
| Audit kỹ thuật | seo-technical-audit | slug \| file crawl | Duyệt danh sách ưu tiên |
| Tối ưu GEO | seo-geo-optimization | slug \| YYYY-MM | Duyệt đề xuất, rồi seo-qa-fix |
| Báo cáo tháng | seo-monthly-report | slug \| YYYY-MM | Duyệt báo cáo trước khi gửi khách |

Skill theo tác vụ (agent gọi đúng skill, không chép lại nội dung skill):

| Tác vụ | Skill |
|---|---|
| Blog | harry-content (dự án của Cindy: cindy-seo-content, chưa có) |
| Long-form collection Shopify | shopify-collection-seo; TMF: shopify-collection-seo-tmf |
| Meta, content sản phẩm | harry-optimization |
| Audit nội dung | tapita-eeat-check; skill compliance của khách (cột compliance); harry-reference-check khi bài có nguồn |

## 4. Luật nội dung
- Content giao khách viết theo ngôn ngữ thị trường trong registry (en-US, en-GB, de-DE...). Tiếng Việt chỉ dùng cho chat và báo cáo nội bộ.
- Không bịa số liệu, nguồn, trích dẫn. Link nguồn phải mở được. Thiếu nguồn ghi [CẦN NGUỒN]; thiếu số liệu ghi [CẦN SỐ LIỆU].
- Tuân thủ từ cấm và claim cấm trong PROJECT.md và skill compliance của khách.
- Meta title 40 đến 60 ký tự, meta description 140 đến 160 ký tự (tính cả khoảng trắng).
- Blog 1.500 đến 4.000 từ. Long-form collection không có H1.
- Bài tiếng Việt: Claude còn nặng giọng AI, người sửa wording sau khi viết.

## 5. Dữ liệu
- Mỗi khách có `Projects/<slug>/data/`: `inputs/` (site_urls.csv, url_list.csv), `keywords/` (clusters.csv, ahrefs_YYYY-MM.csv), `gsc/`, `ga4/`, `rank/`, `crawl/`, `backlinks/`, `geo/` (prompts.csv, citations_YYYY-MM.csv), `_summary/` (extractor ghi), cùng `inventory.csv`, `changelog.csv`, `manifest.csv`.
- File xuất theo kỳ: `<nguồn>_YYYY-MM.csv`. Không sửa file export gốc; kết quả xử lý ghi thành file mới.
- File thô lớn (GSC, crawl, backlinks) có thể để trên Google Drive; link nằm trong `sources.md`. Brain giữ ngữ cảnh, bản tóm tắt và outputs.
- `Projects/_registry/portfolio_kpi.csv` là file duy nhất dùng chung giữa các khách, chỉ chứa số tổng hợp mỗi tháng.
- Không chép dữ liệu giữa các khách. Không ghi mật khẩu hay token vào bất kỳ file nào.
- Không đưa nội dung trong `Projects/` vào `wiki/` hay `memory/`.

## 6. Template
`Projects/_templates/brief.md`, `review.md`, `report.md`. Review thang 100, ngưỡng đạt mặc định 80.

## 7. Đặt tên
- slug: chữ thường, gạch ngang, không dấu (ví dụ `tmf`, `coway-uk`).
- File ra: `YYYY-MM-DD_<loại>_<chủ-đề>.md`, loại gồm brief, outline, draft, review, meta, audit, plan, report, imageplan. Bản sửa có hậu tố `_v2`.

## 8. Skill
Chỉ dùng các skill trong `skills/` của brain. Không tự tạo hoặc cài skill mới; đề xuất kèm lý do và chờ duyệt.
