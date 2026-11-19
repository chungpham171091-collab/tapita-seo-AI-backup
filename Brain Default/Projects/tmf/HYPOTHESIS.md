# HYPOTHESIS: dữ liệu giả định của TMF

> Tạo ngày 2026-11-13 để test mọi workflow khi chưa có dữ liệu thật. Mọi thứ trong file này là GIẢ ĐỊNH: số liệu, thứ hạng, backlink, giá, nội dung, quyết định duyệt.
> Khi có dữ liệu thật: đặt file thật vào đúng chỗ (xóa hoặc ghi đè file giả định), rồi xóa dòng tương ứng khỏi file này. Khi file này không còn dòng nào trong các bảng: đổi `test_data: yes` thành `test_data: no` trong PROJECT.md và xóa file này.
> Lệnh `python tools/seo_ops.py hypotheses tmf` liệt kê các file giả định còn trên đĩa. Lệnh check cảnh báo khi còn.
> Trong lúc test_data: yes, mọi file kết quả của TMF ghi dòng đầu "DỮ LIỆU GIẢ ĐỊNH - KHÔNG GIAO KHÁCH" và không gửi khách.

> Cập nhật 2026-11-19: file GSC, GA4, rank, GEO và Shopify được làm lại theo đúng bố cục file export thật của từng công cụ; thêm GSC cả tháng và tháng 10/2025 để báo cáo tháng so được tháng trước và cùng kỳ. Ahrefs (keywords, backlinks, link intersect) giữ nguyên, chờ một file thật để khớp cột.

## Hồ sơ khách: giá trị giả định trong PROJECT.md

| Mục | Giá trị giả định | Thay bằng |
|---|---|---|
| own_dr | 25 | Domain Rating thật trên Ahrefs Site Explorer |
| branded_keywords | keep | Quyết định của team: TMF có bán theo brand (Hydro-Force, Parker...) không |
| theme | Dawn | Tên theme thật trong Shopify Admin > Online Store > Themes |
| priority | 1 | Thứ tự ưu tiên của khách trong danh mục |
| report_day | 5 | Ngày gửi báo cáo tháng đã thống nhất với khách |
| test_data | yes | no, khi đã thay hết dữ liệu |
| Mục tiêu và KPI | Tăng 30% clicks Hoses và Wands trong 6 tháng | KPI khách xác nhận |
| Tone of voice | Giọng thợ nói với thợ | Yêu cầu của khách |
| Từ cấm và claim cấm | Danh sách guaranteed, never fails... | Yêu cầu của khách |
| Nhóm sản phẩm ưu tiên | Hoses, Wands, Sprayers, Chemicals | Khách xác nhận |
| Kỹ thuật | Không hreflang, theme Dawn | Kiểm site thật |

Các mục đánh dấu [CẦN XÁC NHẬN] trong PROJECT.md (số năm hoạt động, điểm khác biệt, hãng sản xuất) vẫn là thông tin thật còn thiếu, không phải giả định.

## Dữ liệu đầu vào (data/inputs)

| File | Giả định gì | Thay bằng |
|---|---|---|
| `data/inputs/shopify_products_2026-11-10.csv` | Shopify product export, đủ 39 cột như file Shopify xuất ra. Handle thật; giá, SKU, mô tả, tồn kho, SEO title/description là giả định trừ Inline Sprayer PRO (SKU 70109, 284.99) và V-JET (17.99) lấy từ PROJECT.md. | Shopify Admin > Products > Export > All products > CSV for Excel, Numbers or other spreadsheet programs |
| `data/inputs/url_list.csv` | Meta và nội dung hiện tại của 8 collection và 12 product. URL thật; title collection lấy theo PROJECT.md; meta description, nội dung là giả định. | Shopify export hoặc tool crawl meta (title, meta description, nội dung hiện tại) |
| `data/inputs/top-sellers_high-pressure-solution-line-hoses.csv` | Top sellers của collection high-pressure-solution-line-hoses. Thứ tự bán chạy là giả định. | Shopify Analytics > sản phẩm bán chạy theo collection |

## Từ khóa (data/keywords)

| File | Giả định gì | Thay bằng |
|---|---|---|
| `data/keywords/ahrefs_us_2026-11.csv` | Export Ahrefs Keywords Explorer (us), 49 từ khóa. Toàn bộ volume, KD, CPC, Lowest DR, intent là giả định; từ khóa là đề xuất tay. | Ahrefs Keywords Explorer, country us, tab Matching terms từ seed_for_ahrefs.txt, Export CSV |

## GSC hằng tuần (data/gsc)

13 tuần, từ tuần kết thúc 2026-08-23 đến 2026-11-15. Bố cục cột giống file Search Console xuất ra; query x page theo bố cục của Search Analytics for Sheets.

