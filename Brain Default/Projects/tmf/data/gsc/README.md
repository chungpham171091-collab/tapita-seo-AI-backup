Thư mục dữ liệu `gsc` (Google Search Console). Xuất hằng tuần, mỗi file là 7 ngày, ngày trong tên file là ngày cuối của tuần.

- `queries_YYYY-MM-DD.csv`: query, clicks, impressions, ctr, position
- `pages_YYYY-MM-DD.csv`: page, clicks, impressions, ctr, position
- `query_page_YYYY-MM-DD.csv`: page, query, clicks, impressions, ctr, position (dùng để tìm trang cạnh tranh cùng từ khóa)

Không sửa file export gốc. File cũ hơn 13 tuần: người chuyển vào `_archive/` và giữ mỗi tháng một file.
