# CATALOG: danh sách tác vụ SEO-Ops

> File tự sinh từ `workflows/*.md` bằng `python tools/seo_ops.py build`. Không sửa tay.
> Muốn đổi bước của một tác vụ: sửa file workflow rồi chạy lại lệnh build.

| Workflow | Tên | Trạng thái | Chuỗi agent | Đầu vào (một dòng, cách nhau bằng dấu \|) | Skill được gọi |
|---|---|---|---|---|---|
| `seo-blog-outline` | SEO Blog outline (giai đoạn 1b) | off | seo-writer | slug khách \| thư mục run blog \| title đã chọn (số thứ tự trong titles.md hoặc nguyên văn) \| ghi chú chỉnh của người (hoặc "không") | skill_blog (PROJECT.md) |
| `seo-cannibalization-links` | SEO Trang cạnh tranh từ khóa và internal link | off | seo-extractor -> seo-auditor -> seo-planner | slug khách \| chủ đề run (ví dụ YYYY-MM) \| số nhóm tối đa cần xem (ví dụ 20) |  |
| `seo-content-brief` | SEO Content brief | active | seo-planner -> seo-reviewer | slug khách \| URL đích hoặc chủ đề \| từ khóa chính \| loại (blog hoặc collection) |  |
| `seo-content-draft` | SEO Viết nội dung (giai đoạn 2) | active | seo-writer | slug khách \| thư mục run \| ghi chú duyệt outline của người (hoặc "duyệt nguyên bản") | skill_blog (PROJECT.md), skill_collection (PROJECT.md) |
| `seo-content-refresh-update` | SEO Refresh 2 - làm mới một trang | off | seo-writer | slug khách \| thư mục run refresh \| URL trang \| từ khóa chính \| hướng làm mới của người | skill_blog (PROJECT.md), skill_collection (PROJECT.md), skill_product (PROJECT.md) |
| `seo-content-refresh` | SEO Refresh 1 - tìm trang mất click và đề xuất | off | seo-planner | slug khách \| số trang tối đa cần xem (ví dụ 10) \| ghi chú của người (hoặc "không") |  |
| `seo-content-writing` | SEO Viết nội dung (giai đoạn 1) | active | seo-writer | slug khách \| loại (blog hoặc collection) \| từ khóa chính \| từ khóa phụ (cách nhau bằng dấu phẩy, hoặc "không") \| URL collection hoặc chủ đề blog \| thư mục run có sẵn (ví dụ đã có brief) hoặc "mới" \| ghi chú (intent, file top sellers, hoặc "không") | skill_blog (PROJECT.md), skill_collection (PROJECT.md) |
| `seo-data-summary` | SEO Tóm tắt dữ liệu theo kỳ | off | seo-extractor | slug khách \| nguồn (gsc, rank, ga4, keywords hoặc backlinks) \| kỳ (YYYY-MM-DD là ngày cuối của tuần, YYYY-MM là tháng, hoặc "mới nhất") |  |
| `seo-feedback-localization` | SEO Sửa theo feedback và bản địa hóa | active | seo-writer -> seo-auditor | slug khách \| thư mục run của bài \| file bài \| file feedback hoặc "feedback: <nội dung>" \| thị trường đích | harry-reference-check, compliance (PROJECT.md) |
| `seo-geo-optimization` | SEO Tối ưu GEO | active | seo-extractor -> seo-auditor -> seo-planner -> seo-writer | slug khách \| tháng YYYY-MM |  |
| `seo-image-plan` | SEO Kế hoạch ảnh blog | active | seo-writer | slug khách \| thư mục run blog \| file blog hoàn chỉnh trong run |  |
| `seo-keyword-level` | SEO Planning 2 - lọc và xếp level từ khóa | off | seo-extractor | slug khách \| thư mục run planning \| file export Ahrefs (hoặc "mới nhất" để lấy file ahrefs_<country>_*.csv mới nhất trong Projects/<slug>/data/keywords/) |  |
| `seo-keyword-mapping` | SEO Planning 4-5 - keyword mapping và content cluster | off | seo-extractor -> seo-planner -> seo-planner | slug khách \| thư mục run planning \| file nhóm từ khóa trong run (mặc định groups_<country>.csv) |  |
| `seo-keyword-research` | SEO Keyword research | off | seo-extractor -> seo-planner | slug khách \| chủ đề hoặc seed keyword \| thị trường |  |
| `seo-keyword-seed` | SEO Planning 1 - seed từ khóa | off | seo-extractor -> seo-planner | slug khách \| phạm vi (collection, product hoặc cả hai) \| chủ đề run (ví dụ toan-site hoặc tên nhóm sản phẩm) \| số trang tối đa (số, hoặc "tất cả") |  |
| `seo-meta-optimization` | SEO Product 2 - chọn từ khóa chính, meta và content sản phẩm | active | seo-extractor -> seo-writer | slug khách \| thư mục run product \| file Ahrefs trong run (mặc định ahrefs_volume.csv) \| ghi chú chỉnh từ khóa của người (hoặc "không") | skill_product (PROJECT.md) |
| `seo-monthly-report` | SEO Báo cáo tháng | active | seo-extractor -> seo-planner -> seo-reviewer -> seo-extractor | slug khách \| tháng YYYY-MM |  |
| `seo-offpage` | SEO Off-page - hồ sơ backlink, link gap, outreach nháp | off | seo-extractor -> seo-planner -> seo-writer | slug khách \| chủ đề run (ví dụ YYYY-MM) \| file backlink (hoặc "mới nhất") \| file link gap (hoặc "mới nhất", hoặc "không") |  |
| `seo-onpage-audit` | SEO Audit on-page | active | seo-extractor -> seo-auditor -> seo-reviewer | slug khách \| file hoặc danh sách URL cần audit \| từ khóa chính (nếu có) \| chủ đề run | tapita-eeat-check |
| `seo-post-publish-check` | SEO Kiểm tra sau khi đăng | off | seo-auditor | slug khách \| thư mục run của bài đã đăng \| URL đã đăng (hoặc "theo RUN.md") |  |
| `seo-priority-plan` | SEO Planning 6 - bản nháp kế hoạch ưu tiên | off | seo-planner | slug khách \| thư mục run planning \| số tháng của kế hoạch \| ghi chú của người (hoặc "không") |  |
| `seo-product-keywords` | SEO Product 1 - phân tích sản phẩm và bộ từ khóa | off | seo-extractor -> seo-writer | slug khách \| file Shopify export (hoặc "mới nhất" để lấy file shopify_products_*.csv mới nhất trong Projects/<slug>/data/inputs/) \| danh sách URL hoặc handle sản phẩm, cách nhau bằng dấu phẩy \| chủ đề run (ví dụ tên nhóm sản phẩm) | skill_product (PROJECT.md) |
| `seo-qa-fix` | SEO QA và sửa | active | seo-auditor -> seo-writer -> seo-auditor | slug khách \| thư mục run \| file bài trong run (mặc định draft.md) \| từ khóa chính | harry-reference-check, tapita-eeat-check, compliance (PROJECT.md) |
| `seo-technical-audit` | SEO Audit kỹ thuật | active | seo-extractor -> seo-auditor -> seo-planner | slug khách \| chủ đề run (ví dụ ngày lấy mẫu hoặc "sau-fix-1") \| ghi chú phạm vi (ví dụ chỉ product, hoặc "tất cả") |  |

