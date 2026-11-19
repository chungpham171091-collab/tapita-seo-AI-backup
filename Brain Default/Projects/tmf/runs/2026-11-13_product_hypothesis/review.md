DỮ LIỆU GIẢ ĐỊNH - KHÔNG GIAO KHÁCH

# Review: tmf - product (hose) - meta_table.csv

- Khách: tmf (en-US, google.com). Skill product: harry-optimization. Compliance: PROJECT.md không có skill, kiểm theo mục Từ cấm (chỉ có phần [GIẢ ĐỊNH]).
- Bài: Projects/tmf/runs/2026-11-13_product_hypothesis/meta_table.csv (4 sản phẩm). Đã đọc toàn bộ từ đầu, đối chiếu products.csv, product_analysis.md, ahrefs_volume.csv, product_keywords_sv.csv, deliverables/keyword_mapping_us.csv, data/inputs/site_urls.csv.
- Lưu ý: meta_table.xlsx có trong run nhưng không audit (chỉ audit .csv theo đầu vào; chưa so khớp hai file).
- Chưa có review.md trước đó nên ghi review.md.

## 1. Nguồn
- Bài không có link ngoài, số liệu thống kê hay trích dẫn nghiên cứu. harry-reference-check: không áp dụng (N/A).
- Link nội bộ: không có link trong nội dung. 4 URL sản phẩm đều có trong site_urls.csv (dòng 5, 187, 191, 195). Đạt.
- Các fact lấy từ listing (3000 PSI at 250F, 100/150 ft, 1/4 inch ID, brass quick connects) khớp products.csv. Chính sách đổi trả 30 ngày khớp PROJECT.md. Hotline 1-800-949-7726 khớp PROJECT.md.

## 2. E-E-A-T (QRG, tapita-eeat-check, locale en-US)
Đây là bản nháp (không fetch được trang live, không xét layout/quảng cáo/reputation; không có nguồn độc lập nào được tra, ghi "Cần kiểm tra thêm").
- YMYL: không. Loại trang: product (ecommerce). Mục tiêu: bán.
- Lowest: không có trigger. Không claim sai/lừa; nội dung trung thực, gắn nhãn thiếu dữ liệu.
- Page Quality ước tính: Hose 1-3 Low+/Medium-; Hose 4 Low (spec chỉ lấy từ tên sản phẩm, không xác minh).
- Needs Met (truy vấn chính từng sản phẩm): Moderately Meets. Trang trả lời được "là gì, dài bao nhiêu, PSI", nhưng thiếu tương thích, đường kính (Hose 1), nhà sản xuất, vật liệu.
- Experience: không có review thật, ảnh thật, kinh nghiệm dùng. Expertise: thông số rất ít. Authoritativeness: manufacturer trống ở cả 4. Trust: tốt (không overclaim, có chính sách và hotline).

## 3. Compliance
Không có từ/claim cấm trong danh sách [GIẢ ĐỊNH] (guaranteed, best in the industry, never fails, lifetime, y tế/diệt khuẩn, so sánh đối thủ, năm thành lập): không gặp. Skill compliance: PROJECT.md để trống.

## 4. Quy tắc skill harry-optimization (đếm thật)
| Sản phẩm | Meta title | Meta desc | Từ khóa (tổng; 2/3/4 từ) | Từ khóa chính trong content |
|---|---|---|---|---|
| Hi-Flo 2 Supra Flex | 51 (40-60 đạt) | 132 (120-150 đạt) | 10; 1/3/6 | "high pressure solution hose" có, nguyên cụm |
| Hydro-Force 50 ft | 57 đạt | 130 đạt | 9; 1/0/8 | "solution hose 50 ft" có |
| Hydro-Force 100 ft | 53 đạt | 128 đạt | 9; 1/1/7 | "hydro force hose": KHÔNG nguyên cụm (viết "Hydro-Force hose") |
| Super Truckmount Vacuum | 54 đạt | 131 đạt | 8; 1/1/6 | "truck mount vacuum hose" có (title viết "Truckmount") |
(Số từ khóa tính cả dòng chính; các dòng đã bỏ ghi chú "(SV 0)".)
- Cấu trúc nội dung: có đủ các section áp dụng được ([1][2][3][8][9][10][11][12][15]); bảng thông tin ≥8 dòng đạt; FAQ 8 câu mỗi bài đạt; không có claim sức khỏe.
- Cột Note chỉ hàng đầu, các cột meta/content chỉ hàng đầu: đạt.

## 5. Nhãn còn sót
- [CẦN XÁC NHẬN] còn nhiều trong cả 4 bài (xem lỗi 5 và 10 bên dưới). Không có [CẦN NGUỒN], [CẦN SỐ LIỆU], SUBSTANTIATION NEEDED.

