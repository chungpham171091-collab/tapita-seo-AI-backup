Thư mục dữ liệu `tech`: mẫu HTML thô (view-source) để audit kỹ thuật. Lấy lại sau mỗi lần site thay đổi.

- `samples.csv`: template, url, file, note. Mỗi template 3 đến 4 URL (homepage có thể 1), URL lấy từ sitemap, đang trả 200, không có tham số.
- `home_1.html`, `collection_1.html`, `product_1.html`...: HTML lấy bằng view-source (không lấy bản Inspect sau khi JS chạy). Dòng đầu là comment ghi URL gốc. Giữ nguyên thẻ head, JSON-LD và nội dung body; có thể bỏ bớt script thư viện.
