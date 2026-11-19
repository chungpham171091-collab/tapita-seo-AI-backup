DỮ LIỆU GIẢ ĐỊNH - KHÔNG GIAO KHÁCH

# Tóm tắt dữ liệu báo cáo tháng: tmf 2026-10

> GIẢ ĐỊNH: số liệu lấy từ file export giả định trong `data/`. Khách có `test_data: yes`. Xóa cảnh báo này khi có dữ liệu thật.

- Khách: tmf
- Tháng báo cáo: 2026-10 (tháng trước: 2026-09; cùng kỳ năm trước: 2025-10)
- Số dòng đã đọc: GSC tổng ngày 3 file (31 + 30 + 31 ngày); GSC trang 3 file (20 dòng mỗi file); GSC query 3 file (25 dòng mỗi file); GA4 landing 3 file (20 + 20 + 18 dòng); rank 8 file tuần (4 file tháng 10, 4 file tháng 9, 14 từ khóa mỗi file); GEO 2 file (32 dòng mỗi file)
- Ngày tạo: 2026-11-19
- Run: `Projects/tmf/runs/2026-11-19_report_2026-10/`

## 1. Cửa sổ dữ liệu

| Nguồn | Tháng này (2026-10) | Tháng trước (2026-09) | Cùng kỳ năm trước (2025-10) | Ghi chú |
|---|---|---|---|---|
| GSC tổng ngày | `gsc/month_dates_2026-10.csv`, đủ 31 ngày (01/10 đến 31/10) | `gsc/month_dates_2026-09.csv`, đủ 30 ngày | `gsc/month_dates_2025-10.csv`, đủ 31 ngày | Đủ tháng, so trực tiếp được |
| GSC trang và query | `gsc/month_pages_2026-10.csv`, `gsc/month_queries_2026-10.csv` | cùng loại file tháng 09 | cùng loại file tháng 10/2025 | Chỉ là top trang và top query, xem mục 3 |
| GA4 landing (organic) | `ga4/landing_2026-10.csv` | `ga4/landing_2026-09.csv` | `ga4/landing_2025-10.csv` | Đủ tháng |
| Rank (trung bình tuần) | 4 file: `rank_2026-10-04`, `10-11`, `10-18`, `10-25` (phủ 28/09 đến 25/10) | 4 file: `rank_2026-09-06`, `09-13`, `09-20`, `09-27` (phủ 31/08 đến 27/09) | Không có | Cửa sổ lệch lịch tháng, xem mục 7 |
| GEO (citations) | `geo/citations_2026-10.csv` (ngày kiểm 20/10/2026) | `geo/citations_2026-09.csv` (ngày kiểm 20/09/2026) | Không có | Cỡ mẫu nhỏ, xem mục 6 |

## 2. KPI

### GSC (tổng từ `gsc/month_dates_*.csv`)

| Chỉ số | Tháng này 2026-10 | Tháng trước 2026-09 | Thay đổi so tháng trước | Cùng kỳ 2025-10 | Thay đổi so cùng kỳ |
|---|---|---|---|---|---|
| Clicks (tổng tháng) | 1.748 | 1.736 | +12 (+0,7%) | 1.073 | +675 (+62,9%) |
| Clicks trung bình/ngày | 56,4 | 57,9 | -2,6% | 34,6 | +62,9% |
| Impressions (tổng tháng) | 121.016 | 118.373 | +2.643 (+2,2%) | 75.026 | +45.990 (+61,3%) |
| Impressions trung bình/ngày | 3.903,7 | 3.945,8 | -1,1% | 2.420,2 | +61,3% |
| CTR (clicks / impressions) | 1,44% | 1,47% | -0,02 điểm % | 1,43% | +0,01 điểm % |
| Vị trí trung bình (có trọng số impressions từng ngày) | 11,55 | 11,48 | +0,07 (xấu hơn) | 12,29 | -0,74 (tốt hơn) |

CTR tính lại từ clicks và impressions; cột CTR trong export là phần trăm làm tròn. Vị trí trung bình là ước lượng từ các dòng ngày, không phải số GSC chính thức.

