# TMF - Collection `high-pressure-solution-line-hoses` - Gate 1 + Strategy (Bước 4, CHỜ DUYỆT)

Ngày: 2026-11-08 | Skill: shopify-collection-seo-tmf | Thị trường: en-US (giả định, chưa được xác nhận; tin nhắn gửi ô 4 còn nguyên placeholder)
Từ khóa chính người giao: `hose parts`

## 0. Inputs đã lấy
- `Projects/tmf/inputs/site_urls.csv`: lấy từ sitemap.xml, 471 blog + 212 collection + 64 page + 971 product (cột type,url).
- Collection fetch qua `/collections/high-pressure-solution-line-hoses/products.json` (HTTP 200, 14 listing). Ngày kiểm: 2026-11-08.

## 1. GATE 1a - Collection Reality Check: CÓ VẤN ĐỀ, cần bạn quyết định

**Collection này không phải collection "hose parts".** Nó là hose dung dịch áp lực cao.
- Live title: "Carpet Cleaning Hose Replacement". Không chứa "hose parts". Meta hiện tại có "hose parts" (`...hose replacement and hose parts at TMF - durable vacuum and solution hoses...`). Chữ "vacuum hoses" trong meta sai so với nội dung: collection không có hose hút nào.
- Nội dung thật (14 listing): Hydro-Force Pro Solution Hose (25/50/100/150 ft), TMF Hosezilla (25/50/100/150/250/300 ft), Parker Parflex Truckmount Solution Hose (Blue 50, Orange 50), Convenience Hose Outlet, Hide-A-Hose Swivel Cuff 1.5".
- Intent "hose parts" (cuff, connector, barb, ball valve, quick connect...) nằm ở collection khác:
  - `/collections/hose-cuffs` (33 sản phẩm, title "Flash Cuffs - Hose Cuffs for Sale - TMF Store", meta cũng viết "parts")
  - `/collections/hoses-accessories` (30 sản phẩm: quick connects, ball valve, hose crimps, hose net, vacuum hose...)
  - `/collections/vacuum-hoses` (15 sản phẩm)
  - `/collections/parts` và `/collections/hoser-hose-washer`: 0 sản phẩm (không link).
- Rủi ro cannibalization: đặt `hose parts` lên collection này sẽ cạnh tranh với `hose-cuffs` và `hoses-accessories`. Cụm này chưa có trong keyword map của known-issues.md. Skill yêu cầu TMF quyết định URL ownership trước khi viết.

**Đề xuất (cần bạn chọn):**
- **Phương án A (khuyến nghị):** primary = `truckmount solution hose` (hoặc `high pressure solution hose`). `hose parts` chỉ làm secondary, kèm một đoạn dẫn sang `hose-cuffs` và `hoses-accessories`. Khớp với 14 sản phẩm thật, giảm trùng URL. Đề nghị đổi live title thành chứa từ khóa này (ví dụ "Truckmount Solution Hose").
- **Phương án B:** giữ `hose parts` làm primary đúng yêu cầu ban đầu. Skill cho phép, nhưng trang sẽ hứa "parts" trong khi chỉ có hose và 2 phụ kiện (bounce risk), và trùng ý định với 2 collection khác. Nếu chọn B, tôi vẫn cần bạn xác nhận ai sở hữu từ khóa.

Các kiểm tra Gate 1a còn lại: handle copy từ sitemap, trả 200. Chưa có handle nhiễu gần giống. Link out: chỉ link collection đã mở và đếm (hose-cuffs 33, hoses-accessories 30, vacuum-hoses 15).

## 2. GATE 1b - Product Fact Sheet (Tier A, từ listing JSON ngày 2026-11-08)