| File | Giả định gì | Thay bằng |
|---|---|---|
| `data/gsc/queries_2026-08-23.csv` | Queries.csv tuần 2026-08-17 đến 2026-08-23, đúng cột của Search Console (Top queries, Clicks, Impressions, CTR dạng %, Position). Số giả định. | Search Console > Performance > Search results, 7 ngày kết thúc Chủ nhật > Export > Download CSV (file zip: Queries.csv, Pages.csv). Tải zip lên ô GSC ở tab Data |
| `data/gsc/pages_2026-08-23.csv` | Pages.csv tuần 2026-08-17 đến 2026-08-23. Tổng theo trang lớn hơn tổng theo query như export thật (Google ẩn một phần query). Số giả định. | Search Console > Performance > Search results, 7 ngày kết thúc Chủ nhật > Export > Download CSV (file zip: Queries.csv, Pages.csv). Tải zip lên ô GSC ở tab Data |
| `data/gsc/query_page_2026-08-23.csv` | Query x page tuần kết thúc 2026-08-23, cột như Search Analytics for Sheets hoặc API (CTR dạng số thập phân). Có 2 trang giảm click từ 19/10 và 2 cặp trang cạnh tranh cùng query. Số giả định. | Search Analytics for Sheets hoặc Search Console API, dimensions query + page, cùng 7 ngày |
| `data/gsc/queries_2026-08-30.csv` | Queries.csv tuần 2026-08-24 đến 2026-08-30, đúng cột của Search Console (Top queries, Clicks, Impressions, CTR dạng %, Position). Số giả định. | Search Console > Performance > Search results, 7 ngày kết thúc Chủ nhật > Export > Download CSV (file zip: Queries.csv, Pages.csv). Tải zip lên ô GSC ở tab Data |
| `data/gsc/pages_2026-08-30.csv` | Pages.csv tuần 2026-08-24 đến 2026-08-30. Tổng theo trang lớn hơn tổng theo query như export thật (Google ẩn một phần query). Số giả định. | Search Console > Performance > Search results, 7 ngày kết thúc Chủ nhật > Export > Download CSV (file zip: Queries.csv, Pages.csv). Tải zip lên ô GSC ở tab Data |
| `data/gsc/query_page_2026-08-30.csv` | Query x page tuần kết thúc 2026-08-30, cột như Search Analytics for Sheets hoặc API (CTR dạng số thập phân). Có 2 trang giảm click từ 19/10 và 2 cặp trang cạnh tranh cùng query. Số giả định. | Search Analytics for Sheets hoặc Search Console API, dimensions query + page, cùng 7 ngày |
| `data/gsc/queries_2026-09-06.csv` | Queries.csv tuần 2026-08-31 đến 2026-09-06, đúng cột của Search Console (Top queries, Clicks, Impressions, CTR dạng %, Position). Số giả định. | Search Console > Performance > Search results, 7 ngày kết thúc Chủ nhật > Export > Download CSV (file zip: Queries.csv, Pages.csv). Tải zip lên ô GSC ở tab Data |
| `data/gsc/pages_2026-09-06.csv` | Pages.csv tuần 2026-08-31 đến 2026-09-06. Tổng theo trang lớn hơn tổng theo query như export thật (Google ẩn một phần query). Số giả định. | Search Console > Performance > Search results, 7 ngày kết thúc Chủ nhật > Export > Download CSV (file zip: Queries.csv, Pages.csv). Tải zip lên ô GSC ở tab Data |
| `data/gsc/query_page_2026-09-06.csv` | Query x page tuần kết thúc 2026-09-06, cột như Search Analytics for Sheets hoặc API (CTR dạng số thập phân). Có 2 trang giảm click từ 19/10 và 2 cặp trang cạnh tranh cùng query. Số giả định. | Search Analytics for Sheets hoặc Search Console API, dimensions query + page, cùng 7 ngày |
| `data/gsc/queries_2026-09-13.csv` | Queries.csv tuần 2026-09-07 đến 2026-09-13, đúng cột của Search Console (Top queries, Clicks, Impressions, CTR dạng %, Position). Số giả định. | Search Console > Performance > Search results, 7 ngày kết thúc Chủ nhật > Export > Download CSV (file zip: Queries.csv, Pages.csv). Tải zip lên ô GSC ở tab Data |
| `data/gsc/pages_2026-09-13.csv` | Pages.csv tuần 2026-09-07 đến 2026-09-13. Tổng theo trang lớn hơn tổng theo query như export thật (Google ẩn một phần query). Số giả định. | Search Console > Performance > Search results, 7 ngày kết thúc Chủ nhật > Export > Download CSV (file zip: Queries.csv, Pages.csv). Tải zip lên ô GSC ở tab Data |
| `data/gsc/query_page_2026-09-13.csv` | Query x page tuần kết thúc 2026-09-13, cột như Search Analytics for Sheets hoặc API (CTR dạng số thập phân). Có 2 trang giảm click từ 19/10 và 2 cặp trang cạnh tranh cùng query. Số giả định. | Search Analytics for Sheets hoặc Search Console API, dimensions query + page, cùng 7 ngày |
| `data/gsc/queries_2026-09-20.csv` | Queries.csv tuần 2026-09-14 đến 2026-09-20, đúng cột của Search Console (Top queries, Clicks, Impressions, CTR dạng %, Position). Số giả định. | Search Console > Performance > Search results, 7 ngày kết thúc Chủ nhật > Export > Download CSV (file zip: Queries.csv, Pages.csv). Tải zip lên ô GSC ở tab Data |
| `data/gsc/pages_2026-09-20.csv` | Pages.csv tuần 2026-09-14 đến 2026-09-20. Tổng theo trang lớn hơn tổng theo query như export thật (Google ẩn một phần query). Số giả định. | Search Console > Performance > Search results, 7 ngày kết thúc Chủ nhật > Export > Download CSV (file zip: Queries.csv, Pages.csv). Tải zip lên ô GSC ở tab Data |
| `data/gsc/query_page_2026-09-20.csv` | Query x page tuần kết thúc 2026-09-20, cột như Search Analytics for Sheets hoặc API (CTR dạng số thập phân). Có 2 trang giảm click từ 19/10 và 2 cặp trang cạnh tranh cùng query. Số giả định. | Search Analytics for Sheets hoặc Search Console API, dimensions query + page, cùng 7 ngày |
| `data/gsc/queries_2026-09-27.csv` | Queries.csv tuần 2026-09-21 đến 2026-09-27, đúng cột của Search Console (Top queries, Clicks, Impressions, CTR dạng %, Position). Số giả định. | Search Console > Performance > Search results, 7 ngày kết thúc Chủ nhật > Export > Download CSV (file zip: Queries.csv, Pages.csv). Tải zip lên ô GSC ở tab Data |
| `data/gsc/pages_2026-09-27.csv` | Pages.csv tuần 2026-09-21 đến 2026-09-27. Tổng theo trang lớn hơn tổng theo query như export thật (Google ẩn một phần query). Số giả định. | Search Console > Performance > Search results, 7 ngày kết thúc Chủ nhật > Export > Download CSV (file zip: Queries.csv, Pages.csv). Tải zip lên ô GSC ở tab Data |
| `data/gsc/query_page_2026-09-27.csv` | Query x page tuần kết thúc 2026-09-27, cột như Search Analytics for Sheets hoặc API (CTR dạng số thập phân). Có 2 trang giảm click từ 19/10 và 2 cặp trang cạnh tranh cùng query. Số giả định. | Search Analytics for Sheets hoặc Search Console API, dimensions query + page, cùng 7 ngày |
| `data/gsc/queries_2026-10-04.csv` | Queries.csv tuần 2026-09-28 đến 2026-10-04, đúng cột của Search Console (Top queries, Clicks, Impressions, CTR dạng %, Position). Số giả định. | Search Console > Performance > Search results, 7 ngày kết thúc Chủ nhật > Export > Download CSV (file zip: Queries.csv, Pages.csv). Tải zip lên ô GSC ở tab Data |
| `data/gsc/pages_2026-10-04.csv` | Pages.csv tuần 2026-09-28 đến 2026-10-04. Tổng theo trang lớn hơn tổng theo query như export thật (Google ẩn một phần query). Số giả định. | Search Console > Performance > Search results, 7 ngày kết thúc Chủ nhật > Export > Download CSV (file zip: Queries.csv, Pages.csv). Tải zip lên ô GSC ở tab Data |
| `data/gsc/query_page_2026-10-04.csv` | Query x page tuần kết thúc 2026-10-04, cột như Search Analytics for Sheets hoặc API (CTR dạng số thập phân). Có 2 trang giảm click từ 19/10 và 2 cặp trang cạnh tranh cùng query. Số giả định. | Search Analytics for Sheets hoặc Search Console API, dimensions query + page, cùng 7 ngày |
| `data/gsc/queries_2026-10-11.csv` | Queries.csv tuần 2026-10-05 đến 2026-10-11, đúng cột của Search Console (Top queries, Clicks, Impressions, CTR dạng %, Position). Số giả định. | Search Console > Performance > Search results, 7 ngày kết thúc Chủ nhật > Export > Download CSV (file zip: Queries.csv, Pages.csv). Tải zip lên ô GSC ở tab Data |
| `data/gsc/pages_2026-10-11.csv` | Pages.csv tuần 2026-10-05 đến 2026-10-11. Tổng theo trang lớn hơn tổng theo query như export thật (Google ẩn một phần query). Số giả định. | Search Console > Performance > Search results, 7 ngày kết thúc Chủ nhật > Export > Download CSV (file zip: Queries.csv, Pages.csv). Tải zip lên ô GSC ở tab Data |
| `data/gsc/query_page_2026-10-11.csv` | Query x page tuần kết thúc 2026-10-11, cột như Search Analytics for Sheets hoặc API (CTR dạng số thập phân). Có 2 trang giảm click từ 19/10 và 2 cặp trang cạnh tranh cùng query. Số giả định. | Search Analytics for Sheets hoặc Search Console API, dimensions query + page, cùng 7 ngày |
| `data/gsc/queries_2026-10-18.csv` | Queries.csv tuần 2026-10-12 đến 2026-10-18, đúng cột của Search Console (Top queries, Clicks, Impressions, CTR dạng %, Position). Số giả định. | Search Console > Performance > Search results, 7 ngày kết thúc Chủ nhật > Export > Download CSV (file zip: Queries.csv, Pages.csv). Tải zip lên ô GSC ở tab Data |
| `data/gsc/pages_2026-10-18.csv` | Pages.csv tuần 2026-10-12 đến 2026-10-18. Tổng theo trang lớn hơn tổng theo query như export thật (Google ẩn một phần query). Số giả định. | Search Console > Performance > Search results, 7 ngày kết thúc Chủ nhật > Export > Download CSV (file zip: Queries.csv, Pages.csv). Tải zip lên ô GSC ở tab Data |
| `data/gsc/query_page_2026-10-18.csv` | Query x page tuần kết thúc 2026-10-18, cột như Search Analytics for Sheets hoặc API (CTR dạng số thập phân). Có 2 trang giảm click từ 19/10 và 2 cặp trang cạnh tranh cùng query. Số giả định. | Search Analytics for Sheets hoặc Search Console API, dimensions query + page, cùng 7 ngày |
| `data/gsc/queries_2026-10-25.csv` | Queries.csv tuần 2026-10-19 đến 2026-10-25, đúng cột của Search Console (Top queries, Clicks, Impressions, CTR dạng %, Position). Số giả định. | Search Console > Performance > Search results, 7 ngày kết thúc Chủ nhật > Export > Download CSV (file zip: Queries.csv, Pages.csv). Tải zip lên ô GSC ở tab Data |
| `data/gsc/pages_2026-10-25.csv` | Pages.csv tuần 2026-10-19 đến 2026-10-25. Tổng theo trang lớn hơn tổng theo query như export thật (Google ẩn một phần query). Số giả định. | Search Console > Performance > Search results, 7 ngày kết thúc Chủ nhật > Export > Download CSV (file zip: Queries.csv, Pages.csv). Tải zip lên ô GSC ở tab Data |
| `data/gsc/query_page_2026-10-25.csv` | Query x page tuần kết thúc 2026-10-25, cột như Search Analytics for Sheets hoặc API (CTR dạng số thập phân). Có 2 trang giảm click từ 19/10 và 2 cặp trang cạnh tranh cùng query. Số giả định. | Search Analytics for Sheets hoặc Search Console API, dimensions query + page, cùng 7 ngày |
| `data/gsc/queries_2026-11-01.csv` | Queries.csv tuần 2026-10-26 đến 2026-11-01, đúng cột của Search Console (Top queries, Clicks, Impressions, CTR dạng %, Position). Số giả định. | Search Console > Performance > Search results, 7 ngày kết thúc Chủ nhật > Export > Download CSV (file zip: Queries.csv, Pages.csv). Tải zip lên ô GSC ở tab Data |
| `data/gsc/pages_2026-11-01.csv` | Pages.csv tuần 2026-10-26 đến 2026-11-01. Tổng theo trang lớn hơn tổng theo query như export thật (Google ẩn một phần query). Số giả định. | Search Console > Performance > Search results, 7 ngày kết thúc Chủ nhật > Export > Download CSV (file zip: Queries.csv, Pages.csv). Tải zip lên ô GSC ở tab Data |
| `data/gsc/query_page_2026-11-01.csv` | Query x page tuần kết thúc 2026-11-01, cột như Search Analytics for Sheets hoặc API (CTR dạng số thập phân). Có 2 trang giảm click từ 19/10 và 2 cặp trang cạnh tranh cùng query. Số giả định. | Search Analytics for Sheets hoặc Search Console API, dimensions query + page, cùng 7 ngày |
| `data/gsc/queries_2026-11-08.csv` | Queries.csv tuần 2026-11-02 đến 2026-11-08, đúng cột của Search Console (Top queries, Clicks, Impressions, CTR dạng %, Position). Số giả định. | Search Console > Performance > Search results, 7 ngày kết thúc Chủ nhật > Export > Download CSV (file zip: Queries.csv, Pages.csv). Tải zip lên ô GSC ở tab Data |
| `data/gsc/pages_2026-11-08.csv` | Pages.csv tuần 2026-11-02 đến 2026-11-08. Tổng theo trang lớn hơn tổng theo query như export thật (Google ẩn một phần query). Số giả định. | Search Console > Performance > Search results, 7 ngày kết thúc Chủ nhật > Export > Download CSV (file zip: Queries.csv, Pages.csv). Tải zip lên ô GSC ở tab Data |
| `data/gsc/query_page_2026-11-08.csv` | Query x page tuần kết thúc 2026-11-08, cột như Search Analytics for Sheets hoặc API (CTR dạng số thập phân). Có 2 trang giảm click từ 19/10 và 2 cặp trang cạnh tranh cùng query. Số giả định. | Search Analytics for Sheets hoặc Search Console API, dimensions query + page, cùng 7 ngày |
| `data/gsc/queries_2026-11-15.csv` | Queries.csv tuần 2026-11-09 đến 2026-11-15, đúng cột của Search Console (Top queries, Clicks, Impressions, CTR dạng %, Position). Số giả định. | Search Console > Performance > Search results, 7 ngày kết thúc Chủ nhật > Export > Download CSV (file zip: Queries.csv, Pages.csv). Tải zip lên ô GSC ở tab Data |
| `data/gsc/pages_2026-11-15.csv` | Pages.csv tuần 2026-11-09 đến 2026-11-15. Tổng theo trang lớn hơn tổng theo query như export thật (Google ẩn một phần query). Số giả định. | Search Console > Performance > Search results, 7 ngày kết thúc Chủ nhật > Export > Download CSV (file zip: Queries.csv, Pages.csv). Tải zip lên ô GSC ở tab Data |
| `data/gsc/query_page_2026-11-15.csv` | Query x page tuần kết thúc 2026-11-15, cột như Search Analytics for Sheets hoặc API (CTR dạng số thập phân). Có 2 trang giảm click từ 19/10 và 2 cặp trang cạnh tranh cùng query. Số giả định. | Search Analytics for Sheets hoặc Search Console API, dimensions query + page, cùng 7 ngày |