### GA4 (tổng các dòng trong `ga4/landing_*.csv`, organic)

| Chỉ số | Tháng này 2026-10 | Tháng trước 2026-09 | Thay đổi so tháng trước | Cùng kỳ 2025-10 | Thay đổi so cùng kỳ |
|---|---|---|---|---|---|
| Sessions | 1.980 | 1.999 | -19 (-1,0%) | 1.226 | +754 (+61,5%) |
| Active users | 1.692 | 1.693 | -0,1% | 1.021 | +671 (+65,7%) |
| Engaged sessions | [CẦN SỐ LIỆU] | [CẦN SỐ LIỆU] | - | [CẦN SỐ LIỆU] | - |
| Key events (conversions) | 22 | 18 | +4 (+22,2%) | 16 | +6 (+37,5%) |
| Total revenue (đơn vị theo export, export không ghi tiền tệ) | 6.551,94 | 4.529,67 | +2.022,27 (+44,6%) | 3.468,56 | +3.083,38 (+88,9%) |

Export GA4 không có cột engaged_sessions; chỉ có Active users và Key events. Tổng là tổng các dòng landing page trong export, không phải tổng toàn kênh.

## 3. Trang và query (GSC, clicks trong tháng)

Tổng clicks của top 20 trang trong `month_pages` bằng đúng tổng `month_dates` của cả ba tháng (1.748; 1.736; 1.073). Top 25 query thì thấp hơn: 1.593; 1.578; 1.008. Phần chênh là query Google ẩn, nên tổng tháng lấy từ `month_dates`.

### Trang giảm nhiều nhất so với tháng trước (`month_pages`)

| Trang | 2026-09 | 2026-10 | Thay đổi | Vị trí TB 09 → 10 |
|---|---|---|---|---|
| /collections/high-pressure-solution-line-hoses | 186 | 144 | -42 | 7,82 → 8,75 |
| /blogs/news/orbot-sprayborg-vs-orbot-vibe | 140 | 113 | -27 | 3,11 → 3,48 |
| /collections/carpet-cleaning-chemicals | 185 | 177 | -8 | 15,25 → 15,26 |
| /products/hydro-force-pro-solution-hose-100-feet | 41 | 36 | -5 | 12,26 → 11,96 |
| /collections/sprayers | 55 | 51 | -4 | 10,40 → 10,49 |

### Trang tăng nhiều nhất so với tháng trước (`month_pages`)

| Trang | 2026-09 | 2026-10 | Thay đổi | Vị trí TB 09 → 10 |
|---|---|---|---|---|
| / (trang chủ) | 427 | 466 | +39 | 1,19 → 1,19 |
| /collections/hoses-accessories | 73 | 87 | +14 | 10,02 → 10,10 |
| /products/hose-cuff-2-in-standard | 5 | 13 | +8 | 6,81 → 6,84 |
| /collections/wands-wand-parts | 190 | 196 | +6 | 12,42 → 12,45 |
| /products/tmf-revolution-wand-14-glide | 28 | 34 | +6 | 15,79 → 15,47 |
| /products/11001-hi-flow-ss-jets-for-carpet-cleaning-wands | 58 | 63 | +5 | 5,24 → 5,26 |

So với cùng kỳ 2025-10 (clicks): trang chủ 278 → 466 (+188); carpet-cleaning-chemicals 103 → 177 (+74); wands-wand-parts 130 → 196 (+66); carpet-cleaning-inline-sprayer 73 → 117 (+44).

### Query giảm nhiều nhất so với tháng trước (`month_queries`)

| Query | 2026-09 | 2026-10 | Thay đổi | Vị trí TB 09 → 10 |
|---|---|---|---|---|
| orbot sprayborg vs orbot vibe | 88 | 70 | -18 | 2,40 → 2,65 |
| truck mount solution hose | 130 | 113 | -17 | 8,98 → 9,44 |
| carpet cleaning solution hose | 75 | 61 | -14 | 8,91 → 9,39 |
| hydro force inline sprayer | 48 | 42 | -6 | 1,83 → 1,80 |
| carpet cleaning chemicals | 117 | 112 | -5 | 15,02 → 15,03 |
| orbot sprayborg | 39 | 35 | -4 | 3,76 → 4,22 |