| Sản phẩm (title live) | Giá / tồn kho | Category | Mechanism / mô tả trích từ listing | Spec |
|---|---|---|---|---|
| Hydro-Force Pro Solution Hose 25 ft (`hydro-force-pro-solution-hose-25-feet`) | $78.99, còn | solution hose | "tough, yet flexible polymer coating"; "Steel-braided"; "Non-marking" | 1/4" ĐK; "Rated at 250 degrees and 4,000 PSI" |
| Hydro-Force Pro 50 ft (`...-50-feet`) | $135.00, còn | như trên | như trên | như trên |
| Hydro-Force Pro 100 ft (`...-100-feet`) | $255.00, còn | như trên | như trên; có bảng "Loss of Material" 0.3 g theo ISO so với hose đối thủ | như trên |
| Hydro-Force Pro 150 ft (`...-150-feet`) | $379.99, còn | như trên | như trên | như trên |
| TMF Hosezilla 25' With Bend Restrictors | $75.00, **HẾT** | solution hose | "steel-braided, non-marking construction and flexible polymer coating"; "bend restrictors" | 1/4" ĐK; "Heat rated to 250°F"; "Rated at 3,000 PSI" |
| TMF Hosezilla 50' | $130.00, **HẾT** | như trên | như trên | như trên |
| TMF Hosezilla 100' (handle `...-50-...-copy`) | $245.00, **HẾT** | như trên | như trên | như trên |
| TMF Hosezilla 150' | $370.00, **HẾT** | như trên | như trên | như trên |
| TMF Hosezilla 250' | $475.00, còn | như trên | như trên | như trên |
| TMF Hosezilla 300' | $585.00, còn | như trên | như trên | như trên |
| Parker Parflex Truckmount Solution Hose - Blue (50') | $222.00, còn | solution hose ("A great lead hose") | "smooth, seamless thermoplastic inner tube specially compounded for use with high temperature solutions"; "lose less heat than other hoses" | "up to 1,750 PSI"; "up to 230° F" |
| Parker Parflex ... Orange (50') | $222.00, còn | như trên | như trên | như trên |
| Convenience Hose Outlet | $102.00, còn | outlet (phụ kiện) | "connects between the truckmount (or portable) and the solution hose"; dùng để pha dung dịch, đổ sprayer, rửa hose; "SHIPS IN BLUE OR BLACK" | không có spec |
| Hide-A-Hose Swivel Cuff - 1.5" inch | $23.99, còn | swivel cuff | Listing chỉ có 2 câu chung chung. Theo product-corrections.md, "Hide-A-Hose" ở TMF là chạy solution hose bên trong vacuum hose | ĐK 1.5" |

Rating + số review (Okendo): **chưa lấy được**, cần đọc từ trang render. Vì vậy bài không được nêu rating. Ô trống = không viết.

**Mâu thuẫn / lưu ý trên listing (flag cho TMF):**
1. Hydro-Force listing: "Length (25, 50, 100 or 150)" nhưng cùng trang đó là 4 listing riêng, ổn. Hosezilla Key Features liệt kê "25', 50', 150', 250', or 300'" (không có 100'), trong khi collection có listing 100'.
2. Listing Hosezilla 100' dùng handle `...-50-...-copy`, dấu hiệu nhân bản. Cần TMF kiểm tra trước khi link.
3. Cả Hydro-Force lẫn Hosezilla đều viết kiểu "outlasts any/every other comparable hose". Đây là claim so sánh của listing/nhà sản xuất, không dùng làm claim của TMF Store trong bài (banned pattern 1, 8). Số "0.3 grams" nằm trong listing, nếu dùng phải quy cho listing/Hydro-Force.
4. Hosezilla 25/50/100/150 hết hàng. Chỉ 250' và 300' còn. Không đưa làm hero.
5. Parker: 1,750 PSI vs Hydro-Force 4,000 PSI vs Hosezilla 3,000 PSI. Đây là pressure rating, chưa có thông tin pressure requirement của máy; bài chỉ nói chung "chọn hose có rating bằng hoặc cao hơn áp suất làm việc của máy" (Tier D).
6. Tier B (nhà sản xuất): chưa mở. Không thêm spec ngoài listing.

## 3. GATE 1c - Blog Whitelist (đo thật từ HTML, ngày 2026-11-08)
Không tìm thấy bài blog nào viết riêng về solution hose. Ứng viên gần chủ đề (hose / vacuum / cuff), số từ đo trong thẻ `<article>`, có thể gồm cả chữ của theme, cần đo lại thủ công trước khi duyệt:
| URL | Từ | Ghi chú |
|---|---|---|
| /blogs/news/how-to-organize-truckmount-vacuum-hose-without-vacuum-reel | ~1,019 | Về vacuum hose, không phải solution hose |
| /blogs/news/vacuum-with-the-power-of-your-truckmount | ~1,180 | Vacuum, liên quan gián tiếp |
| /blogs/news/how-much-vacuum-does-a-truckmount-have | ~1,008 | Vacuum |
| /blogs/news/seal-vacuum-inlet-what-to-use-carpet-truckmount | ~932 | Vacuum |
Loại (dưới 300 từ hoặc video): `new-tmf-converter-tough-cuff-1-5-to-2` (19), `ways-to-bring-hoses-over-balcony` (44), `vacuum-boost` (380 nhưng chưa xét nội dung). Trong blacklist cũ: `which-flash-cuffs-is-right-for-you`, `tips-on-wand-cuffs-to-maximize-vacuum`, `video-should-you-use-a-leader-hose`, `proper-psi-...-inline-sprayers`.
**Kết luận:** có thể chưa đủ 3 bài đúng chủ đề solution hose. Theo skill, tôi báo thiếu thay vì độn bài. Đề xuất TMF viết 1 bài về chọn solution hose (PSI, chiều dài, lead hose).

## 4. GATE 1d - Brand facts
Dùng nguyên văn `references/tmf-brand-facts.md`: không ghi năm thành lập; "thousands of professionals"; điện thoại 1-800-949-7726 (9-5 EST, T2-T6) kèm giờ, không đưa vào meta; link `/pages/military`, `/pages/loyalty` nếu dùng. Không đưa free shipping $300 (chưa xác minh). Với hose đơn lẻ dưới $1,000, không cần nhấn financing.

## 5. STEP 2 - SERP (giới hạn, cần nói rõ)
`WebSearch` chỉ trả danh sách kết quả tóm tắt, **không phải top 10 Google US có thứ tự**, không có heading hay word count. Tôi không bịa phần đó. Tôi đã chạy 2 truy vấn: "hose parts carpet cleaning truckmount" và "truckmount solution hose high pressure carpet cleaning". Những gì rút ra được (chỉ ở mức loại trang, không phải heading):
- Các nhà bán hàng cạnh tranh (Jon-Don, Kleen Kuip, Clean Freak, Interlink Supply, Dultmeier) dùng trang collection/catalog, nhóm theo vacuum hose / solution hose / hose phụ kiện. Intent "hose parts" tách vacuum hose, solution hose và phụ kiện, tức là rộng hơn collection này.
- Cụm tự nhiên gặp trong kết quả: "solution hose", "high pressure solution hose", "truckmount solution hose", "carpet cleaning solution hose", "vacuum hose", "hose cuffs".
- Tôi **không thể** liệt kê H1/headings của top 10 hay cột "content gaps" thật. Nếu bạn muốn đủ Bước 2, hãy dán top 10 Google.com cho keyword đã chốt (Option 1 của skill), hoặc xác nhận chạy tiếp không SERP (Option 2). Báo cáo dưới đây dựa trên intent + persona + Fact Sheet, và đã được gắn cờ.

## 6. STEP 4 - Strategy Report (A-G)

**A. Search intent:** thương mại. Technician hoặc chủ máy đang cần thay hoặc mua hose dung dịch cho truckmount/portable. Sẵn sàng mua cao. Hành động tiếp: chọn chiều dài và rating rồi thêm vào giỏ. Động lực: không dừng việc giữa job, hose không để lại vết trong nhà khách.

**B. Persona:** owner-operator hoặc đội nhiều xe. Đau: hose hỏng giữa job, không biết chọn rating, chiều dài. Tiêu chí chọn: PSI rating so với máy, nhiệt độ, chiều dài, không để vết (non-marking), độ cứng/gập. Câu hỏi trước khi mua: hose nào hợp máy tôi, cần mấy feet, còn hàng không.

**C. SERP insight (có giới hạn, xem mục 5):** dạng trang chủ yếu là collection/catalog bán hàng. Gợi ý information-gain, đều có nguồn trong Fact Sheet hoặc là Tier D:
1. Bảng chọn theo PSI rating thực tế của sản phẩm TMF (4,000 / 3,000 / 1,750 PSI) và chiều dài. Cả ba cột đều có dữ liệu thật.
2. "Lead hose" (Parker Parflex, trích listing) và hose dài theo chiều dài job.
3. Outlet ở xe (Convenience Hose Outlet) và quy tắc chung: rating hose phải bằng hoặc cao hơn áp suất làm việc của máy (Tier D).

**D. Strategy decision**
| Mục | Quyết định |
|---|---|
| Intent phục vụ | Mua hose dung dịch thay thế |
| Mục tiêu nội dung | Giúp chọn đúng rating + chiều dài, dẫn đến product page |
| Chuyển đổi | Link sản phẩm theo từng họ + bảng chọn |
| Tone | Thương mại, thẳng, US English, không dash dài |
| Độ dài | ~600-750 từ (14 listing nhưng chỉ 4 họ sản phẩm, có bảng) |

**E. Outline (không có H1, mở bằng intro 50-70 từ có primary trong câu đầu)**
1. Intro (nêu từ khóa chính ngay câu đầu)
2. H2 Shop by category: Solution Hoses (bảng họ sản phẩm: Hydro-Force Pro, Hosezilla, Parker Parflex; chiều dài, rating, giá, tồn kho) và liên kết sang `hose-cuffs`, `hoses-accessories`. Chỉ ở mục này mới có tên sản phẩm.
3. H2 How to Choose a Solution Hose (rating so với áp suất máy, nhiệt độ, chiều dài, non-marking; Tier D, không tên sản phẩm; kết "In short, ...")
4. H2 Hose Length and Fitment Table (chiều dài theo họ sản phẩm, link; chỉ dùng số trong listing)
5. H2 Why Buy [Primary] at TMF Store (60-100 từ, theo brand-facts)
6. H2 FAQ (5-7 câu, mỗi câu 20-40 từ, không tên sản phẩm)
7. H2 Related Blogs (chỉ bài qua whitelist, báo thiếu nếu không đủ 3)
8. META

Hết hàng: nói rõ Hosezilla 25/50/100/150 đang hết, mở bằng sản phẩm còn hàng (Hydro-Force Pro 25-150, Hosezilla 250/300).

**Framework Feasibility Check**
- Trục PSI rating: sản phẩm trải 1,750 / 3,000 / 4,000 - có phân hóa thật. OK.
- Trục chiều dài: 25 đến 300 ft - có phân hóa. OK.
- Trục nhiệt độ: 230 / 250 / 250 - phân hóa yếu, chỉ nêu như thông số, không làm khung chọn.
- Người đọc thực hiện được khung chỉ bằng sản phẩm của collection: có. Gợi ý đầu bảng trỏ sản phẩm còn hàng: có.
- Không dùng khung "pressure requirement": chưa có dữ liệu máy.

**F. On-page SEO (theo phương án A; phương án B ở dưới)**
- Collection title: live "Carpet Cleaning Hose Replacement" **không chứa primary** (cả A lẫn B). Cần TMF đổi title; tôi chỉ gắn cờ.
- Meta Title A (45 ký tự): `Truckmount Solution Hose for Sale | TMF Store`
- Meta Description A (142 ký tự): `Shop high pressure truckmount solution hoses at TMF Store. Compare Hydro-Force Pro, TMF Hosezilla and Parker Parflex by length and PSI rating.`
- Meta Title B (54): `Hose Parts for Truckmounts: Solution Hoses | TMF Store`
- Meta Description B (154): `Shop hose parts for truckmounts: solution hoses, Hydro-Force Pro, TMF Hosezilla and Parker Parflex, plus cuffs and accessories. Compare by length and PSI.` (nội dung "plus cuffs" chỉ đúng khi bài có link sang `hose-cuffs`; collection chỉ có 1 swivel cuff)
- Đã giữ token `| TMF Store`, không đưa số điện thoại, có mô hình/thương hiệu thật. Description chưa có CTA mềm rõ ràng; có thể thêm "Compare" như đã làm. Lưu ý: PROJECT.md ghi meta hiện tại gồm "vacuum hoses" nhưng collection không có, nên bản mới bỏ.
- Từ khóa phụ đề xuất (không có từ khóa phụ từ người giao, lấy theo kết quả tìm): `high pressure solution hose`, `carpet cleaning solution hose`, `truckmount solution hose` (nếu A: primary), `Hydro-Force Pro solution hose`, `TMF Hosezilla`, `Parker Parflex solution hose`, `solution hose 4000 PSI`. Cần bạn chốt, và tôi chưa kiểm khối lượng tìm kiếm thật.

**G. Links + Related Blogs (dự kiến, chỉ URL có trong sitemap)**
- Sub-collection/liên quan: `/collections/hose-cuffs` (anchor "hose cuffs"), `/collections/hoses-accessories` (anchor "hose accessories"), `/collections/vacuum-hoses` (anchor "vacuum hoses", để người cần hose hút).
- Sản phẩm: link tới từng họ qua handle thật (vd `/products/hydro-force-pro-solution-hose-100-feet`, `/products/tmf-hosezilla-250-high-pressure-solution-hose-with-bend-restrictors`, `/products/parker-parflex-truckmount-solution-hose-blue-50`, `/products/convenience-hose-outlet`).
- Related blogs: chờ quyết định ở mục 3.

## 7. Cần bạn duyệt / trả lời trước khi viết
1. Chọn **A hay B** cho primary (xem 1). Tôi khuyên A.
2. Chốt thị trường **en-US** (mục 4 trong tin nhắn trước chưa điền).
3. Chốt bộ từ khóa phụ (mục F).
4. SERP: dán top 10 Google US, hoặc cho phép chạy tiếp không SERP (đã gắn cờ).
5. Blog: đồng ý dùng bài vacuum hose liên quan gián tiếp, hay để mục Related Blogs ngắn hơn 3 bài.
6. Cho phép mở trang render để lấy rating và số review (hiện chưa có, bài sẽ không nêu rating).

Chưa viết bài. Chờ phản hồi.