## GSC cả tháng (data/gsc, month_*)

Bốn tháng: 2026-08, 2026-09, 2026-10 và 2025-10 (để so cùng kỳ năm trước). Mỗi tháng ba file như trong zip Search Console: Pages, Queries, Dates.

| File | Giả định gì | Thay bằng |
|---|---|---|
| `data/gsc/month_pages_2025-10.csv` | Pages.csv cả tháng 2025-10. Số giả định. | Search Console > Performance, Custom: ngày 1 đến cuối tháng > Export > Download CSV; tải zip lên ô Search Console - whole month |
| `data/gsc/month_queries_2025-10.csv` | Queries.csv cả tháng 2025-10. Số giả định. | Search Console > Performance, Custom: ngày 1 đến cuối tháng > Export > Download CSV; tải zip lên ô Search Console - whole month |
| `data/gsc/month_dates_2025-10.csv` | Dates.csv cả tháng 2025-10: tổng theo ngày của cả site, nguồn đúng cho tổng clicks và impressions của tháng. Số giả định. | Search Console > Performance, Custom: ngày 1 đến cuối tháng > Export > Download CSV; tải zip lên ô Search Console - whole month |
| `data/gsc/month_pages_2026-08.csv` | Pages.csv cả tháng 2026-08. Số giả định. | Search Console > Performance, Custom: ngày 1 đến cuối tháng > Export > Download CSV; tải zip lên ô Search Console - whole month |
| `data/gsc/month_queries_2026-08.csv` | Queries.csv cả tháng 2026-08. Số giả định. | Search Console > Performance, Custom: ngày 1 đến cuối tháng > Export > Download CSV; tải zip lên ô Search Console - whole month |
| `data/gsc/month_dates_2026-08.csv` | Dates.csv cả tháng 2026-08: tổng theo ngày của cả site, nguồn đúng cho tổng clicks và impressions của tháng. Số giả định. | Search Console > Performance, Custom: ngày 1 đến cuối tháng > Export > Download CSV; tải zip lên ô Search Console - whole month |
| `data/gsc/month_pages_2026-09.csv` | Pages.csv cả tháng 2026-09. Số giả định. | Search Console > Performance, Custom: ngày 1 đến cuối tháng > Export > Download CSV; tải zip lên ô Search Console - whole month |
| `data/gsc/month_queries_2026-09.csv` | Queries.csv cả tháng 2026-09. Số giả định. | Search Console > Performance, Custom: ngày 1 đến cuối tháng > Export > Download CSV; tải zip lên ô Search Console - whole month |
| `data/gsc/month_dates_2026-09.csv` | Dates.csv cả tháng 2026-09: tổng theo ngày của cả site, nguồn đúng cho tổng clicks và impressions của tháng. Số giả định. | Search Console > Performance, Custom: ngày 1 đến cuối tháng > Export > Download CSV; tải zip lên ô Search Console - whole month |
| `data/gsc/month_pages_2026-10.csv` | Pages.csv cả tháng 2026-10. Số giả định. | Search Console > Performance, Custom: ngày 1 đến cuối tháng > Export > Download CSV; tải zip lên ô Search Console - whole month |
| `data/gsc/month_queries_2026-10.csv` | Queries.csv cả tháng 2026-10. Số giả định. | Search Console > Performance, Custom: ngày 1 đến cuối tháng > Export > Download CSV; tải zip lên ô Search Console - whole month |
| `data/gsc/month_dates_2026-10.csv` | Dates.csv cả tháng 2026-10: tổng theo ngày của cả site, nguồn đúng cho tổng clicks và impressions của tháng. Số giả định. | Search Console > Performance, Custom: ngày 1 đến cuối tháng > Export > Download CSV; tải zip lên ô Search Console - whole month |

