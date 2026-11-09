# REVIEW: 2026-11-09_brief_hose-parts.md

Người duyệt: seo-reviewer | Ngày: 2026-11-09 | Khách: tmf
Đã đọc: `Projects/SEO-OPS.md`, `Projects/tmf/PROJECT.md`, `Projects/_templates/brief.md`, `Projects/_templates/review.md`, toàn bộ brief (214 dòng), `outputs/2026-11-08_report_hose-parts-strategy.md` (đối chiếu), `skills/shopify-collection-seo-tmf/SKILL.md` (Gate 1, luật meta và keyword), `data/inputs/site_urls.csv` (kiểm URL), `data/keywords/clusters.csv` và `data/geo/prompts.csv` (đều chỉ có header).

## Điểm (thang 100)
| Nhóm | Tối đa | Điểm | Ghi chú |
|---|---|---|---|
| Đáp ứng intent | 25 | 14 | Intent ghi nhận đúng: "hose parts" theo kết quả search là trang gộp vacuum + solution + phụ kiện, rộng hơn collection (dòng 19, 33). Brief tự nhận rủi ro nhưng vẫn lập theo primary chưa khớp intent. Skill Gate 1 yêu cầu chốt URL ownership trước khi viết (SKILL.md dòng 118-119). Chưa có SERP Google US thật. |
| Đúng brief | 20 | 16 | Đủ mục theo template: thông tin đầu, outline, entity và câu hỏi, GEO prompt, internal link, nguồn, SERP, claim cấm. Outline đúng khung skill (không H1, intro 50-70 từ, Why Buy 60-100 từ, FAQ 5-7 câu 20-40 từ, Related Blogs, META). Trừ điểm: từ khóa phụ chưa chốt, clusters.csv trống. |
| E-E-A-T và nguồn | 20 | 13 | Fact sheet có nguồn tầng A, có danh sách 14 điểm cần xác minh, đánh dấu [CẦN NGUỒN]/[CẦN SỐ LIỆU] đúng chỗ. Trừ điểm: vài khẳng định không truy được URL (xem P1 dưới), entity chưa có trong fact sheet, nhiều fact chỉ từ "phần tóm tắt" của products.json, HTML collection chưa đọc được. |
| Khả năng được AI trích dẫn | 20 | 14 | Bảng so sánh PSI/nhiệt độ/chiều dài, FAQ câu hỏi trực tiếp, câu tóm "In short" là cấu trúc tốt. prompts.csv trống nên chưa gắn được prompt GEO nào. |
| Văn phong và compliance | 15 | 11 | Tôn trọng ràng buộc PROJECT.md (không năm thành lập, không ngưỡng free ship, không hãng sản xuất, không hotline trong meta, hàng hết không làm sản phẩm chính). Trừ điểm: meta description phương án 1 dài 156 ký tự, vượt giới hạn dưới 155 của skill. |
| **Tổng** | 100 | **68** | |

## Quyết định
**Sửa** (68 < 80). PROJECT.md không đặt ngưỡng riêng; dùng mặc định 80.

Lý do chặn chính: primary keyword chưa chốt. Theo skill `shopify-collection-seo-tmf` Gate 1, nếu từ khóa có thể trùng collection khác thì phải dừng và lấy quyết định URL ownership trước khi viết; brief đã nêu đúng rủi ro nhưng chưa có quyết định.

## Kiểm theo yêu cầu
- **Đủ mục theo template:** đạt. Mục "Prompt GEO" ghi rõ trống (đúng, prompts.csv chỉ có header).
- **Claim cấm khớp PROJECT.md:** đạt. PROJECT.md chưa có từ cấm của khách; brief ghi đúng [CẦN XÁC NHẬN] và chép đúng quy tắc fact của skill, đúng các mục "chưa được viết" (năm thành lập, ngưỡng free ship, hãng sản xuất thật).
- **Từ khóa và intent khớp SERP đã ghi:** chưa đạt. SERP đã ghi (dòng 184-195) cho thấy "hose parts" là intent rộng; collection chỉ có solution hose + 2 phụ kiện. Khuyến nghị của chính planner là đổi primary.
- **URL bịa:** không phát hiện. Đã kiểm 24 URL nội bộ (9 collection, 12 sản phẩm theo họ, 7 sản phẩm ngoài collection, 3 blog): tất cả có trong `data/inputs/site_urls.csv`. Số sản phẩm 33/30/15 của hose-cuffs/hoses-accessories/vacuum-hoses khớp file 2026-11-08 (dòng 16-18). URL đối thủ là kết quả web search, brief ghi rõ chưa mở từng trang; reviewer không kiểm truy cập được.

