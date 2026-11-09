# REVIEW: 2026-11-09_brief_hose-parts_v2.md

Người duyệt: seo-reviewer | Ngày: 2026-11-09 | Khách: tmf | Vòng: 2
Đã đọc: `Projects/SEO-OPS.md`, `Projects/tmf/PROJECT.md`, `Projects/_templates/brief.md`, `Projects/_templates/review.md`, toàn bộ brief v2 (244 dòng), review vòng 1 (`outputs/2026-11-09_review_brief_hose-parts.md`, 68 điểm, "sửa"), `skills/shopify-collection-seo-tmf/SKILL.md`. Đối chiếu bằng grep: `data/inputs/site_urls.csv`, `skills/shopify-collection-seo-tmf/references/known-issues.md`, `product-corrections.md`, `tmf-brand-facts.md`, `outputs/2026-11-08_report_hose-parts-strategy.md`. `data/keywords/clusters.csv` và `data/geo/prompts.csv` đều chỉ có 1 dòng (header). Không mở shop.truckmountforums.com (Cloudflare 429).

Bối cảnh đã chốt: Harry quyết định ngày 2026-11-09 16:48, primary `truckmount solution hose`, `hose parts` là từ khóa phụ. Reviewer coi đây là quyết định cuối.

## Điểm (thang 100)
| Nhóm | Tối đa | Điểm | Ghi chú |
|---|---|---|---|
| Đáp ứng intent | 25 | 22 | Primary mới khớp đúng thứ collection bán (14 listing: 3 họ solution hose + Convenience Hose Outlet + Hide-A-Hose, dòng 24). Intent thương mại khớp kết quả search đã ghi (dòng 32-36, 198-213): kết quả nghiêng về trang sản phẩm, hai listing TMF có mặt. Đoạn dẫn ra cho intent "hose parts" rộng được giữ bắt buộc (dòng 26, 84). Trừ điểm: vẫn chưa có top 10 Google.com en-US có thứ tự, heading và word count (dòng 41, 219). |
| Đúng brief | 20 | 18 | Đủ mục theo template. Outline đúng khung skill: không H1, intro 50-70 từ có primary ở câu đầu, How to choose có câu "In short", Why Buy 60-100 từ, FAQ 5-7 câu 20-40 từ không tên sản phẩm, Related Blogs, META. Trừ điểm: từ khóa phụ chưa duyệt, clusters.csv còn trống (ghi rõ là mở, dòng 13, 240); hai bảng ở mục 4.2 và 4.4 trùng nội dung. |
| E-E-A-T và nguồn | 20 | 17 | Fact Sheet nay trích nguyên văn từ products.json theo handle (dòng 165-169). Hai khẳng định không URL của v1 (3000 PSI, 275°F) đã xóa và ghi lý do (dòng 38-39). Entity steel-braided, non-marking có trích nguồn và loại trừ Parker (dòng 97-100). Mọi số trong meta truy được về Fact Sheet. Trừ điểm: Why Buy dùng fact từ PROJECT.md (family owned, giao trong ngày trước 12 PM EST, 30-day returns) trong khi skill yêu cầu Why Buy lấy fact "only from references/tmf-brand-facts.md", và file đó không có ba fact này; HTML collection vẫn chưa đọc được. |
| Khả năng được AI trích dẫn | 20 | 16 | Bảng so sánh 3 họ hose theo PSI 1,750 / 3,000 / 4,000 là information gain có thật, FAQ dạng câu hỏi trực tiếp, câu tóm "In short". Trừ điểm: prompts.csv trống nên chưa gắn prompt GEO; H3 Heat rating dựa trên trục 230 / 250 / 250 mà file 2026-11-08 (dòng 112) đã đánh giá "phân hóa yếu, không làm khung chọn". |
| Văn phong và compliance | 15 | 14 | Meta đạt giới hạn (đếm bằng script, xem dưới). Không có em dash hay en dash trong brief (script đếm 0). Không hotline trong meta, không năm thành lập, không ngưỡng free ship, hàng hết không làm sản phẩm chính, "made by Parker" và Prop 65 để người quyết. Trừ nhẹ: cả hai title bỏ cụm "Carpet Cleaning" của title live; phương án 1 bỏ luôn "Hose Replacement". |
| **Tổng** | 100 | **87** | |