## Rank hằng tuần (data/rank)

| File | Giả định gì | Thay bằng |
|---|---|---|
| `data/rank/rank_2026-08-23.csv` | Thứ hạng tuần 2026-08-23 của 14 từ khóa chính đã mapping, lấy từ vị trí trung bình của đúng trang đó trong GSC giả định. Định dạng theo data_sources.csv (keyword, url, position, search_volume, date). | Export hằng tuần của tool rank tracking team dùng (cần xác nhận tool để khớp đúng cột) |
| `data/rank/rank_2026-08-30.csv` | Thứ hạng tuần 2026-08-30 của 14 từ khóa chính đã mapping, lấy từ vị trí trung bình của đúng trang đó trong GSC giả định. Định dạng theo data_sources.csv (keyword, url, position, search_volume, date). | Export hằng tuần của tool rank tracking team dùng (cần xác nhận tool để khớp đúng cột) |
| `data/rank/rank_2026-09-06.csv` | Thứ hạng tuần 2026-09-06 của 14 từ khóa chính đã mapping, lấy từ vị trí trung bình của đúng trang đó trong GSC giả định. Định dạng theo data_sources.csv (keyword, url, position, search_volume, date). | Export hằng tuần của tool rank tracking team dùng (cần xác nhận tool để khớp đúng cột) |
| `data/rank/rank_2026-09-13.csv` | Thứ hạng tuần 2026-09-13 của 14 từ khóa chính đã mapping, lấy từ vị trí trung bình của đúng trang đó trong GSC giả định. Định dạng theo data_sources.csv (keyword, url, position, search_volume, date). | Export hằng tuần của tool rank tracking team dùng (cần xác nhận tool để khớp đúng cột) |
| `data/rank/rank_2026-09-20.csv` | Thứ hạng tuần 2026-09-20 của 14 từ khóa chính đã mapping, lấy từ vị trí trung bình của đúng trang đó trong GSC giả định. Định dạng theo data_sources.csv (keyword, url, position, search_volume, date). | Export hằng tuần của tool rank tracking team dùng (cần xác nhận tool để khớp đúng cột) |
| `data/rank/rank_2026-09-27.csv` | Thứ hạng tuần 2026-09-27 của 14 từ khóa chính đã mapping, lấy từ vị trí trung bình của đúng trang đó trong GSC giả định. Định dạng theo data_sources.csv (keyword, url, position, search_volume, date). | Export hằng tuần của tool rank tracking team dùng (cần xác nhận tool để khớp đúng cột) |
| `data/rank/rank_2026-10-04.csv` | Thứ hạng tuần 2026-10-04 của 14 từ khóa chính đã mapping, lấy từ vị trí trung bình của đúng trang đó trong GSC giả định. Định dạng theo data_sources.csv (keyword, url, position, search_volume, date). | Export hằng tuần của tool rank tracking team dùng (cần xác nhận tool để khớp đúng cột) |
| `data/rank/rank_2026-10-11.csv` | Thứ hạng tuần 2026-10-11 của 14 từ khóa chính đã mapping, lấy từ vị trí trung bình của đúng trang đó trong GSC giả định. Định dạng theo data_sources.csv (keyword, url, position, search_volume, date). | Export hằng tuần của tool rank tracking team dùng (cần xác nhận tool để khớp đúng cột) |
| `data/rank/rank_2026-10-18.csv` | Thứ hạng tuần 2026-10-18 của 14 từ khóa chính đã mapping, lấy từ vị trí trung bình của đúng trang đó trong GSC giả định. Định dạng theo data_sources.csv (keyword, url, position, search_volume, date). | Export hằng tuần của tool rank tracking team dùng (cần xác nhận tool để khớp đúng cột) |
| `data/rank/rank_2026-10-25.csv` | Thứ hạng tuần 2026-10-25 của 14 từ khóa chính đã mapping, lấy từ vị trí trung bình của đúng trang đó trong GSC giả định. Định dạng theo data_sources.csv (keyword, url, position, search_volume, date). | Export hằng tuần của tool rank tracking team dùng (cần xác nhận tool để khớp đúng cột) |
| `data/rank/rank_2026-11-01.csv` | Thứ hạng tuần 2026-11-01 của 14 từ khóa chính đã mapping, lấy từ vị trí trung bình của đúng trang đó trong GSC giả định. Định dạng theo data_sources.csv (keyword, url, position, search_volume, date). | Export hằng tuần của tool rank tracking team dùng (cần xác nhận tool để khớp đúng cột) |
| `data/rank/rank_2026-11-08.csv` | Thứ hạng tuần 2026-11-08 của 14 từ khóa chính đã mapping, lấy từ vị trí trung bình của đúng trang đó trong GSC giả định. Định dạng theo data_sources.csv (keyword, url, position, search_volume, date). | Export hằng tuần của tool rank tracking team dùng (cần xác nhận tool để khớp đúng cột) |
| `data/rank/rank_2026-11-15.csv` | Thứ hạng tuần 2026-11-15 của 14 từ khóa chính đã mapping, lấy từ vị trí trung bình của đúng trang đó trong GSC giả định. Định dạng theo data_sources.csv (keyword, url, position, search_volume, date). | Export hằng tuần của tool rank tracking team dùng (cần xác nhận tool để khớp đúng cột) |