## Ghi chú từng workflow

- `seo-blog-outline`: Một bước, kết thúc để người duyệt outline. Bước kế tiếp là `seo-content-draft`.
- `seo-cannibalization-links`: Ba bước. Cần keyword mapping đã duyệt trong `deliverables/` và các file tuần `query_page_*.csv` trong `data/gsc/`. Kiểm link chỉ trong các trang đã mở, không thay cho crawl toàn site.
- `seo-content-brief`: Brief là tùy chọn, không bắt buộc trước khi viết. Nếu dùng, người duyệt brief rồi chạy `seo-content-writing` với thư mục run của brief.
- `seo-content-draft`: Một bước. Bước kế tiếp luôn là `seo-qa-fix` trên draft.md.
- `seo-content-refresh-update`: Một bước. Bước kế tiếp là `seo-qa-fix` trên file refresh, rồi người duyệt và đăng như mọi bài khác.
- `seo-content-refresh`: Một bước, kết thúc để người chọn trang. Cần `latest_gsc.md` do `seo-data-summary` ghi (đủ 8 file tuần để so 4 tuần với 4 tuần). Bước kế tiếp cho từng trang được chọn là `seo-content-refresh-update`.
- `seo-content-writing`: Một bước, kết thúc ở điểm duyệt đầu tiên của skill. Blog: người chọn title rồi chạy `seo-blog-outline`. Collection: người duyệt outline rồi chạy `seo-content-draft`. Brief (`seo-content-brief`) là tùy chọn; nếu đã chạy thì đưa thư mục run của brief vào đầu vào.
- `seo-data-summary`: Một bước. Chạy sau mỗi lần đặt file export mới vào data/: gsc và rank hằng tuần, ga4 hằng tháng, keywords hằng quý. Người xem mục "File cũ cần người quyết định" và tự chuyển file vào `_archive/`.
- `seo-feedback-localization`: Hai bước. Bài tiếng Việt: người sửa wording sau cùng vì giọng AI còn nặng.
- `seo-geo-optimization`: Bốn bước. Cần có prompts.csv và file citations của tháng (kiểm ChatGPT, Perplexity, Gemini, AI Overviews do người hoặc tool thực hiện). Sau đó chạy `seo-qa-fix` trên file đề xuất trước khi đăng.
- `seo-image-plan`: Một bước. Ảnh được tạo bên ngoài (ví dụ Gemini) rồi người chèn vào bài.
- `seo-keyword-level`: Một bước, chạy sau khi người đã export Ahrefs. Kết thúc để người chạy công cụ nhóm từ khóa của team (Planning bước 3). Lưu ý: sheet để trống khoảng chênh 25 đến 30 điểm DR; workflow tạm xếp phần này vào difficult.
- `seo-keyword-mapping`: Ba bước, chạy sau khi người đã nhóm từ khóa bằng công cụ của team và lưu groups_<country>.csv vào thư mục run. Kết thúc để người xem mapping và cluster.
- `seo-keyword-research`: Hai bước, chạy một lượt. Số liệu thiếu thì giữ trống chứ không ước lượng. Người xem clusters.csv và chốt từ khóa chính, phụ cho từng URL trước khi chạy `seo-content-brief`. ĐÃ TẮT ngày 2026-11-13. Planning chạy theo bốn workflow mới: `seo-keyword-seed`, `seo-keyword-level`, `seo-keyword-mapping`, `seo-priority-plan`.
- `seo-keyword-seed`: Planning bước 1 trong sheet Working Steps. Hai bước, rồi kết thúc. Người chạy Ahrefs Keywords Explorer (Planning bước 2), lưu export vào data/keywords/, rồi chạy `seo-keyword-level`. Cần có `data/inputs/site_urls.csv` và ít nhất một trong hai file dữ liệu trang (Shopify export hoặc url_list.csv).
- `seo-meta-optimization`: Hai bước, chạy sau khi người đã lấy search volume trên Ahrefs. Bước kế tiếp là `seo-qa-fix` trên meta_table.csv. Luật từ khóa volume 0 nằm ở workflow này vì skill sản phẩm chưa có.
- `seo-monthly-report`: Bốn bước. `portfolio_kpi.csv` là file duy nhất dùng chung giữa các khách và chỉ chứa số tổng hợp. Báo cáo gửi khách theo tháng lịch; các tác vụ khác so cửa sổ 4 tuần.
- `seo-offpage`: Ba bước. Cần export backlink của khách và export Link Intersect (khách so với các đối thủ trong PROJECT.md) từ Ahrefs trong `data/backlinks/`. Workflow không gửi email và không tự liên hệ ai.
- `seo-onpage-audit`: Ba bước. Audit chỉ báo lỗi và cách sửa; người hoặc `seo-writer` sửa trong việc riêng.
- `seo-post-publish-check`: Một bước. Chạy sau khi người đã đăng bài và ghi live_url, published_on vào RUN.md và một dòng vào data/changelog.csv. Kết quả đáng tin hơn khi người lưu view-source của trang thành live.html trong thư mục run.
- `seo-priority-plan`: Một bước, kết thúc để người quyết định. Bản keyword mapping đã duyệt trong `deliverables/` là mapping hiện hành mà các tác vụ khác đọc.
- `seo-product-keywords`: Hai bước, kết thúc ở bước Ahrefs giữa quy trình. Đầu vào là Shopify product export đặt trong `data/inputs/`. Bước kế tiếp là `seo-meta-optimization`.
- `seo-qa-fix`: Ba bước, một vòng sửa. Kiểm nguồn chạy trước E-E-A-T trong cùng một lượt audit vì nguồn sai kéo điểm Trust xuống. Dùng chung cho blog, collection, product (bảng meta và content) và bản refresh. Mỗi bước chỉ truyền vài dòng kết quả (đường dẫn file) sang bước sau. Theo sheet, người vẫn nên kiểm tay các link nguồn trước khi duyệt.
- `seo-technical-audit`: Ba bước. Phạm vi theo sheet: chỉ đánh giá dựa trên code, bỏ qua App và dữ liệu GSC. Người chuẩn bị trước: chọn 3 đến 4 URL mỗi template (homepage có thể 1) từ sitemap, lấy HTML bằng view-source (không lấy bản Inspect sau khi JS chạy), lưu vào `data/tech/` (home_1.html, collection_1.html, product_1.html...) với URL gốc ở dòng đầu, và điền `data/tech/samples.csv`. Không dùng file crawl.