### Query tăng nhiều nhất so với tháng trước (`month_queries`)

| Query | 2026-09 | 2026-10 | Thay đổi | Vị trí TB 09 → 10 |
|---|---|---|---|---|
| truckmountforums | 254 | 293 | +39 | 1,08 → 1,09 |
| carpet cleaning hose | 70 | 78 | +8 | 9,45 → 9,52 |
| 2 inch hose cuff | 5 | 13 | +8 | 6,44 → 6,45 |
| carpet cleaning jets | 34 | 40 | +6 | 5,50 → 5,52 |
| inline sprayer carpet cleaning | 62 | 68 | +6 | 3,60 → 3,67 |
| carpet cleaning wand | 161 | 166 | +5 | 13,14 → 13,06 |

So với cùng kỳ 2025-10 (clicks): truckmountforums 168 → 293 (+125); carpet cleaning wand 115 → 166 (+51); carpet cleaning chemicals 67 → 112 (+45); truck mount solution hose 77 → 113 (+36).

## 4. Rank từ khóa chính (`rank/`, trung bình 4 tuần; số nhỏ là tốt hơn)

Cùng kỳ năm trước: không có file rank 2025 → [CẦN SỐ LIỆU]. Volume lấy từ file rank, không đổi trong kỳ.

| Từ khóa | Volume | TB 2026-09 | TB 2026-10 | Thay đổi | Các tuần tháng 10 (04/10, 11/10, 18/10, 25/10) |
|---|---|---|---|---|---|
| truck mount solution hose | 480 | 8,00 | 8,50 | +0,50 | 8, 8, 8, 10 |
| carpet cleaning hose | 1.300 | 9,50 | 9,75 | +0,25 | 10, 10, 9, 10 |
| carpet cleaning vacuum hose | 880 | 10,75 | 11,00 | +0,25 | 11, 11, 11, 11 |
| vacuum hose cuff | 210 | 5,00 | 5,00 | 0 | 5, 5, 5, 5 |
| carpet cleaning wand | 2.400 | 12,00 | 12,50 | +0,50 | 12, 12, 13, 13 |
| carpet wand glide | 320 | 7,00 | 7,00 | 0 | 7, 7, 7, 7 |
| carpet cleaning jets | 390 | 5,50 | 5,75 | +0,25 | 6, 5, 6, 6 |
| carpet cleaning wand valve | 170 | 8,25 | 8,25 | 0 | 9, 8, 7, 9 |
| carpet cleaning sprayer | 1.000 | 9,75 | 10,00 | +0,25 | 10, 10, 10, 10 |
| inline sprayer carpet cleaning | 390 | 4,00 | 4,00 | 0 | 4, 4, 4, 4 |
| carpet cleaning chemicals | 3.600 | 15,00 | 15,00 | 0 | 15, 16, 15, 14 |
| truck mount carpet cleaning machine | 1.900 | 13,25 | 13,75 | +0,50 | 14, 14, 14, 13 |
| quick connect carpet cleaning | 210 | 8,25 | 8,25 | 0 | 9, 8, 8, 8 |
| solution hose 100 ft | 110 | 4,00 | 4,00 | 0 | 4, 4, 4, 4 |

Không từ khóa nào cải thiện. Bảy từ khóa xấu đi 0,25 đến 0,50 vị trí; bảy từ khóa giữ nguyên. Cửa sổ 4 tuần.

## 5. GA4 landing (organic): biến động lớn nhất

