# Prompt mẫu cho khách TMF

Dán vào chat của Javis. Prompt 1 dùng chat thường (engine Claude Code, agent SEO Planner hoặc SEO Writer). Prompt 2 dùng agent SEO Planner.

## Prompt 1: cập nhật hồ sơ khách
```
Khách tmf. Cập nhật hồ sơ đầy đủ cho khách này. Chỉ sửa: Projects/tmf/PROJECT.md, Projects/tmf/sources.md, dòng tmf trong Projects/_registry/projects.csv, Projects/tmf/data/inputs/. Không đụng khách khác.

Thông tin tôi biết (không biết thì để trống, đừng đoán):
- Thị trường chính: 
- Người phụ trách: 
- Người duyệt phía khách: 
- KPI và mục tiêu: 
- Đối thủ tôi biết: 
- Tone và wording khách yêu cầu: 
- Từ cấm hoặc claim cấm khách yêu cầu: 
- Link thư mục Drive, GSC property, GA4 property ID, Ahrefs project: 

Việc làm:
1. Mở bằng web fetch: trang chủ, trang giới thiệu, trang giao hàng và đổi trả, 5 collection và 5 sản phẩm của shop.truckmountforums.com. Chỉ ghi vào PROJECT.md những gì đọc được từ trang, mỗi mục kèm URL nguồn. Phần nào không xác minh được thì ghi [CẦN XÁC NHẬN].
2. Mục Thông tin doanh nghiệp: khách là ai, bán gì, cho ai, điểm khác biệt. Tuyệt đối không bịa hãng sản xuất, thông số, chứng nhận.
3. Mục Đối thủ chính: dùng web search để đề xuất, đánh dấu "đề xuất, chưa xác nhận" và kèm URL. Nếu tôi đã nêu đối thủ ở trên thì dùng danh sách của tôi.
4. Mục Tone và Từ cấm: lấy từ thông tin tôi cung cấp. Nếu tôi bỏ trống, ghi [CẦN XÁC NHẬN] và đừng tự đặt claim cấm. Có thể ghi thêm các quy tắc xác minh fact mà skill shopify-collection-seo-tmf đang yêu cầu, ghi rõ nguồn là skill.
5. Lấy sitemap công khai của site, ghi Projects/tmf/data/inputs/site_urls.csv (cột type,url; type là homepage, collection, product, blog hoặc page; chỉ URL có thật trong sitemap). Nếu có Projects/tmf/inputs/site_urls.csv cũ thì gộp vào rồi báo tôi.
6. Cập nhật dòng tmf trong registry với những gì xác minh được; ô còn lại để trống.
7. Cuối cùng báo cáo bảng ngắn: mục nào đã điền (kèm nguồn), mục nào còn thiếu, và tối đa 5 câu hỏi tôi cần trả lời. Chưa commit; đợi tôi duyệt.
```

## Prompt 2: lập run sheet và chạy hết task của dự án (demo TMF)
```
Khách tmf. Bạn là điều phối cho khách này. Đọc Projects/SEO-OPS.md, Projects/tmf/PROJECT.md, sources.md và dòng tmf trong registry.

Nội dung demo: collection https://shop.truckmountforums.com/collections/high-pressure-solution-line-hoses, từ khóa chính "hose parts" (bạn được phép đề xuất từ khóa tốt hơn kèm lý do). Thị trường theo registry.

Bước A, CHƯA chạy gì: lập run sheet cho TẤT CẢ tác vụ trong mục 3 của SEO-OPS.md. Bảng gồm: Thứ tự | Workflow | Dòng đầu vào chính xác (dùng đường dẫn file có thật) | Điều kiện cần có | Đang có đủ chưa | Điểm dừng người duyệt | Đầu ra. Với mỗi tác vụ chưa đủ điều kiện (ví dụ thiếu export GSC, crawl, citations, ahrefs, url_list), ghi rõ thiếu file nào, đặt ở thư mục nào. Tác vụ không áp dụng cho demo (feedback, image-plan khi chưa có blog) ghi "bỏ qua, lý do".

Bước B, sau khi tôi duyệt run sheet: chạy từng workflow theo thứ tự. Nếu bạn không tự chạy được workflow, in ra đúng dòng đầu vào để tôi dán vào trang Workflows. Dừng ở mọi điểm duyệt, nêu câu hỏi, và chỉ chạy tiếp khi tôi trả lời. Sau mỗi workflow báo tối đa 5 dòng gồm đường dẫn file và việc còn mở.

Ràng buộc: không bịa số liệu, nguồn, URL; thiếu thì ghi [CẦN NGUỒN] hoặc [CẦN SỐ LIỆU]. Không dùng thông tin của khách khác.
```