## Danh sách lỗi

### P1
1. **Vị trí:** cột Keywords, cả 4 sản phẩm. **Vấn đề:** số từ khóa 8-10 so với 22-33 yêu cầu; dải 2 từ chỉ 1 (cần 2-3); dải 3 từ 0-3 (cần 10-15); dải 4 từ 6-8 (cần 10-15). Skill coi đây là lỗi cứng (validate.py không qua). **Bằng chứng:** đếm từ meta_table.csv, ví dụ Hose 2 chỉ có 9 dòng, 0 từ khóa 3 từ. **Sửa:** bổ sung từ khóa có cơ sở (tên sản phẩm trước, rồi nội dung) hoặc ghi rõ trong Note lý do dưới ngưỡng và để người duyệt chấp nhận; chạy scripts/validate.py.
2. **Vị trí:** Hose 4, mục [2]: "The details here come from the product name only, so material, rating and cuff type are marked for confirmation." **Vấn đề:** ghi chú nội bộ nằm trong nội dung khách. **Sửa:** xóa câu; đưa ý này vào cột Note.
3. **Vị trí:** Hose 4 (Super Truckmount Vacuum Hose 2 x 50 ft Blue). **Vấn đề:** toàn bộ spec lấy từ tên sản phẩm; sản phẩm không có trong products.csv/product_analysis.md; trang bị 429 (Note ghi rõ). Chưa có mô tả listing để xác minh; 5 dòng spec để [CẦN XÁC NHẬN]. **Sửa:** người export mô tả listing (products.csv) hoặc fetch giãn request rồi viết lại; chưa giao.
4. **Vị trí:** dòng đầu meta_table.csv. **Vấn đề:** khách có test_data: yes nhưng file không có dòng đầu "DỮ LIỆU GIẢ ĐỊNH - KHÔNG GIAO KHÁCH" (SEO-OPS mục 5). Do là CSV, nên đặt dòng này vào Note hoặc đổi tên/đánh dấu ở RUN.md, không chèn vào dòng tiêu đề cột. **Sửa:** ghi trong cột Note hàng đầu và RUN.md.
5. **Vị trí:** nội dung công khai, cả 4: FAQ và Important notes ("No temperature rating is listed. [CẦN XÁC NHẬN] before use with hot solution", "Compatibility is not listed. [CẦN XÁC NHẬN] Call TMF..."); mục [15] alt text "– [mô tả ảnh thật, CẦN XÁC NHẬN] | TMF Store" (có tiếng Việt trong content en-US). **Vấn đề:** nhãn và tiếng Việt nằm trong câu văn khách thấy; alt text chưa dùng được. **Sửa:** viết lại câu thành "TMF does not list X; call 1-800-949-7726" không có nhãn; viết alt text tiếng Anh từ ảnh thật hoặc để trống chờ ảnh.

### P2
6. **Vị trí:** Hose 2 meta desc: "...3000 PSI rating for carpet cleaning setups." **Vấn đề:** listing (products.csv) không nêu carpet cleaning; skill cấm use case không nêu. **Sửa:** bỏ hoặc dẫn từ collection/trang mà TMF nêu (tầng C/D).
7. **Vị trí:** Hose 3, từ khóa chính "hydro force hose" vs title/desc/content "Hydro-Force". **Vấn đề:** cụm chính không xuất hiện nguyên vẹn (gạch nối). Đồng thời mapping hiện hành gán main "solution hose 100 ft" (keyword_mapping_us.csv dòng 15); Note đã nói lý do nhưng cần người chọn. **Sửa:** quyết định main; nếu giữ, dùng "Hydro Force hose" ít nhất một lần.
8. **Vị trí:** Hose 4 main "truck mount vacuum hose" vs mapping "carpet cleaning vacuum hose" (880, dòng 4). **Vấn đề:** lệch mapping, từ khóa chính 880 chỉ ở vị trí secondary. Note đã báo "confirm which main". **Sửa:** người chốt.
9. **Vị trí:** RUN.md "4 sản phẩm hose" và products.csv (Hi-Flo, Hydro 50, Hydro 100, Parker Parflex Blue 50). **Vấn đề:** bảng meta thay Parker Parflex bằng Super Truckmount Vacuum; Parker Parflex chưa được làm. **Sửa:** xác nhận bộ 4 sản phẩm hoặc bổ sung Parker Parflex.
10. **Vị trí:** bảng [10] của cả 4 (Manufacturer, Materials, Inner diameter (Hose 1), Temperature rating (Hose 2-3...)) và mục [9] Use and care chỉ là placeholder. **Vấn đề:** thiếu thông tin nghiêm trọng cho E-E-A-T (Expertise/Authoritativeness), mục hướng dẫn rỗng. **Sửa:** lấy dữ liệu từ khách (PROJECT.md đã ghi hãng sản xuất [CẦN XÁC NHẬN]); không đoán từ tên hãng.
11. **Vị trí:** FAQ/[11] lặp gần như giống nhau ở cả 4 (câu hỏi return policy, "Will it fit", "Who manufactures"). **Vấn đề:** nội dung mẫu lặp, ít giá trị riêng; rủi ro thin/duplicate giữa các biến thể. **Sửa:** thay bằng câu hỏi riêng từng sản phẩm khi có dữ liệu (PAA), bỏ câu chỉ trả lời "[CẦN XÁC NHẬN]".
12. **Vị trí:** Experience (cả 4). **Vấn đề:** không có review, ảnh thật; trang live Hi-Flo 1 chưa kiểm. **Sửa:** dùng đánh giá thật của trang nếu có; không bịa.

