---
client:
task:
topic:
workflow:
status: open
owner:
created:
updated:
next_step:
live_url:
published_on:
---

# RUN: <task> - <topic>

> Mỗi lượt chạy một tác vụ có một thư mục `Projects/<slug>/runs/YYYY-MM-DD_<task>_<topic>/` và một file RUN.md này.
> Các dòng trong khối đầu file được dùng để sinh bảng run (board.csv): mỗi dòng một giá trị, không xuống dòng.
> status: open (đang làm) | waiting (chờ người quyết định) | qa (đang audit, sửa) | approved (người đã duyệt, file đã vào deliverables/) | published (đã đăng) | cancelled.
> workflow: slug của workflow vừa chạy gần nhất. next_step: việc kế tiếp và ai làm (người hoặc tên workflow).

## Đầu vào
(Dòng đầu vào đã dùng, từ khóa chính và phụ, URL, file dữ liệu đã đọc.)

## File trong run này
| File | Bước tạo ra | Ghi chú |
|---|---|---|

## Quyết định của người
(Ngày, ai, quyết định gì: chọn title, duyệt outline, duyệt bản cuối.)

## Đăng
(Người đăng ghi: URL đã đăng, ngày đăng. Đồng thời thêm một dòng vào `data/changelog.csv` của khách.)