## Quyết định
**Đạt** (87, từ 80). PROJECT.md không đặt ngưỡng riêng; dùng mặc định 80.

Điều kiện chuyển sang seo-writer: Harry trả lời các mục mở ở dòng 239-244 của brief (meta, từ khóa phụ, SERP thật hay chạy theo Option 2 của skill, "made by Parker", Prop 65). Writer vẫn phải chạy Gate 1 (đọc HTML collection, đếm collection link ra, đo blog) trước khi viết.

## Kiểm theo yêu cầu
- **Đủ mục theo template:** đạt. Thông tin đầu (dòng 9-18), Outline (mục 4), Entity và câu hỏi (dòng 86-101, nằm trong mục 4, không có heading riêng), Prompt GEO (mục 9, ghi rõ trống), Internal link (mục 6), Nguồn và SERP (mục 8), Claim cấm (mục 10).
- **Từng mục sửa vòng 1:**

| Mục vòng 1 | Mức cũ | Trạng thái v2 | Bằng chứng |
|---|---|---|---|
| Primary chưa chốt, Gate 1a URL ownership | P0 | Đã xử lý | Dòng 7, 12, 22; cột primary mục 3 (dòng 55); intro dòng 75; H2 dòng 76, 77; cả hai meta (dòng 109-110) đều đổi sang primary mới |
| Thiếu SERP Google.com thật, độ dài không đối chiếu đối thủ | P1 | Còn mở, ghi rõ | Dòng 17, 41, 219, 241. Đã chạy lại search cho primary mới và mở được 1 trang đối thủ (Interlink). Hạ xuống P2 vì skill cho phép Option 2 có flag, nhưng Harry phải chọn |
| Câu "dưới 3000 PSI" không URL | P1 | Đã xử lý (xóa) | Dòng 38, 231 |
| Số 275°F không URL | P1 | Đã xử lý (xóa) | Dòng 39, 231 |
| Entity steel-braided, non-marking không nguồn; quick connect bắt buộc | P1 | Đã xử lý | Dòng 97-101: trích nguyên văn theo handle, Parker loại trừ, quick connect thành tùy chọn chỉ ở đoạn dẫn ra |
| Spec lấy từ bản tóm tắt products.json, "250 degrees" thiếu đơn vị | P2 | Đã xử lý | Dòng 165-169, 174, 178: trích nguyên văn; Hydro-Force giữ "250 degrees" không thêm °F |
| Meta mô tả phương án 1 dài 156 | P2 | Đã xử lý | Script: 151 và 149 ký tự |
| Meta phương án 2 gán 1/4" | P2 | Đã xử lý | Dòng 113: không phương án nào ghi 1/4" |
| clusters.csv trống, từ khóa phụ chưa duyệt | P2 | Còn mở, ghi rõ | Dòng 13, 51, 240. Chờ Harry, đúng điểm dừng |
| FAQ đường kính dễ khái quát | P3 | Đã xử lý | Dòng 90 |
| Handle viết tắt "..." | P3 | Đã xử lý | Dòng 142-155: handle đầy đủ |
| Phí nhập kho trong Why Buy | P3 | Đã xử lý | Dòng 85, 232 |

