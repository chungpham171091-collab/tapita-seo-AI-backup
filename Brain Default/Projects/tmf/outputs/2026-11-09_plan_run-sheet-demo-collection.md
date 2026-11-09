# TMF: Run sheet demo, collection high-pressure-solution-line-hoses (Bước A, CHƯA CHẠY GÌ)

Ngày: 2026-11-09 | Khách: tmf | Thị trường: en-US (registry, xác nhận 2026-11-09) | Người phụ trách: Harry | Người duyệt phía khách: Rob
Collection demo: https://shop.truckmountforums.com/collections/high-pressure-solution-line-hoses (14 sản phẩm hiển thị, theo PROJECT.md)
Nguồn đã đọc: `Projects/SEO-OPS.md` (mục 3, 5), `Projects/tmf/PROJECT.md`, `sources.md`, dòng tmf trong `_registry/projects.csv`, header các file trong `data/`, `outputs/2026-11-08_report_hose-parts-strategy.md`, file workflow trong `workflows/seo-*.md`.

## 0. Từ khóa chính: đề xuất thay "hose parts"

**Đề xuất: `truckmount solution hose`** (phụ: `high pressure solution hose`, `carpet cleaning solution hose`; `hose parts` chỉ làm từ khóa phụ kèm đoạn dẫn sang collection khác).

Lý do, đều từ file 2026-11-08_report_hose-parts-strategy.md (mục 1 và 5), do Gate 1a đọc trực tiếp collection ngày 2026-11-08:
1. Collection chỉ gồm hose dung dịch: Hydro-Force Pro (25 đến 150 ft), TMF Hosezilla (25 đến 300 ft), Parker Parflex (Blue, Orange), Convenience Hose Outlet, Hide-A-Hose Swivel Cuff. Không có hose hút nào, dù meta cũ nhắc "vacuum hoses".
2. Intent "hose parts" (cuff, connector, quick connect, ball valve) nằm ở `/collections/hose-cuffs` (33 sản phẩm) và `/collections/hoses-accessories` (30 sản phẩm). Đặt "hose parts" lên trang này có nguy cơ cannibalization.
3. Cụm "solution hose", "high pressure solution hose", "truckmount solution hose" xuất hiện trong kết quả web search cùng ngày. Đây chỉ là tín hiệu định tính, KHÔNG phải xếp hạng hay volume.

Chưa có: volume, KD, SERP top 10 có thứ tự cho cả hai cụm: [CẦN SỐ LIỆU] (không có Ahrefs, GSC). Việc chọn cuối cùng là của Harry và Rob; bước 1 dưới đây là điểm chốt.
Lưu ý: file 2026-11-08 ghi thị trường là giả định; nay đã xác nhận en-US nên giả định đó hết hiệu lực.

## 1. Run sheet

Ký hiệu cột "Đang có đủ chưa": ĐỦ / MỘT PHẦN (chạy được nhưng thiếu số liệu, kết quả có [CẦN SỐ LIỆU]) / THIẾU (không chạy được) / BỎ QUA.
`<KW>` = từ khóa chính sau khi chốt ở bước 1. Đường dẫn file bước sau là mẫu, tên thật do workflow đặt (`YYYY-MM-DD_<loại>_<chủ-đề>.md`), tôi sẽ thay bằng đường dẫn thật khi chạy.

