---
client: tmf
task: report
topic: 2026-10
workflow: seo-monthly-report
playbook: report
stage: done
status: approved
owner: Harry
created: 2026-11-19
updated: 2026-11-19
next_step: Xong. Không còn công đoạn nào
live_url:
published_on:
---

# RUN: Monthly report - 2026-10

> Mỗi lượt chạy một tác vụ có một thư mục `Projects/<slug>/runs/YYYY-MM-DD_<task>_<topic>/` và một file RUN.md này.
> Các dòng trong khối đầu file được dùng để sinh bảng run (board.csv): mỗi dòng một giá trị, không xuống dòng.
> status: open (đang làm) | waiting (chờ người quyết định) | qa (đang audit, sửa) | approved (người đã duyệt, file đã vào deliverables/) | published (đã đăng) | cancelled.
> playbook và stage: loại việc và công đoạn hiện tại, do trang Projects ghi (Projects/_templates/playbooks.json); để trống nếu chạy workflow lẻ.
> workflow: slug của workflow vừa chạy gần nhất. next_step: việc kế tiếp và ai làm (người hoặc tên workflow).

## Đầu vào
(Dòng đầu vào đã dùng, từ khóa chính và phụ, URL, file dữ liệu đã đọc.)
- Month: 2026-10

## File trong run này
| File | Bước tạo ra | Ghi chú |
|---|---|---|
| report.md | seo-monthly-report | Chờ người duyệt; số liệu lấy từ tóm tắt test data (test_data: yes), không gửi khách |
| review_report_v2.md | seo-monthly-report (seo-reviewer) | Duyệt report.md bản dựng lại: 95/100, đạt, 0 lỗi số liệu; review_report.md là bản duyệt báo cáo cũ

## Quyết định của người
(Ngày, ai, quyết định gì: chọn title, duyệt outline, duyệt bản cuối.)
- 2026-11-19 Harry: quay lại công đoạn Build the report. Rerun with the rebuilt test data (real export layouts)
- 2026-11-19 Harry: duyệt report.md -> deliverables/
- 2026-11-19 Harry: Sent to client. Sent on: keenan@tapita.io

## Đăng
(Người đăng ghi: URL đã đăng, ngày đăng. Đồng thời thêm một dòng vào `data/changelog.csv` của khách.)
