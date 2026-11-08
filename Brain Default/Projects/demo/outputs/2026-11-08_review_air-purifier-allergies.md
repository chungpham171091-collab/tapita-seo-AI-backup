# Báo cáo audit: Air Purifier for Allergies (demo)

**Bài:** Projects/demo/outputs/2026-11-08_draft_air-purifier-allergies.md
**Từ khóa chính:** air purifier for allergies | **Thị trường:** en-GB
**Căn cứ:** Projects/SEO-OPS.md, Projects/demo/PROJECT.md (từ cấm và claim cấm), tapita-eeat-check, harry-reference-check. Không có skill compliance riêng cho demo (cột compliance trống), nên áp mục "Từ cấm và claim cấm" trong PROJECT.md.

## Lỗi

| # | Vị trí (trích) | Vấn đề | Mức | Cách sửa |
|---|---|---|---|---|
| 1 | Thân bài: "Our purifier is medical grade and cures hay fever... you will never suffer from allergies again"; meta: "cures hay fever ... is medical grade" | Claim y tế và chữa bệnh, bị PROJECT.md cấm. Là thông tin sức khỏe sai lệch, thuộc YMYL (QRG: Harmfully misleading). | P0 | Xóa hoàn toàn. Thay bằng mô tả chức năng đo được (lọc hạt gì, theo tiêu chuẩn nào, có nguồn) và nói rõ máy hỗ trợ, không chữa dị ứng. |
| 2 | "Studies show it removes 99.99% of pollen, dust and germs"; "It is 100% guaranteed to work in every room"; meta "removes 99.99% of germs" | Con số hiệu suất không có nguồn (vi phạm PROJECT.md), không có nghiên cứu nào được dẫn. Không có căn cứ để tin. | P0 | Xóa số liệu. Nếu muốn giữ, phải có nghiên cứu cụ thể đã kiểm chứng, kèm điều kiện thử nghiệm. "100% guaranteed" phải xóa. |
| 3 | "reduces the risk of asthma in children by up to 40%. [CẦN NGUỒN]" và "Experts agree..." | Thống kê y tế chưa có nguồn, đã bị gắn [CẦN NGUỒN] nhưng vẫn nằm trong bài. Không có chuyên gia nào được nêu tên. | P0 | Xóa câu này. Chỉ đưa lại khi có nguồn đã kiểm chứng (tên tổ chức, năm, dữ liệu), và nêu đúng phạm vi nghiên cứu. |
| 4 | "Read more at https://example.com/study-that-does-not-exist for details." | Link trích dẫn giả, trỏ tới tên miền placeholder. Không có nguồn nào được xác thực (harry-reference-check: URL không fetch được, không có nội dung khớp). | P0 | Xóa link. Thay bằng nguồn thật đã mở được và có nội dung khớp claim, hoặc bỏ luôn câu đó. |
| 5 | Meta description: "...guaranteed results, order now and breathe easy forever." | Từ cấm "guaranteed" (PROJECT.md). Cam kết tuyệt đối "forever". | P1 | Viết lại meta description, bỏ "guaranteed" và "forever". |
| 6 | meta_title: "Air Purifier for Allergies" (26 ký tự) | Dưới 40 ký tự (SEO-OPS mục 4). | P1 | Viết lại meta title 40–60 ký tự, chứa từ khóa chính và phản ánh đúng nội dung. |
| 7 | meta_description: 196 ký tự | Vượt 160 ký tự (SEO-OPS mục 4). | P1 | Viết lại còn 140–160 ký tự (tính khoảng trắng). |
| 8 | Toàn bài: khoảng 230 từ | Dưới 1.500 từ, yêu cầu tối thiểu cho blog (SEO-OPS mục 4). Bài mỏng, thiếu nội dung hữu ích. | P1 | Viết lại đủ độ dài, có thông tin cụ thể về cách chọn máy cho người dị ứng (loại lọc, diện tích phòng, bảo trì). Phải có nguồn cho mọi khẳng định. |
| 9 | Cụm "air purifier for allergies" xuất hiện 10 lần trong thân bài trên khoảng 230 từ (H1, đoạn mở, "Why choose" đều nhồi từ khóa) | Nhồi từ khóa (keyword stuffing), đọc không tự nhiên. Đây là dấu hiệu chất lượng thấp (QRG: Low). | P1 | Dùng từ khóa 3–4 lần, xen biến thể tự nhiên ("purifier for hay fever", "HEPA filter at home"). |
| 10 | "Delve into the tapestry of filtration and you will see it is a testament to modern engineering"; "game-changer"; "In today's fast-paced world"; "In conclusion" | Văn phong AI và câu rỗng (filler). Không mang thông tin. QRG: Low (filler). | P1 | Viết lại câu cụ thể, bỏ cụm sáo rỗng. Người viết sửa wording (SEO-OPS mục 4). |
| 11 | Toàn bài: không có tác giả, không có thông tin công ty, không có thử nghiệm hay thông số | E-E-A-T yếu cho chủ đề sức khỏe (QRG: Inadequate E-E-A-T là Low). Không có Experience hay Expertise. | P1 | Thêm tác giả có tên và tiểu sử liên quan, thông tin về cửa hàng (liên hệ, chính sách đổi trả), và thông số thật của sản phẩm (kèm nguồn nhà sản xuất). |
| 12 | "The unit draws air through a filter." | Mô tả chung, không có thông số (loại lọc, CADR, phạm vi phòng). | P2 | Bổ sung thông số kỹ thuật thật, có nguồn. Đây là bước từ Medium lên High. |

## Kiểm tra trích dẫn (harry-reference-check)

