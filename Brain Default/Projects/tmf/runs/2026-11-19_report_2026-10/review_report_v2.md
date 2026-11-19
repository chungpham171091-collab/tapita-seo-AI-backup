DỮ LIỆU GIẢ ĐỊNH - KHÔNG GIAO KHÁCH

# REVIEW: report.md (tmf, báo cáo tháng 2026-10, bản dựng lại từ export cả tháng)

- File duyệt: `Projects/tmf/runs/2026-11-19_report_2026-10/report.md` (124 dòng, ghi lúc 21:35, đọc toàn bộ)
- File đối chiếu: `Projects/tmf/data/_summary/2026-10_report-data.md` (tóm tắt, 164 dòng), RUN.md các run trong `Projects/tmf/runs/`, `Projects/tmf/data/changelog.csv`, `Projects/tmf/PROJECT.md`
- Người duyệt: seo-reviewer, ngày 2026-11-19
- Ghi chú: `review_report.md` cùng thư mục (21:16) là bản duyệt báo cáo CŨ (dựng từ file tuần), không còn đúng với report.md hiện tại. Giữ nguyên theo luật không ghi đè; dùng file này.

## Đối chiếu số liệu

Kết quả: **0 lỗi số liệu**. Mọi con số trong báo cáo truy được về tóm tắt hoặc file nguồn ghi bên dưới.

| Phần báo cáo (dòng) | Số trong báo cáo | Nguồn đối chiếu | Kết quả |
|---|---|---|---|
| Ghi chú kỳ (6) | 3 kỳ 2026-10, 2026-09, 2025-10; rank 4 file tuần, 28/09 đến 25/10 | Tóm tắt mục 1 | Khớp |
| Tóm tắt dòng 1 (9) | 1.748 (+0,7%); 1.980 (-1,0%); conv 18 → 22; revenue +44,6%; cùng kỳ +62,9% và +61,5% | Tóm tắt mục 2 | Khớp |
| Tóm tắt dòng 2 (10) | 186 → 144; 7,82 → 8,75; 204 → 158; 7/14 tụt 0,25 đến 0,50 | Tóm tắt mục 3, 4, 5 | Khớp (xem P3 về cách đặt câu) |
| Tóm tắt dòng 3 (11) | 13/32; 7/32; 8 prompt, 1 ngày; magicwandcompany.com 6 | Tóm tắt mục 6 | Khớp |
| Bảng KPI (16-26) | 11 dòng, đủ 3 kỳ và % | Tóm tắt mục 2, 4, 7 | Khớp. Đã tính lại: 1.748/31 = 56,4; 1.736/30 = 57,9; 1.073/31 = 34,6; 56,4/57,9 = -2,6%; 1.748/121.016 = 1,44%; 6.551,94/4.529,67 = +44,6%; 22/16 = +37,5% |
| Ghi chú KPI (28) | -2,6%/ngày, +0,7% tổng tháng | Tóm tắt mục 2, 8 | Khớp |
| Top trang (37-47) | 11 dòng | Tóm tắt mục 3 | Khớp, đủ 5 giảm và 6 tăng như dòng 33 nói |
| Cùng kỳ trang (49) | 278 → 466; 103 → 177; 130 → 196; 73 → 117 | Tóm tắt mục 3 | Khớp |
| Top query (54-65) | 12 dòng | Tóm tắt mục 3 | Khớp, đủ 6 giảm và 6 tăng |
| Cùng kỳ query (67) | 168 → 293; 115 → 166; 67 → 112; 77 → 113 | Tóm tắt mục 3 | Khớp |
| Rank (70-82) | 7 từ khóa tụt, volume, TB, các tuần; chemicals 3.600 ở 15,00 | Tóm tắt mục 4 | Khớp. Đã đếm lại: 7 dòng thay đổi dương, 7 dòng 0; tính lại TB 10/2026 (8+8+8+10)/4 = 8,50; (12+12+13+13)/4 = 12,50; (14+14+14+13)/4 = 13,75 |
| GA4 landing (89-94) | 6 dòng | Tóm tắt mục 5 | Khớp, đủ 6 dòng như dòng 85 nói |
| Key events (96) | 4 → 6; 1 → 3; 3 → 1; 3 → 3 | Tóm tắt mục 5 | Khớp |
| GEO (99-104) | 2026-10-20 / 2026-09-20; 32 dòng; 13/32 (40,6%), 7/32 (21,9%); 5/8, 2/8, 2/8, 4/8 và tháng trước; URL 7 + 6, 4 + 3; đối thủ 20 dòng | Tóm tắt mục 6 | Khớp (xem P3 về dòng bị bỏ) |
| Việc đã làm (107-109) | không run nào `updated` tháng 10; 4 run 2026-11-13 là giả định; hose-cuffs đăng 2026-11-12 | RUN.md 5 run (`updated` 2026-11-13 hoặc 2026-11-19, 4 run 11-13 có ghi giả định); RUN.md `2026-11-13_collection_hypothesis-published` (`published_on: 2026-11-12`); `data/changelog.csv` | Khớp |
| Kế hoạch (116-122) | số trích lại từ mục 3 đến 7; next_step seo-post-publish-check | Tóm tắt; RUN.md run collection | Khớp |
| KPI mục tiêu (124) | 30%, 6 tháng, [GIẢ ĐỊNH] | PROJECT.md mục Mục tiêu và KPI | Khớp |