## GA4 hằng tháng (data/ga4)

| File | Giả định gì | Thay bằng |
|---|---|---|
| `data/ga4/landing_2025-10.csv` | GA4 Landing page, organic, tháng 2025-10, theo bố cục file CSV GA4 tải về (khối dòng # ở đầu, rồi bảng). Sessions khớp tương đối với clicks GSC cùng tháng. Số giả định. | GA4 > Reports > Engagement > Landing page, lọc Session default channel group = Organic Search, cả tháng > Share > Download File > CSV |
| `data/ga4/landing_2026-08.csv` | GA4 Landing page, organic, tháng 2026-08, theo bố cục file CSV GA4 tải về (khối dòng # ở đầu, rồi bảng). Sessions khớp tương đối với clicks GSC cùng tháng. Số giả định. | GA4 > Reports > Engagement > Landing page, lọc Session default channel group = Organic Search, cả tháng > Share > Download File > CSV |
| `data/ga4/landing_2026-09.csv` | GA4 Landing page, organic, tháng 2026-09, theo bố cục file CSV GA4 tải về (khối dòng # ở đầu, rồi bảng). Sessions khớp tương đối với clicks GSC cùng tháng. Số giả định. | GA4 > Reports > Engagement > Landing page, lọc Session default channel group = Organic Search, cả tháng > Share > Download File > CSV |
| `data/ga4/landing_2026-10.csv` | GA4 Landing page, organic, tháng 2026-10, theo bố cục file CSV GA4 tải về (khối dòng # ở đầu, rồi bảng). Sessions khớp tương đối với clicks GSC cùng tháng. Số giả định. | GA4 > Reports > Engagement > Landing page, lọc Session default channel group = Organic Search, cả tháng > Share > Download File > CSV |

## Tóm tắt (data/_summary)

| File | Giả định gì | Thay bằng |
|---|---|---|
| `data/_summary/2026-11-15_gsc.md` | Tóm tắt GSC kỳ 2026-11-15, tính đúng từ file GSC giả định. | seo-data-summary với nguồn gsc |
| `data/_summary/2026-11-08_gsc.md` | Tóm tắt GSC kỳ 2026-11-08, tính lại từ file GSC giả định mới. | seo-data-summary với nguồn gsc |
| `data/_summary/latest_gsc.md` | Bản latest GSC (giống bản 2026-11-15). | seo-data-summary ghi đè |
| `data/_summary/latest_rank.md` | Tóm tắt rank tuần 2026-11-15 so với 4 tuần trước, tính từ file rank giả định. | seo-data-summary với nguồn rank |

## HTML mẫu kỹ thuật (data/tech)

| File | Giả định gì | Thay bằng |
|---|---|---|
| `data/tech/home_1.html` | HTML mẫu home số 1: Ảnh đầu trang đang lazy load | view-source:https://shop.truckmountforums.com/, lưu nguyên văn, URL ở dòng đầu |
| `data/tech/collection_1.html` | HTML mẫu collection số 1: Có H1 và CollectionPage | view-source:https://shop.truckmountforums.com/collections/high-pressure-solution-line-hoses, lưu nguyên văn, URL ở dòng đầu |
| `data/tech/collection_2.html` | HTML mẫu collection số 2: Thiếu meta description, thiếu ItemList | view-source:https://shop.truckmountforums.com/collections/hose-cuffs, lưu nguyên văn, URL ở dòng đầu |
| `data/tech/collection_3.html` | HTML mẫu collection số 3: Link sản phẩm render bằng JS | view-source:https://shop.truckmountforums.com/collections/wands-wand-parts, lưu nguyên văn, URL ở dòng đầu |
| `data/tech/product_1.html` | HTML mẫu product số 1: Product schema thiếu availability | view-source:https://shop.truckmountforums.com/products/carpet-cleaning-inline-sprayer, lưu nguyên văn, URL ở dòng đầu |
| `data/tech/product_2.html` | HTML mẫu product số 2: Hai thẻ H1; canonical trỏ về URL có ?variant= | view-source:https://shop.truckmountforums.com/products/11001-hi-flow-ss-jets-for-carpet-cleaning-wands, lưu nguyên văn, URL ở dòng đầu |
| `data/tech/product_3.html` | HTML mẫu product số 3: Product schema trùng 2 lần; ảnh thiếu alt | view-source:https://shop.truckmountforums.com/products/hydro-force-pro-solution-hose-50-feet, lưu nguyên văn, URL ở dòng đầu |
| `data/tech/samples.csv` | Bảng URL mẫu cho audit kỹ thuật (7 URL thật, 3 template). Mỗi template chỉ có 3 mẫu (sheet yêu cầu 3-4). | Người chọn 3-4 URL mỗi template từ sitemap |

## Backlink (data/backlinks)

| File | Giả định gì | Thay bằng |
|---|---|---|
| `data/backlinks/ahrefs_backlinks_2026-11.csv` | Export backlink của TMF, 40 link. Domain dùng đuôi .example (không có thật); DR, anchor, ngày là giả định. | Ahrefs Site Explorer > Backlinks (shop.truckmountforums.com), Export CSV |
| `data/backlinks/link_intersect_2026-11.csv` | Export Link Intersect TMF so với 7 đối thủ trong PROJECT.md, 15 domain .example (không có thật). Giả định. | Ahrefs Link Intersect: target là 7 đối thủ, 'but doesn't link to' shop.truckmountforums.com, Export CSV |

## GEO (data/geo)

| File | Giả định gì | Thay bằng |
|---|---|---|
| `data/geo/prompts.csv` | 8 prompt GEO cần theo dõi. Giả định. | Team chọn prompt theo cluster và hỏi khách |
| `data/geo/citations_2026-09.csv` | Kiểm 4 engine AI cho 8 prompt, tháng 2026-09, có cột source_urls. Nguồn là trang có thật nhưng việc chúng được trích là giả định. | Người hoặc tool kiểm ChatGPT, Perplexity, Gemini, AI Overviews theo prompts.csv |
| `data/geo/citations_2026-10.csv` | Kiểm 4 engine AI cho 8 prompt, tháng 2026-10, có cột source_urls. Nguồn là trang có thật nhưng việc chúng được trích là giả định. | Người hoặc tool kiểm ChatGPT, Perplexity, Gemini, AI Overviews theo prompts.csv |

## Nhật ký dữ liệu

| File | Giả định gì | Thay bằng |
|---|---|---|
| `data/changelog.csv` | Một dòng đăng bài giả định. | Người ghi mỗi lần đăng hoặc sửa trang |
| `data/manifest.csv` | Danh mục file dữ liệu giả định. | Cập nhật khi đặt file export thật |

## Deliverables 'đã duyệt'

| File | Giả định gì | Thay bằng |
|---|---|---|
| `deliverables/keyword_mapping_us.csv` | Keyword mapping 'đã duyệt' (14 URL). Toàn bộ là giả định, dựng từ groups_us.csv. | seo-keyword-mapping chạy trên dữ liệu thật, người duyệt rồi chép vào deliverables/ |
| `deliverables/content_cluster_us.csv` | Content cluster 'đã duyệt', 5 topic. | seo-keyword-mapping, người duyệt |
| `deliverables/priority_plan.csv` | Kế hoạch ưu tiên 'đã duyệt' 3 tháng. Giả định. | seo-priority-plan, người quyết định |
| `deliverables/collection_hose-cuffs_approved.md` | File 'đã duyệt' của collection hose-cuffs. Nội dung tự viết để test, không đúng trang thật. | Bản cuối người duyệt sau seo-qa-fix |

## Thư mục run dựng sẵn

| File | Giả định gì | Thay bằng |
|---|---|---|
| `runs/2026-11-13_planning_hypothesis/RUN.md` | Thư mục run planning dựng sẵn, đang chờ seo-keyword-mapping. | Tạo bằng seo-keyword-seed, seo-keyword-level với dữ liệu thật |
| `runs/2026-11-13_planning_hypothesis/job.json` | Trạng thái job dựng sẵn (công đoạn mapping). | Job thật tạo từ trang Projects |
| `runs/2026-11-13_planning_hypothesis/pages.csv` | Dữ liệu trang (kết quả bước seed) dựng từ url_list.csv giả định. | seo-keyword-seed sinh ra |
| `runs/2026-11-13_planning_hypothesis/keywords_us.csv` | Kết quả bước level (own_dr giả định 25). | seo-keyword-level sinh ra từ export Ahrefs thật |
| `runs/2026-11-13_planning_hypothesis/groups_us.csv` | Kết quả công cụ nhóm từ khóa của team, 15 nhóm. Cách nhóm là giả định. | Công cụ nhóm từ khóa của team (Google Sheet), export CSV |
| `runs/2026-11-13_product_hypothesis/RUN.md` | Thư mục run product dựng sẵn, đang chờ seo-meta-optimization. | seo-product-keywords chạy với Shopify export thật |
| `runs/2026-11-13_product_hypothesis/job.json` | Trạng thái job dựng sẵn (công đoạn meta). | Job thật tạo từ trang Projects |
| `runs/2026-11-13_product_hypothesis/products.csv` | Dữ liệu 4 sản phẩm lấy từ Shopify export giả định. | seo-product-keywords sinh ra |
| `runs/2026-11-13_product_hypothesis/product_keywords.csv` | Bộ từ khóa sản phẩm (rút gọn, chưa đủ 22-33 từ khóa như skill yêu cầu). | seo-product-keywords sinh ra theo harry-optimization |
| `runs/2026-11-13_product_hypothesis/keywords_for_ahrefs.txt` | Danh sách từ khóa đưa vào Ahrefs. | seo-product-keywords sinh ra |
| `runs/2026-11-13_product_hypothesis/ahrefs_volume.csv` | Export volume Ahrefs cho từ khóa sản phẩm; có từ khóa volume 0 và một từ khóa không có trong export để test luật SV 0. | Ahrefs Keywords Explorer, country us, Export CSV |
| `runs/2026-11-13_product_hypothesis/product_analysis.md` | Bảng phân tích sản phẩm rút gọn. | seo-product-keywords sinh ra |
| `runs/2026-11-13_collection_hypothesis-published/RUN.md` | Thư mục run collection 'đã đăng' để test kiểm tra sau khi đăng. Trang hose-cuffs thật CHƯA đăng bài này, nên kết quả kiểm sẽ báo lệch: đó là điều mong đợi. | Run thật sau khi người đăng bài và ghi live_url |
| `runs/2026-11-13_collection_hypothesis-published/job.json` | Trạng thái job dựng sẵn (công đoạn postcheck). | Job thật tạo từ trang Projects |
| `runs/2026-11-13_blog_hypothesis-qa/RUN.md` | Thư mục run blog có draft lỗi cố ý, để test seo-qa-fix. | Run thật từ seo-content-writing, seo-blog-outline, seo-content-draft |
| `runs/2026-11-13_blog_hypothesis-qa/job.json` | Trạng thái job dựng sẵn (công đoạn qa). | Job thật tạo từ trang Projects |
| `runs/2026-11-13_blog_hypothesis-qa/draft.md` | Bản nháp blog lỗi cố ý: meta sai độ dài, số liệu và nguồn bịa (.example), claim tuyệt đối, link nội bộ không có trong site_urls.csv, văn AI, nhãn [CẦN NGUỒN]. | seo-content-draft sinh ra |

## Điều cố ý trong dữ liệu giả định (để biết test có bắt được không)

- GSC: collection high-pressure-solution-line-hoses và blog orbot-sprayborg-vs-orbot-vibe giảm click mạnh ở 4 tuần gần nhất (test seo-content-refresh).
- GSC: query truck mount solution hose và carpet cleaning solution hose xuất hiện ở cả collection solution hose và product solution hose; carpet cleaning wand ở cả collection wands và product Revolution wand (test seo-cannibalization-links).
- Ahrefs: có từ khóa Local và Branded (test lọc của seo-keyword-level); có từ khóa Lowest DR trong khoảng chênh 25-30 điểm.
- Product: từ khóa volume 0 và một từ khóa không có trong export Ahrefs (test luật SV 0 của seo-meta-optimization).
- HTML mẫu: ảnh đầu trang lazy load, thiếu meta description, link sản phẩm render bằng JS, Product thiếu availability, hai H1, canonical có ?variant=, Product schema trùng, ảnh thiếu alt (test seo-technical-audit).
- Blog draft: meta sai độ dài, số liệu và nguồn bịa, claim tuyệt đối, link nội bộ không có thật, văn AI (test seo-qa-fix).
- Collection 'đã đăng' hose-cuffs: trang thật chưa có nội dung này, nên seo-post-publish-check phải báo lệch.