| # | Workflow | Dòng đầu vào chính xác | Điều kiện cần có | Đang có đủ chưa | Điểm dừng người duyệt | Đầu ra |
|---|---|---|---|---|---|---|
| 1 | seo-keyword-research | `tmf \| truckmount solution hose, hose parts \| en-US` | `data/keywords/ahrefs_2026-11.csv` và/hoặc `data/gsc/` (query) và `data/rank/` để có volume, KD | MỘT PHẦN. `clusters.csv` chỉ có header; các thư mục ahrefs, gsc, rank trống | Chốt từ khóa chính và phụ | `data/_summary/` (extractor), `data/keywords/clusters.csv`, ghi chú trong `outputs/` |
| 2 | seo-onpage-audit (baseline trang live) | `tmf \| https://shop.truckmountforums.com/collections/high-pressure-solution-line-hoses \| <KW>` | URL mở được; crawl, gsc, rank là tùy chọn (extractor sẽ ghi "thiếu") | MỘT PHẦN. URL có; không có crawl, gsc, rank. Cloudflare chặn 429 sau khoảng 15 request, cần giãn request | Chọn lỗi cần sửa | `outputs/..._audit_onpage_...md`, `outputs/..._review_onpage_...md`, `data/_summary/..._onpage_input.md` |
| 3 | seo-content-brief | `tmf \| https://shop.truckmountforums.com/collections/high-pressure-solution-line-hoses \| <KW> \| collection` | `clusters.csv` có từ khóa phụ (từ bước 1); `data/inputs/site_urls.csv` (có, 1.729 URL); web search cho SERP | MỘT PHẦN. site_urls có; clusters trống cho đến khi xong bước 1; SERP chỉ là kết quả web search tóm tắt, không phải top 10 Google có thứ tự | Duyệt brief | `outputs/..._brief_...md`, `outputs/..._review_brief_...md` |
| 4 | seo-content-writing (giai đoạn 1) | `tmf \| collection \| <KW> \| https://shop.truckmountforums.com/collections/high-pressure-solution-line-hoses \| Projects/tmf/outputs/<file brief đã duyệt ở bước 3>.md` | Brief đã duyệt; skill shopify-collection-seo-tmf (có Gate 1 fact sheet); mở collection và trang sản phẩm thật | MỘT PHẦN. Chưa có file brief (sinh ở bước 3). Đã có Gate 1 sơ bộ ngày 2026-11-08 (chưa có rating, review, Tier B). Tone, từ cấm, KPI của khách trống | Duyệt outline | `outputs/..._outline_...md` |
| 5 | seo-content-draft (giai đoạn 2) | `tmf \| Projects/tmf/outputs/<file outline đã duyệt ở bước 4>.md \| <ghi chú duyệt của người>` | Outline đã duyệt kèm ghi chú duyệt | THIẾU. Chưa có outline; ghi chú duyệt do Harry (hoặc Rob) viết sau bước 4 | Sau đó chạy bước 6 | `outputs/..._draft_...md` |
| 6 | seo-qa-fix | `tmf \| Projects/tmf/outputs/<file draft ở bước 5>.md \| <KW> \| en-US` | File draft; Gate 3 của skill TMF; skill compliance của khách (hiện KHÔNG có, cột compliance trong registry trống) | THIẾU (chưa có draft). Compliance trống thì audit chỉ theo luật chung SEO-OPS mục 4 và quy tắc fact của skill TMF | Duyệt bản _v2 | `outputs/..._review_...md`, `outputs/..._draft_..._v2.md` |
| 7 | seo-meta-optimization | `tmf \| 5 \| Projects/tmf/data/inputs/url_list.csv` | `url_list.csv` có các dòng URL, cột url, meta_title_current, meta_description_current, content_current; ahrefs tùy chọn | THIẾU. `url_list.csv` chỉ có header (0 dòng dữ liệu) | Chỉnh từ khóa, duyệt bảng | `data/_summary/..._meta_batch.csv`, `outputs/..._meta_...md` |
| 8 | seo-feedback-localization | (không chạy) mẫu: `tmf \| <file bài> \| <feedback của Rob> \| en-US` | File bài và feedback của khách | BỎ QUA. Lý do: chưa có feedback của Rob (khách) cho bài nào; thị trường đích trùng thị trường gốc en-US nên không có bước bản địa hóa. Chạy khi Rob gửi feedback cho bản _v2 | Duyệt bản mới | (không có) |
| 9 | seo-image-plan | (không chạy) mẫu: `tmf \| <file blog hoàn chỉnh>` | File blog hoàn chỉnh | BỎ QUA. Lý do: workflow dành cho blog; demo là collection và chưa có blog nào. Gate 1c ngày 2026-11-08 cũng ghi chưa có bài blog đúng chủ đề solution hose | Người tạo ảnh | (không có) |
| 10 | seo-technical-audit | `tmf \| Projects/tmf/data/crawl/crawl_2026-11.csv` | File crawl export (Screaming Frog hoặc tương đương) đặt trong `data/crawl/`, tên `<nguồn>_YYYY-MM.csv`. Extractor cần cột như status_code, title, H1, canonical, word_count, và redirect nếu có. Workflow không tự crawl | THIẾU. `data/crawl/` chỉ có README | Duyệt danh sách ưu tiên | `data/_summary/2026-11_crawl.md`, `outputs/..._audit_tech_...md`, `outputs/..._plan_tech-fix.md` |
| 11 | seo-geo-optimization | `tmf \| 2026-11` | `data/geo/prompts.csv` có dòng prompt (cột prompt_id, prompt, intent, cluster, priority) và `data/geo/citations_2026-11.csv` (cột prompt_id, engine, date, brand_mentioned, cited_url, competitor_cited, position) do người hoặc tool kiểm ChatGPT, Perplexity, Gemini, AI Overviews | THIẾU. `prompts.csv` chỉ có header; `citations_2026-11.csv` chưa có | Duyệt đề xuất, rồi seo-qa-fix | `data/_summary/2026-11_geo.md`, `outputs/..._audit_geo_...md`, `outputs/..._plan_geo.md`, `outputs/..._draft_geo-fix.md` |
| 12 | seo-monthly-report | `tmf \| 2026-11` | Trong `data/`: `gsc/gsc_2026-11.csv`, `ga4/ga4_2026-11.csv`, `rank/rank_2026-11.csv`, `geo/citations_2026-11.csv`, cộng tháng trước (2026-10) để so sánh. Tên chính xác theo quy ước `<nguồn>_YYYY-MM.csv` | THIẾU. Cả 4 thư mục chỉ có README; khách chưa cấp GSC, GA4, Ahrefs. Tháng 11 cũng chưa kết thúc (hôm nay 2026-11-09). Registry chưa có report_day | Duyệt báo cáo trước khi gửi khách | `data/_summary/2026-11_<nguồn>.md`, `outputs/..._report_2026-11.md`, `outputs/..._review_report_2026-11.md`, một dòng trong `_registry/portfolio_kpi.csv` |