Đã kiểm thêm bỏ dòng có chọn lọc: bảng trang, query, GA4 đều đưa đủ dòng của tóm tắt; bảng rank đưa đủ 7 từ khóa tụt và nói rõ 7 từ khóa còn lại giữ nguyên. Lỗi P1 và P2 của bản duyệt trước (bảng GA4 bỏ dòng hose tăng) không còn.

## Điểm (thang 100)

Template review.md viết cho bài nội dung; với báo cáo, các nhóm hiểu là: intent = trả lời được "tháng này thế nào, làm gì tiếp"; brief = đúng template report.md và yêu cầu workflow; E-E-A-T và nguồn = số truy được; AI trích dẫn = rõ, dễ đọc lại; compliance = luật dữ liệu giả định, không bịa.

| Nhóm | Tối đa | Điểm | Ghi chú |
|---|---|---|---|
| Đáp ứng intent | 25 | 23 | Nêu đúng điểm chính (đi ngang so tháng trước, mạnh so cùng kỳ, collection solution hose giảm hai nguồn). Câu "Điểm yếu là nhóm Hoses" rộng hơn số liệu (P3) |
| Đúng brief | 20 | 20 | Đủ 6 phần template; việc đã làm lấy đúng từ RUN.md; nguồn thiếu ghi [CẦN SỐ LIỆU] |
| E-E-A-T và nguồn | 20 | 20 | 0 lỗi số liệu; mọi bảng ghi số mục tóm tắt; nêu rõ vị trí TB là ước lượng, tổng GA4 không phải toàn kênh |
| Khả năng được AI trích dẫn | 20 | 18 | Bảng đủ dòng, có ghi tiêu chí chọn. Một mệnh đề rank đặt sai ngữ cảnh (P3) |
| Văn phong và compliance | 15 | 14 | Dòng đầu "DỮ LIỆU GIẢ ĐỊNH - KHÔNG GIAO KHÁCH", KPI gắn [GIẢ ĐỊNH], run giả định được nêu rõ. GEO bỏ một dòng đối thủ tháng trước (P3) |
| **Tổng** | 100 | **95** | |

## Quyết định
**Đạt** (95, ngưỡng 80). PROJECT.md của tmf không đặt ngưỡng riêng.

Lưu ý: khách có `test_data: yes`, báo cáo không gửi khách dù đạt. Các mục dưới đây là P3, sửa hay không do Harry quyết.

## Danh sách sửa
| Vị trí (trích đoạn) | Vấn đề | Mức P0 đến P3 | Cách sửa |
|---|---|---|---|
| Dòng 10: "Điểm yếu là nhóm Hoses. Collection high-pressure-solution-line-hoses giảm..." | Chỉ một collection giảm; các trang hose khác tăng (hoses-accessories GSC 73 → 87, GA4 83 → 94; hose-cuff-2-in-standard 5 → 13; query "carpet cleaning hose" 70 → 78, tóm tắt mục 3, 5). Cả nhóm vẫn giảm ròng trên GSC (4 trang hose trong bảng: 305 → 280) nhưng câu đọc như cả nhóm đi xuống | P3 | Viết "Điểm yếu là collection solution hose (nhóm Hoses)" hoặc thêm một vế nêu các trang hose đang tăng |
| Dòng 10: "...trên rank tracker không từ khóa nào lên hạng, 7/14 từ khóa tụt 0,25 đến 0,50 bậc" | Số 7/14 là toàn bộ bộ từ khóa, nhưng nằm trong câu về Hoses nên dễ đọc thành 7 từ khóa hose tụt. Thực tế 3 trên 6 từ khóa hose tụt (tóm tắt mục 4) | P3 | Tách thành câu riêng hoặc ghi "toàn bộ 14 từ khóa: không cái nào lên, 7 tụt; nhóm hose 3/6 tụt" |
| Dòng 102: "Đối thủ được trích (20 dòng): ... shopexcelsupplies.com 1 (3)" | Bỏ shopcleanersdepot.ecwid.com (tháng trước 3, tháng này 0) và tổng tháng trước 21 dòng (tóm tắt mục 6). Không sai số, nhưng thiếu một biến động | P3 | Thêm "shopcleanersdepot.ecwid.com 0 (3); tháng trước 21 dòng" |

## Tóm tắt
1. Đối chiếu từng số trong report.md với tóm tắt 2026-10, RUN.md và changelog: 0 lỗi số liệu; đã tính lại trung bình/ngày, CTR, %, trung bình rank.
2. Bảng top đưa đủ dòng của tóm tắt, không bỏ dòng chọn lọc; lỗi P1/P2 của bản duyệt trước đã hết.
3. Điểm 95, quyết định đạt.
4. Còn 3 điểm P3 về diễn đạt: "nhóm Hoses" rộng hơn số liệu, mệnh đề rank 7/14 đặt sai ngữ cảnh, GEO thiếu một dòng đối thủ.
5. Không gửi khách vì test_data: yes; `review_report.md` cũ là bản duyệt báo cáo trước, dùng file này.