### P3
13. Cột Keywords còn chú thích "(SV 0)" trong ô từ khóa (vd "supra flex hose (SV 0)"). Xóa khi giao.
14. Hose 4 meta title viết "Truckmount", từ khóa chính "truck mount" (hai chữ); cân nhắc đồng nhất (title phải là tên sản phẩm, nên cho vào desc là đủ).
15. "backed by TMF phone support", "with TMF support" (Hose 1, meta desc Hose 4): hỗ trợ điện thoại có (hotline) nhưng giờ hỗ trợ chưa xác minh; meta desc Hose 4 thiếu móc thúc đẩy mua. Sửa wording hoặc bỏ.
16. Mục [8] có nhóm đối tượng suy ra ("adding a second line" Hose 2). Giữ trong phạm vi listing.
17. Mapping chưa có dòng cho Hose 1 và Hose 2 (grep keyword_mapping_us.csv): không đối chiếu được từ khóa chính. Cần kiểm tra thêm.

## Verdict
KHÔNG ĐẠT (còn P1=5). Điều kiện đạt: sửa lỗi 1-5 (đặc biệt Hose 4 có listing thật), rồi audit lại.

Tóm tắt:
- 3 bài Hose 1-3 chính xác với listing, meta đúng độ dài, không claim cấm.
- Số từ khóa thiếu xa so với chuẩn skill ở cả 4 bài.
- Hose 4 chưa có dữ liệu listing, còn câu ghi chú nội bộ trong nội dung.
- Nhãn [CẦN XÁC NHẬN] và alt text tiếng Việt chưa dùng được cho khách.
- Dữ liệu giả định: không giao khách.

---

## Kiểm lại (audit bản sửa meta_table_v2.csv, 2026-11-20)

Đã đọc lại toàn bộ meta_table_v2.csv từ đầu (4 sản phẩm). Đối chiếu PROJECT.md (đổi trả 30 ngày, phí nhập lại kho, hotline dòng 50-55) và products.csv (không có Hose 4). Bản gốc meta_table.csv không đổi, không audit lại.

### Kiểm từng lỗi P1 cũ
| # | Trạng thái | Bằng chứng |
|---|---|---|
| 1 | **CÒN** (P1) | Số cụm từ khóa: Hose 1 = 9, Hose 2 = 9, Hose 3 = 9, Hose 4 = 7 (đếm dòng cột Keywords, kể cả dòng "(SV 0)"), vẫn dưới 22-33. Note ghi lý do (export chỉ có từng ấy cụm) nên không bịa là đúng, nhưng chưa được người duyệt chấp nhận. Cần: người chấp nhận ngoại lệ hoặc export thêm từ khóa. |
| 2 | Đã sửa | Câu ghi chú nội bộ ở Hose 4 [2] đã thay bằng "Material, rating and cuff type are not listed on the product page." Không còn câu nội bộ. |
| 3 | **CÒN** (P1) | Hose 4 vẫn chỉ có spec từ tên sản phẩm (mọi dòng bảng ghi "(per name)"), products.csv không có sản phẩm này (grep 0 kết quả). Nhãn "per the product name" làm rõ nguồn nhưng không xác minh được. Note ghi "chưa giao". Cần mô tả listing thật. |
| 4 | Đã sửa | Note hàng đầu của cả 4 sản phẩm hiện có "DỮ LIỆU GIẢ ĐỊNH - KHÔNG GIAO KHÁCH" (hàng Hose 1 bắt đầu bằng cụm này; review.md cũng có dòng đầu). Đặt tại Note cho Hose 1; Hose 2-4 không lặp (chấp nhận được vì Note chỉ ở hàng đầu mỗi sản phẩm, nhưng RUN.md cần ghi, xem P3 bên dưới). |
| 5 | Đã sửa | Không còn "[CẦN XÁC NHẬN]" hay tiếng Việt trong content (grep). Câu viết lại thành "Not listed. Call TMF at 1-800-949-7726". Alt text là tiếng Anh, dùng tên sản phẩm (xem P3 mới: alt text chưa mô tả ảnh). |