## Danh sách sửa
| Vị trí (trích đoạn) | Vấn đề | Mức P0 đến P3 | Cách sửa |
|---|---|---|---|
| Dòng 9: "Từ khóa chính: `hose parts` (theo người giao...)" và mục 11 câu 1 | Primary chưa chốt; khác intent SERP đã ghi; vi phạm Gate 1 skill (URL ownership, collection phải chứa đúng thứ từ khóa hứa). | P0 | Harry/Rob chốt primary. Nếu đổi sang `truckmount solution hose`, planner cập nhật dòng 9, cột primary ở mục 3, câu đầu intro, H2 mục 2/5/6 và cả 2 phương án meta. Ghi quyết định vào brief. |
| Dòng 38: "Vị trí và heading top 10: [CẦN SỐ LIỆU]" | Không có SERP Google.com en-US thật; skill yêu cầu URL, title, heading top 3-5, word count. Độ dài 600-750 từ là ước lượng không đối chiếu đối thủ (dòng 14). | P1 | Lấy SERP top 10 Google.com cho primary ĐÃ CHỐT (Harry dán hoặc công cụ rank), mở top 3-5 ghi heading và word count, rồi xác nhận lại độ dài mục tiêu. |
| Dòng 35: "Kết quả tìm kiếm có nhắc cách nói 'dùng được với máy có bơm dưới 3000 PSI'" | Khẳng định không có URL nguồn. | P1 | Gắn URL kết quả cụ thể, hoặc bỏ câu dẫn và giữ nguyên tắc tầng D. |
| Dòng 164: "một nhà bán khác trong kết quả search ghi hose 1/4\" thường 275°F" | Số liệu không truy được (không ghi URL). | P1 | Ghi URL nhà bán hoặc xóa con số 275°F. |
| Dòng 91: Entity bắt buộc "steel-braided, non-marking" | Hai entity này không có trong Fact Sheet mục 7; nếu writer buộc phải dùng sẽ thành mô tả sản phẩm không có nguồn. "quick connect" cũng là entity bắt buộc trong khi dòng 162 ghi chưa rõ hose có kèm đầu nối. | P1 | Thêm nguồn listing cho "steel-braided", "non-marking" vào Fact Sheet (họ nào, trích nguyên văn) hoặc bỏ khỏi danh sách bắt buộc. Đổi "quick connect" sang tùy chọn, chỉ dùng trong đoạn dẫn sang `hoses-accessories`. |
| Dòng 151, 153-154: "products.json (phần tóm tắt, không nguyên văn)" | Spec Hydro-Force 25 ft, Parker, Convenience Hose Outlet lấy từ bản tóm tắt; "rated 250 degrees" chưa có đơn vị. | P2 | Trước khi viết, đọc lại nguyên văn và ghi trích dẫn cụ thể (đã có trong danh sách xác minh mục 3, 7; giữ là điều kiện bắt buộc của Gate 1). |
| Dòng 99: meta description phương án 1, 156 ký tự | Vượt giới hạn "under 155 chars" của skill TMF (SKILL.md dòng 186), dù trong khoảng 140-160 của SEO-OPS. | P2 | Rút ít nhất 2 ký tự (ví dụ bỏ "at TMF Store" lặp hoặc đổi "sorted by" thành "by"). Đếm lại bằng script. |
| Dòng 100: meta phương án 2 "1/4 in." | Đã tự ghi rủi ro: Parker không ghi đường kính. | P2 | Nếu chọn phương án 2, sửa câu để không gán 1/4" cho toàn bộ hose, hoặc chờ xác minh Parker. |
| Dòng 85: FAQ "What diameter is a carpet cleaning solution hose?" | Đường kính Parker chưa rõ; câu trả lời dễ khái quát hóa quá dữ liệu. | P3 | Giữ câu hỏi nhưng ghi chú writer chỉ nêu 1/4" cho listing có ghi, hoặc trả lời theo tầng D có nguồn. |
| Dòng 138-141: "/products/tmf-hosezilla-25-...-with-bend-restrictors" | Handle viết tắt bằng "..."; writer không copy dùng được. URL đầy đủ có trong site_urls.csv. | P3 | Ghi handle đầy đủ (ví dụ `tmf-hosezilla-25-high-pressure-solution-hose-with-bend-restrictors`). |
| Dòng 10, 47 và mục 3 | clusters.csv trống, volume/KD [CẦN SỐ LIỆU]; từ khóa phụ chưa duyệt. | P2 | Sau khi chốt primary, Harry duyệt danh sách, planner ghi vào clusters.csv status `proposed`. Có Ahrefs/GSC thì điền số. |
| Dòng 80: "Why Buy... đổi trả 30 ngày kèm phí nhập kho 30% cho phụ kiện" | Đúng fact PROJECT.md, nhưng đưa phí nhập kho vào mục "Why Buy" là điểm trừ cho người mua. | P3 | Gợi ý writer chỉ nêu "30-day returns", để chi tiết phí cho trang chính sách (link). |

## Tóm tắt
1. Brief đầy đủ cấu trúc template, không có URL bịa (24 URL nội bộ đều có trong site_urls.csv), ràng buộc PROJECT.md và skill được chép đúng.
2. Chặn duyệt (P0): primary `hose parts` chưa khớp intent SERP đã ghi và chưa có quyết định URL ownership theo Gate 1 của skill.
3. P1: thiếu SERP Google thật; 2 khẳng định không có URL (3000 PSI, 275°F); entity "steel-braided", "non-marking" không có nguồn trong Fact Sheet.
4. P2: meta phương án 1 dài 156 ký tự (skill yêu cầu dưới 155); nhiều spec còn lấy từ bản tóm tắt products.json; từ khóa phụ chưa vào clusters.csv.
5. Sau khi Harry/Rob chốt primary và planner sửa các mục P0-P1, gửi lại để chấm vòng 2.
