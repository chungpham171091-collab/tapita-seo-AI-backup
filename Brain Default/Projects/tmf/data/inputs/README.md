Thư mục `inputs`: danh sách URL và dữ liệu trang của site.

- `site_urls.csv`: type, url (type gồm homepage, collection, product, blog, page). Lấy từ sitemap; cập nhật khi site đổi.
- `url_list.csv`: url, meta_title_current, meta_description_current, content_current. Dữ liệu trang hiện tại cho mọi loại trang.
- `shopify_products_YYYY-MM-DD.csv`: Shopify product export (Products > Export, CSV for Excel or Numbers). Đầu vào của tác vụ sản phẩm và seed từ khóa.
- File top sellers hoặc danh sách sản phẩm của một collection (tùy chọn): `top-sellers_<handle-collection>.csv` với cột url, title. Nêu tên file trong ghi chú khi chạy seo-content-writing.

Không sửa file export gốc.
