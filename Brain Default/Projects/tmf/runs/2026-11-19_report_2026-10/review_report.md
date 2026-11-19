DỮ LIỆU GIẢ ĐỊNH - KHÔNG GIAO KHÁCH

# REVIEW: report.md (tmf, báo cáo tháng 2026-10)

- File duyệt: `Projects/tmf/runs/2026-11-19_report_2026-10/report.md` (102 dòng, đọc toàn bộ)
- File đối chiếu: `Projects/tmf/data/_summary/2026-10_report-data.md` (tóm tắt), cùng RUN.md trong `Projects/tmf/runs/`, `Projects/tmf/data/changelog.csv`, `Projects/tmf/PROJECT.md`
- Người duyệt: seo-reviewer, ngày 2026-11-19

## Đối chiếu số liệu

Kết quả: **0 lỗi số liệu**. Mọi con số trong báo cáo truy được về tóm tắt hoặc file nguồn ghi bên dưới.

| Phần báo cáo (dòng) | Số trong báo cáo | Nguồn đối chiếu | Kết quả |
|---|---|---|---|
| Ghi chú cửa sổ (6) | 28/09 đến 25/10, 4 tuần; 14/09 đến 27/09, 2 tuần | Tóm tắt mục 1, 8 | Khớp |
| Tóm tắt dòng 1 (9) | 351,5 / 372,0 / -5,5%; 8.747 / 11.154 / -21,6%; 154 / 207 / -25,6%; revenue -26,1% | Tóm tắt mục 2 | Khớp |
| Tóm tắt dòng 2 (10) | -6,7 clicks/tuần; 6,5 → 8,8; +4,0 | Tóm tắt mục 3, 4 | Khớp |
| Tóm tắt dòng 3 (11) | 16/32 (50%) | Tóm tắt mục 6 | Khớp |
| Bảng KPI (16-23) | 8 dòng, toàn bộ giá trị và % | Tóm tắt mục 2 | Khớp. Đã tính lại: 1.406/4 = 351,5; 744/2 = 372,0; các % thay đổi đúng đến 0,1 |
| Top trang (32-38) | 7 dòng, clicks và vị trí | Tóm tắt mục 3 | Khớp |
| Top query (43-49) | 7 dòng | Tóm tắt mục 3 | Khớp |
| Rank (54-59) | volume, TB trước, TB nay, ghi chú tuần cuối | Tóm tắt mục 4 | Khớp. Đã tính lại TB từ 4 tuần (35/4 = 8,75; 52/4 = 13,0; 38/4 = 9,5; 46/4 = 11,5; 37/4 = 9,25; 62/4 = 15,5) |
| GA4 landing (66-73) | 8 dòng sessions và conv | Tóm tắt mục 5 | Khớp |
| Nhận xét GA4 (75) | +2,5/tuần; 741 → 366; 21 → 1 | Tóm tắt mục 3, 5 | Khớp |
| GEO (78-82) | 2026-10-20; 8 × 4 = 32; 16/32; 3/8, 4/8, 4/8, 5/8; 16, 12, 4 dòng; đối thủ 3, 3, 2, 2, 2, 2, 2 | Tóm tắt mục 6 | Khớp |
| Việc đã làm (85-87) | run 2026-11-13 và 2026-11-19; hose-cuffs đăng 2026-11-12 | RUN.md các run (`updated` đều là 2026-11-13 hoặc 2026-11-19), RUN.md `2026-11-13_collection_hypothesis-published` (`published_on: 2026-11-12`), `data/changelog.csv` | Khớp |
| Kế hoạch (94-100) | các số trích lại từ mục 2 đến 7; "7 đối thủ"; next_step seo-post-publish-check | Tóm tắt; RUN.md run collection | Khớp |
| KPI mục tiêu (102) | 30%, 6 tháng | PROJECT.md mục Mục tiêu và KPI, có nhãn [GIẢ ĐỊNH] | Khớp |

Ô cùng kỳ năm trước và GEO tháng trước ghi [CẦN SỐ LIỆU], đúng với tóm tắt mục 7.

## Điểm (thang 100)

Template review.md viết cho bài nội dung; với báo cáo, các nhóm được hiểu như sau: intent = báo cáo trả lời được "tháng này thế nào, làm gì tiếp"; brief = đúng template report.md và yêu cầu workflow; E-E-A-T và nguồn = số truy được; AI trích dẫn = rõ ràng, dễ đọc lại; compliance = luật dữ liệu giả định, không bịa.