## 2. Tác vụ chưa đủ điều kiện: cần gì, đặt ở đâu

Tất cả đường dẫn tính từ `Projects/tmf/`. Không sửa file export gốc. File lớn có thể để trên Drive, ghi link vào `sources.md` (Drive của khách hiện [CẦN XÁC NHẬN]).

| Cần | Đặt ở | Dùng cho bước | Ai cung cấp | Ghi chú |
|---|---|---|---|---|
| Export Ahrefs (Keywords Explorer hoặc Organic keywords) | `data/keywords/ahrefs_2026-11.csv` | 1, 3, 7 | Harry | Chưa có Ahrefs project (`sources.md`). Thiếu thì volume và KD để trống, ghi [CẦN SỐ LIỆU] |
| Export GSC: queries và pages (28 hoặc 90 ngày) | `data/gsc/gsc_queries_2026-11.csv`, `data/gsc/gsc_pages_2026-11.csv` | 1, 2, 12 | Harry xin quyền property từ Rob | GSC property [CẦN XÁC NHẬN] |
| Export GA4 | `data/ga4/ga4_2026-11.csv` | 12 | Harry xin quyền từ Rob | GA4 property ID [CẦN XÁC NHẬN] |
| Rank tracking | `data/rank/rank_2026-11.csv` | 1, 2, 12 | Harry (tool nào, [CẦN XÁC NHẬN]) | Không bắt buộc cho demo |
| Crawl export | `data/crawl/crawl_2026-11.csv` | 2 (tùy chọn), 10 | Harry chạy Screaming Frog hoặc tương đương | Site có 1.729 URL (site_urls.csv). Có thể crawl riêng nhóm hose nếu muốn nhẹ, nhưng khi đó audit chỉ kết luận được cho nhóm đó |
| `url_list.csv` có dữ liệu | `data/inputs/url_list.csv` | 7 | Tôi điền URL sau khi bạn chọn, lấy từ `site_urls.csv`; meta hiện tại đọc từ trang thật | Cần bạn chọn 5 URL: gợi ý 5 sản phẩm trong chính collection này. Không điền khi chưa được chọn |
| `prompts.csv` có dòng + `citations_2026-11.csv` | `data/geo/` | 11, 12 | Prompt: tôi có thể đề xuất (không cần số liệu), bạn duyệt. Citations: người hoặc tool kiểm engine AI | Citations không thể tạo giả; thiếu thì bước 11 và 12 không chạy |
| Link Drive khách, GSC, GA4, Ahrefs, tone, từ cấm, KPI | `sources.md`, `PROJECT.md` | 4, 6, 12 | Harry hỏi Rob | Đang [CẦN XÁC NHẬN]. Tone và từ cấm trống nên bước 4 và 6 chỉ theo luật chung và quy tắc fact của skill TMF |

## 3. Đề xuất phạm vi chạy cho demo

Chạy được ngay (dù thiếu số liệu): 1, 2, 3, 4, 5, 6. Đây là chuỗi viết collection đầy đủ và là phần demo cốt lõi.
Chạy sau khi bổ sung file: 7 (cần url_list), 10 (cần crawl), 11 (cần prompts và citations), 12 (cần GSC, GA4, rank, citations; hợp lý nhất là chạy cho 2026-12 hoặc khi tháng 11 kết thúc).
Bỏ qua: 8, 9.

## 4. Câu hỏi cần bạn trả lời trước khi sang Bước B

1. Duyệt từ khóa chính `truckmount solution hose` (hose parts là phụ), hay giữ `hose parts` làm chính? Nếu giữ, ai sở hữu từ khóa giữa collection này, `hose-cuffs` và `hoses-accessories` (Rob quyết)?
2. Chấp nhận chạy bước 1 và 3 không có số liệu volume, KD (ghi [CẦN SỐ LIỆU]), hay chờ export Ahrefs hoặc GSC?
3. Bước 7: chọn 5 URL cho `url_list.csv` (gợi ý 5 sản phẩm trong collection).
4. Bước 11: bạn có muốn tôi đề xuất `prompts.csv` để bạn duyệt không?
5. Thứ tự chạy: giữ 1 đến 6 như bảng, rồi 7, 10, 11, 12 khi có file?