### Lỗi mới / còn sót
**P1**
- Không có lỗi P1 mới.

**P2**
- Hose 2, meta desc: "...3000 PSI rating for carpet cleaning setups." vẫn còn (lỗi 6 cũ chưa sửa). products.csv không nêu carpet cleaning; use case ngoài listing. Sửa: bỏ cụm này.
- Hose 3: từ khóa chính "hydro force hose" vẫn không xuất hiện nguyên cụm (title/H1 viết "Hydro-Force"; desc "Hydro-Force hose"). Lỗi 7 cũ chưa sửa. Sửa: dùng "Hydro Force hose" một lần, hoặc người chốt main.
- Hose 4: main "truck mount vacuum hose" vs mapping "carpet cleaning vacuum hose" (880); Note đã báo, chờ người chốt (lỗi 8). Bộ 4 sản phẩm thay Parker Parflex (lỗi 9) chưa có quyết định của người.
- Manufacturer/Materials/Temperature đều "Not listed" ở cả 4 bài; Use and care chỉ là "call TMF". E-E-A-T mỏng, nhưng trung thực, không claim sai (lỗi 10-12 cũ, nay không còn nhãn nội bộ).

**P3**
- Mới: FAQ Hose 2 và Hose 3 lặp "Not listed. Not listed. Call TMF at 1-800-949-7726." (câu hỏi temperature rating). Xóa một "Not listed."
- Còn: "(SV 0)" trong ô từ khóa (Hose 1: supra flex hose; Hose 2-4 tương tự). Xóa khi giao.
- Còn: "TMF phone support"/"with TMF support": giờ hỗ trợ chưa xác minh (lỗi 15).
- Alt text chỉ lặp tên sản phẩm + "| TMF Store", chưa mô tả ảnh thật (chưa có ảnh).
- Còn: Hose 4 title "Truckmount" vs từ khóa "truck mount" (lỗi 14).
- Hose 2-3 bảng có "Brand on listing | Hydro-Force (in product name)": suy từ tên, ghi rõ nguồn, chấp nhận.

### Quét khẳng định, số liệu, nguồn mới
- Không có số liệu, nguồn, link ngoài hay trích dẫn mới. harry-reference-check: N/A.
- Số liệu spec (3000 PSI at 250F, 100/150 ft, 1/4 inch ID, brass quick connects, 50/100 ft) giữ nguyên, khớp products.csv đã đối chiếu ở lượt trước (không đổi).
- Chính sách đổi trả "30 days... unused items in original condition ... restocking fees": khớp PROJECT.md dòng 55 (đọc lại lượt này). Hotline 1-800-949-7726 khớp PROJECT.md dòng 50.
- Claim mới: "Flexible (per listing)" (Hose 1) và "Flexible hose built for truck mount solution lines": products.csv có mô tả "Flexible high pressure solution..." nên chấp nhận. "Hose 4: Made for truck mount vacuum lines, per the product name": suy từ tên, đã gắn nhãn.
- Không có từ cấm (guaranteed, best, lifetime, y tế, so sánh đối thủ). Không có claim sức khỏe.

### Số đo lại (meta)
Title/desc không đổi so với bản đầu, vẫn đạt độ dài (title 51/57/53/54; desc 132/130/128/131 theo review ban đầu; nội dung title/desc v2 trùng bản đầu).

## Verdict (Kiểm lại)
**KHÔNG ĐẠT.** Còn P1 = 2 (lỗi 1: số từ khóa dưới ngưỡng; lỗi 3: Hose 4 thiếu dữ liệu listing). Lỗi 2, 4, 5 đã sửa. Còn 3 mục P2 chưa sửa (Hose 2 "carpet cleaning setups", Hose 3 cụm chính, chốt main/bộ sản phẩm), P3 nhỏ.

Tóm tắt:
- Lỗi 2, 4, 5 xong, không phát sinh số liệu hay nguồn mới.
- Lỗi 1 và 3 (P1) cần quyết định hoặc dữ liệu từ người (export từ khóa, mô tả listing Hose 4).
- Hose 1-3 chính xác với listing và PROJECT.md; Hose 4 chỉ dựa tên sản phẩm.
- P2 Hose 2 "carpet cleaning setups" còn nguyên, nên bỏ.
- Dữ liệu giả định: không giao khách.