- **Claim cấm khớp PROJECT.md:** đạt. PROJECT.md chưa có từ cấm của khách; brief ghi [CẦN XÁC NHẬN] (dòng 227) và chép đúng quy tắc fact của skill cùng các mục "chưa được viết" (năm thành lập, ngưỡng free ship, hãng sản xuất thật; dòng 228-229). Xử lý "made by Parker" (dòng 186) đúng tinh thần PROJECT.md dòng 21: chỉ trích listing, để Harry quyết.
- **Từ khóa và intent khớp SERP đã ghi:** đạt. Truy vấn primary có trong bảng dòng 196-213; kết quả là trang sản phẩm và danh mục bán solution hose, intent thương mại. Một kết quả lệch (vacuum hose, dòng 203) được đánh dấu đúng. Lưu ý: SERP nghiêng về trang sản phẩm, nên bảng sản phẩm có link phải nằm sớm trong bài (outline đã đặt ở H2 đầu tiên).
- **URL bịa:** không phát hiện. Script lấy 23 URL đầy đủ và 20 đường dẫn tương đối của shop.truckmountforums.com trong brief, đối chiếu `site_urls.csv`: tất cả có mặt, trừ endpoint `.../collections/high-pressure-solution-line-hoses/products.json?limit=250` (API, không phải trang, hợp lệ). Gồm cả handle bất thường `tmf-hosezilla-50-high-pressure-solution-hose-with-bend-restrictors-copy`. URL đối thủ là output web search; reviewer không mở (chỉ Interlink được brief ghi là đã mở).
- **Số liệu truy nguồn:** 33/30/15 sản phẩm khớp `2026-11-08_report_hose-parts-strategy.md` dòng 16-18 (brief ghi "chưa đếm lại hôm nay"). Blog leader hose 36-71 từ khớp known-issues.md dòng 76. Mô tả Hide-A-Hose khớp product-corrections.md dòng 74. Nhận định "keyword map không có cụm solution hose" khớp grep known-issues.md. Giá, tồn kho, PSI, nhiệt độ quy về products.json đọc 2026-11-09; reviewer không mở lại (429), chấp nhận theo nguồn và ngày ghi.
- **Meta (script Python, len(), tính khoảng trắng):**

| Phương án | Title | Ký tự | Description | Ký tự | Kết quả |
|---|---|---|---|---|---|
| 1 | Truckmount Solution Hose: High Pressure Hoses \| TMF Store | 57 | Shop truckmount solution hose at TMF Store: ... Compare PSI. | 151 | Đạt 40-60, đạt 140-160 và dưới 155 |
| 2 | Truckmount Solution Hose and Hose Replacement \| TMF Store | 57 | Truckmount solution hose rated 1,750 to 4,000 PSI: ... Shop TMF Store. | 149 | Đạt 40-60, đạt 140-160 và dưới 155 |

Số ký tự brief ghi (57/57/151/149) khớp script. Cả hai có primary ở đầu title, có brand token `| TMF Store`, có tên hãng và model collection bán (luật meta của skill).