| Landing page | Sessions 2026-09 | Sessions 2026-10 | Thay đổi |
|---|---|---|---|
| /collections/high-pressure-solution-line-hoses | 204 | 158 | -46 |
| /blogs/news/orbot-sprayborg-vs-orbot-vibe | 170 | 132 | -38 |
| /products/carpet-cleaning-inline-sprayer | 125 | 142 | +17 |
| / (trang chủ) | 493 | 509 | +16 |
| /collections/hoses-accessories | 83 | 94 | +11 |
| /products/11001-hi-flow-ss-jets-for-carpet-cleaning-wands | 63 | 74 | +11 |

So với cùng kỳ 2025-10 (sessions): trang chủ 308 → 509 (+201); carpet-cleaning-chemicals 124 → 215 (+91); wands-wand-parts 150 → 212 (+62); carpet-cleaning-inline-sprayer 81 → 142 (+61).

Key events theo trang: trang chủ 4 → 6; orbot blog 1 → 3; collections/high-pressure-solution-line-hoses 3 → 1; collections/wands-wand-parts 3 → 3.

## 6. GEO (`geo/`, 8 prompt × 4 engine mỗi tháng)

Ngày kiểm: 2026-09-20 (tháng trước), 2026-10-20 (tháng này). Số dòng: 32 mỗi tháng.

- Tỷ lệ prompt có nhắc brand: 13/32 (40,6%) tháng này; 7/32 (21,9%) tháng trước.
- Theo engine, tháng này / tháng trước: ChatGPT 5/8 (2/8); Perplexity 2/8 (2/8); Gemini 2/8 (1/8); AI Overviews 4/8 (2/8).
- URL được trích, tháng này (13 dòng): collection wands-wand-parts 7; trang chủ 6. Tháng trước (7 dòng): trang chủ 4; wands-wand-parts 3.
- Đối thủ ghi ở cột competitor_cited, tháng này (20 dòng): magicwandcompany.com 6; interlinksupply.com 5; clean.direct 3; jondon.com 3; dultmeier.com 2; shopexcelsupplies.com 1. Tháng trước (21 dòng): interlinksupply.com 5; jondon.com 4; shopexcelsupplies.com 3; shopcleanersdepot.ecwid.com 3; clean.direct 3; magicwandcompany.com 2; dultmeier.com 1.
- Cùng kỳ 2025-10: không có file citations → [CẦN SỐ LIỆU].

## 7. Nguồn thiếu, tuần thiếu và giới hạn

- **Cùng kỳ năm trước**: không có rank 2025 và không có GEO 2025. Các ô tương ứng ghi [CẦN SỐ LIỆU]. GSC và GA4 có đủ 2025-10.
- **GA4 engaged sessions**: export không có cột này. Ô tương ứng để [CẦN SỐ LIỆU]; không thay bằng cột khác.
- **GA4 total revenue**: export không ghi tiền tệ. Giữ nguyên số theo export.
- **Rank, cửa sổ lệch tháng**: file tuần theo tên là ngày cuối tuần. Tháng 10 có 4 file (28/09 đến 25/10). Tuần 26/10 đến 01/11 (`rank_2026-11-01.csv`) thuộc tháng 11 theo tên file nên không tính, nên 26/10 đến 31/10 không có số rank. Tháng 09 có 4 file (31/08 đến 27/09).
- **GSC query**: tổng query thấp hơn tổng tháng do Google ẩn một phần query; tổng tháng lấy từ `month_dates`.
- **GEO**: 8 prompt và một ngày kiểm mỗi tháng, cỡ mẫu nhỏ; không đủ để kết luận xu hướng.
- **Không dùng**: file tuần GSC (`gsc/pages_*`, `gsc/queries_*`, `gsc/query_page_*`) vì đã có export cả tháng; `_summary/latest_gsc.md`.

## 8. Lưu ý phương pháp

- Tổng GSC lấy từ `month_dates` (đủ ngày). Tháng 09 có 30 ngày nên so thêm trung bình/ngày.
- Vị trí trung bình tháng: trung bình có trọng số impressions của từng ngày.
- Rank: trung bình đơn giản của các file tuần trong tháng; mỗi từ khóa đủ 4 tuần ở cả hai tháng.
- Bản tóm tắt trước của kỳ này (lấy từ file tuần) đã được thay bằng bản này.