- Tổng số tham chiếu: 3 (1 URL, 2 khẳng định thống kê không nguồn). Pass: 0 | Fail: 3.
- URL example.com: FAIL, placeholder không tồn tại theo nội dung bài. Không cần fetch thực tế để kết luận vì domain example.com là domain dành riêng để thử nghiệm.
- Khẳng định 99.99% và 100%: FAIL, không có nguồn trong bài.
- Khẳng định asthma 40%: FAIL, đánh dấu [CẦN NGUỒN] nhưng vẫn được xuất bản.
- Không kiểm được gì thêm vì bài không có tham chiếu thật nào. Không fetch mạng.

## Ghi chú

- Kiểm tra kỹ thuật (crawl, index, tốc độ, schema) nằm ngoài phạm vi, không kiểm tra trong lượt này.
- Khi không chắc claim nào đó đúng sự thật, đều xử lý theo hướng xóa hoặc đưa nguồn thật, không viết lại thành khẳng định chắc hơn.

## Verdict: KHÔNG ĐẠT

Còn 4 lỗi P0 và 7 lỗi P1. Bài phải được sửa lại trước khi làm tiếp.

## Tóm tắt 5 dòng

1. Bài chứa claim chữa bệnh và "medical grade", bị cấm trong PROJECT.md. Đây là P0.
2. Số liệu 99.99%, 100% và thống kê asthma 40% không có nguồn, kể cả khi đã gắn [CẦN NGUỒN]. Đây là P0.
3. Link trích dẫn example.com không phải nguồn thật. Đây là P0.
4. Meta title 26 ký tự, meta description 196 ký tự, bài khoảng 230 từ, vi phạm quy tắc độ dài trong SEO-OPS. Đây là P1.
5. Văn phong AI, nhồi từ khóa (10 lần), thiếu tác giả và thông số. Cần viết lại gần như toàn bộ.

## Kiểm lại

**Bài kiểm:** Projects/demo/outputs/2026-11-08_draft_air-purifier-allergies_v2.md (đọc lại toàn bộ từ đầu, 110 dòng)

| # | Lỗi cũ | Trạng thái | Ghi chú |
|---|---|---|---|
| 1 | Claim chữa bệnh, "medical grade" (P0) | Đạt | Không còn "medical grade". "cure" chỉ còn trong câu phủ định ("does not cure hay fever") |
| 2 | 99.99%, 100%, "guaranteed" (P0) | Đạt | Không còn số liệu hiệu suất |
| 3 | Thống kê asthma 40%, "Experts agree" (P0) | Đạt | Đã xóa |
| 4 | Link example.com (P0) | Đạt | Bài không còn URL nào |
| 5 | "guaranteed", "forever" trong meta (P1) | Đạt | |
| 6 | Meta title 26 ký tự (P1) | Đạt | 45 ký tự, trong khoảng 40–60 |
| 7 | Meta description 196 ký tự (P1) | Đạt | 155 ký tự, trong khoảng 140–160 |
| 8 | Dưới 1.500 từ (P1) | Đạt, sát ngưỡng | Khoảng 1.520 từ (đã bỏ ký hiệu bảng, tính cả heading và placeholder [CẦN]). Khi thay placeholder bằng nội dung thật, phải đếm lại |
| 9 | Nhồi từ khóa (P1) | Đạt | "air purifier for allergies" 5 lần, kể cả H1 |
| 10 | Văn phong AI, câu rỗng (P1) | Đạt | Không còn "In conclusion", "game-changer", "tapestry", "fast-paced". Chưa đánh giá sâu wording, người sửa cần đọc lại |
| 11 | E-E-A-T yếu: thiếu tác giả, cửa hàng, thông số (P1) | **Chưa đạt** | Vẫn là placeholder: dòng 10 (tác giả, tiểu sử), dòng 102 (thông số sản phẩm), dòng 106 (thông tin cửa hàng, chính sách đổi trả, link) |
| 12 | Mô tả chung, không có thông số (P2) | Đã bỏ | Câu cũ không còn. Thông số vẫn chờ ở dòng 102 |

### Lỗi mới phát sinh

- **N1 (P1), thiếu [CẦN NGUỒN] cho khẳng định thực tế.** SEO-OPS mục 4 yêu cầu ghi [CẦN NGUỒN] khi thiếu nguồn. Các đoạn sau đưa ra khẳng định cụ thể nhưng không có nguồn và không có đánh dấu:
  - Dòng 16: "Many common allergy triggers are airborne particles..."
  - Dòng 20: "Allergens that have already settled on bedding, carpets and soft furniture stay there..."
  - Dòng 39: "A unit is usually rated for a room size, and a purifier tends to work best when..."
  - Cách sửa: thêm [CẦN NGUỒN] hoặc nguồn thật cho từng đoạn.
- **N2 (P2), câu kết không rõ nghĩa.** Dòng 110: "get in touch with your room size so we can help you choose". Cách sửa: viết lại câu cuối cho rõ nghĩa.

### Kiểm tra trích dẫn (harry-reference-check)

- Bài không có URL, DOI hay trích dẫn nào được gắn nguồn thật. Không có gì để fetch. Pass: 0 | Fail: 0 | Chưa có nguồn: 14 placeholder [CẦN ...].
- Phần còn lại vẫn phải làm: nguồn cho các placeholder [CẦN NGUỒN] trước khi xuất bản.

### Verdict kiểm lại: KHÔNG ĐẠT

Không còn P0. Còn 1 P1 cũ (#11) chưa xong và 1 P1 mới (N1). Theo SEO-OPS, chỉ đạt khi không còn P0 và P1.