## Danh sách sửa
| Vị trí (trích đoạn) | Vấn đề | Mức P0 đến P3 | Cách sửa |
|---|---|---|---|
| Dòng 41: "KHÔNG phải top 10 Google.com có thứ tự... [CẦN SỐ LIỆU]" | Skill Step 2 yêu cầu top 10 Google US, heading top 3-5, word count. Chưa có; độ dài 500-700 từ chưa đối chiếu đối thủ. | P2 | Trước khi viết, Harry chọn: dán SERP Google.com en-US (Option 1) hoặc chạy Option 2 có flag trong strategy report. Ghi lựa chọn vào brief hoặc ghi chú duyệt. |
| Dòng 85: "Why Buy... family owned and operated (About Us); đơn đặt trước 12 PM EST giao trong ngày làm việc; 30-day returns" | Skill: Why Buy lấy fact "only from references/tmf-brand-facts.md". Ba fact này có nguồn tầng C trong PROJECT.md (đọc 2026-11-09) nhưng không có trong tmf-brand-facts.md. Brand-facts gợi ý các fact đã xác minh khác: military discount, TMF Rewards (kèm link /pages/military, /pages/loyalty). | P2 | Harry xác nhận cho dùng fact tầng C từ PROJECT.md trong Why Buy (đề xuất bổ sung vào brand-facts, chờ duyệt), hoặc đổi sang fact có trong brand-facts. Nếu dùng military/loyalty, grep site_urls.csv trước khi link. |
| Dòng 13, 51, 240: từ khóa phụ "ĐỀ XUẤT... CHƯA ghi vào clusters.csv" | Secondary chưa duyệt; skill yêu cầu mỗi secondary xuất hiện ít nhất một lần, nên danh sách 14 cụm cần thu gọn trước khi viết. | P2 | Harry duyệt và rút còn khoảng 4-6 cụm writer phải phủ; planner ghi clusters.csv status `proposed`. |
| Dòng 76 và 83: "Bảng 3 họ hose..." và "Solution Hose Length and Rating Chart" | Hai bảng cùng trục (họ x chiều dài x PSI), dễ lặp nội dung, tốn từ trong collection 350-500 từ theo skill. | P2 | Gộp thành một bảng spec có link ở H2 đầu; hoặc nói rõ bảng 4.4 khác trục gì (ví dụ chiều dài theo kiểu job). |
| Dòng 79: "H3: Heat rating" | Framework Feasibility Check: trục nhiệt 230 / 250 / 250, Hydro-Force không ghi đơn vị; file 2026-11-08 dòng 112 khuyên không làm khung chọn. | P3 | Gộp nhiệt độ vào H3 áp suất như thông số kèm, không thành tiêu chí chọn riêng. |
| Dòng 81: "H3: Fittings and diameter... listing TMF không nói hose kèm đầu nối" | Người đọc không thực hiện được tiêu chí này chỉ với dữ liệu collection (Feasibility Check của skill). | P3 | Giữ ngắn ở mức tầng D (kiểm đầu nối máy trước khi mua) và dẫn sang `hoses-accessories`; không mở rộng thành khung chọn. |
| Dòng 183: "Mô tả 'chạy solution hose trong vacuum hose' lấy từ product-corrections.md; chưa có trên listing" | Skill coi product-corrections.md là "verified truth" và yêu cầu kiểm file này trước khi viết; brief thận trọng hơn mức cần. | P3 | Ghi rõ writer được dùng mô tả của product-corrections.md (dòng 74) cho Hide-A-Hose, không thêm chi tiết khác. |
| Dòng 109-110: hai title | Cả hai bỏ "Carpet Cleaning" của title live; phương án 1 bỏ thêm "Hose Replacement". Skill: không bỏ term có giá trị nếu không lập luận được. | P3 | Khi Harry chọn, ghi lý do bỏ term (ví dụ ưu tiên primary đã chốt); cân nhắc giữ "Carpet Cleaning" ở description hoặc title collection mới. |
| Dòng 130-131: `/collections/accessories`, `/collections/truckmount-parts` "Chưa mở" | Skill: không link collection chưa mở và đếm. Brief đã đánh dấu. | P3 | Writer mở và đếm trong Gate 1a; không link nếu không mở được. |
| Dòng 86-101: entity và câu hỏi nằm trong mục 4 | Template có mục "Entity và câu hỏi cần trả lời" riêng. Nội dung đủ, chỉ lệch cấu trúc. | P3 | Lần sau tách heading riêng cho dễ đối chiếu. |

## Tóm tắt
1. Đạt 87/100: brief v2 xử lý P0 (primary chốt theo quyết định Harry 16:48) và cả 3 mục P1 có thể sửa; 1 mục P1 cũ (SERP thật) còn mở, ghi rõ, hạ xuống P2.
2. Không URL bịa: 23 URL đầy đủ và 20 đường dẫn tương đối đều có trong site_urls.csv (trừ endpoint products.json, hợp lệ).
3. Meta đạt bằng script: title 57/57, description 151/149, đều dưới 155 và có brand token.
4. Còn mở trước khi viết: Harry chọn meta, duyệt từ khóa phụ, chọn Option SERP, quyết "made by Parker", Prop 65, và nguồn fact cho Why Buy.
5. Writer chạy Gate 1 (HTML collection, đếm collection link ra, đo blog) và gộp bảng trùng; không cần gửi lại reviewer cho brief, chỉ duyệt bài viết sau.