| Nhóm | Tối đa | Điểm | Ghi chú |
|---|---|---|---|
| Đáp ứng intent | 25 | 20 | Nêu rõ độ lệch GSC và GA4. Nhận định "Hoses giảm nhiều nhất" chỉ đúng với GSC, bỏ qua số GA4 ngược chiều (xem P1) |
| Đúng brief | 20 | 19 | Đủ 6 phần của template report.md. Mục "Việc đã làm" lấy đúng từ RUN.md theo workflow |
| E-E-A-T và nguồn | 20 | 20 | 0 lỗi số liệu; mỗi bảng ghi số mục tóm tắt |
| Khả năng được AI trích dẫn | 20 | 16 | Bảng rõ. Bảng GA4 chọn lọc 8 trên 10 dòng mà không nói tiêu chí chọn |
| Văn phong và compliance | 15 | 14 | Có dòng "DỮ LIỆU GIẢ ĐỊNH - KHÔNG GIAO KHÁCH", không dùng số giả định như số thật, KPI ghi nhãn [GIẢ ĐỊNH]. Một chỗ diễn đạt dễ hiểu sai (P3) |
| **Tổng** | 100 | **89** | |

## Quyết định
**Đạt** (89, ngưỡng 80). PROJECT.md của tmf không đặt ngưỡng riêng.

Lưu ý: khách có `test_data: yes`, báo cáo không được gửi khách dù đạt. Nên sửa P1 trước khi người duyệt.

## Danh sách sửa
| Vị trí (trích đoạn) | Vấn đề | Mức P0 đến P3 | Cách sửa |
|---|---|---|---|
| Dòng 10: "Nhóm Hoses giảm nhiều nhất: collection high-pressure-solution-line-hoses -6,7 clicks/tuần" | Chỉ đúng trên GSC. Tóm tắt mục 5 cho thấy GA4 của chính collection này tăng (640 → 719 sessions, conv 11 → 21), hoses-accessories tăng (239 → 353), hose 100 feet tăng (174 → 730). Kết luận cả nhóm giảm là phiến diện, và dẫn tới ưu tiên "Cao" ở kế hoạch #2 | P1 | Ghi rõ "trên GSC" và nêu số GA4 ngược chiều; cân nhắc lại mức ưu tiên kế hoạch #2 hoặc gộp vào việc #1 (kiểm lệch GSC và GA4) |
| Dòng 63-73: bảng "GA4 landing organic, biến động sessions lớn nhất" | Bỏ 2 dòng của tóm tắt (hoses-accessories +114; high-pressure-solution-line-hoses +79), đúng là 2 dòng mâu thuẫn với nhận định Hoses giảm. Không nêu tiêu chí chọn | P2 | Đưa đủ 10 dòng của tóm tắt mục 5, hoặc ghi tiêu chí chọn (ví dụ: biến động trên 130 sessions) |
| Dòng 95: kế hoạch #2, lý do "-6,7 clicks/tuần; ... (mục 3, 4)" | Lý do chưa tính GA4 tăng của chính trang này (mục 5) | P2 | Thêm số GA4 vào cột lý do để người duyệt cân nhắc |
| Dòng 94: "GSC clicks -5,5%/tuần" | Dễ đọc thành giảm 5,5% mỗi tuần. Thực tế là trung bình/tuần giảm 5,5% so với tháng trước | P3 | Viết "GSC clicks trung bình/tuần -5,5%" |
| Dòng 32-38: bảng trang GSC | Không có trang chủ (-1,5) và sprayers (-1,3) trong tóm tắt mục 3; chấp nhận được vì là top, nhưng nên nói số dòng đã chọn | P3 | Thêm ghi chú "chọn 4 giảm và 3 tăng lớn nhất" |

## Tóm tắt
1. Đối chiếu toàn bộ số trong report.md với tóm tắt 2026-10, RUN.md và changelog: 0 lỗi số liệu, đã tính lại các trung bình và %.
2. Báo cáo đúng template, đủ [CẦN SỐ LIỆU] cho cùng kỳ năm trước và GEO tháng trước, giữ đúng nhãn dữ liệu giả định.
3. Điểm 89, quyết định đạt.
4. Lỗi chính (P1): nhận định "Hoses giảm nhiều nhất" dựa riêng GSC, bảng GA4 bỏ đúng 2 dòng hose tăng.
5. Nên sửa P1 và P2 trước khi Harry duyệt; báo cáo không gửi khách vì test_data: yes.
